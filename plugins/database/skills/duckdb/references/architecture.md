# DuckDB Architecture Reference

Current as of DuckDB 2.0.0 LTS (2026-10-21). Version-qualified where behavior differs from 1.4/1.5.

## In-Process Execution Model

> Source: https://duckdb.org/docs/2.0/internals/overview.html
> Source: https://duckdb.org/docs/2.0/connect/concurrency.html

DuckDB runs as an embedded library inside the host application -- no separate server process, no socket, no client-server protocol overhead. (The optional Quack extension can turn an instance into a server; see `quack.md`.)

```
┌─────────────────────────────────────────────┐
│           Host Application                  │
│  (Python, R, Node.js, Java, C++, Rust, Go)  │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │           DuckDB Engine               │  │
│  │  ┌──────────┐  ┌──────────────────┐   │  │
│  │  │  Parser  │  │  Optimizer       │   │  │
│  │  │  (PEG,   │  │  (join ordering, │   │  │
│  │  │  default │  │   filter         │   │  │
│  │  │  in 2.0) │  │   pushdown, ...) │   │  │
│  │  └──────────┘  └──────────────────┘   │  │
│  │  ┌──────────┐  ┌──────────────────┐   │  │
│  │  │ Catalog  │  │ Execution Engine │   │  │
│  │  │ System   │  │ (vectorized,     │   │  │
│  │  │          │  │  push-based)     │   │  │
│  │  └──────────┘  └──────────────────┘   │  │
│  │  ┌──────────────────────────────────┐ │  │
│  │  │  Buffer Manager / Storage        │ │  │
│  │  │  (columnar, compressed,          │ │  │
│  │  │   single-file database)          │ │  │
│  │  └──────────────────────────────────┘ │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Connection and Process Model

- A DuckDB instance opens a database file (or `:memory:`); more databases can be added with `ATTACH`.
- Multiple connections (and writer threads) within one process share the instance.
- **Read-write mode: exactly one process** can open the file and both read and write.
- **Read-only mode: many processes** can read, but only if *every* process opens it read-only (`ATTACH ... (READ_ONLY)`, `duckdb -readonly`, Python `read_only=True`, `access_mode = 'READ_ONLY'`). One read-write opener locks the others out.
- Native multi-process writers are not supported. For writes from multiple processes use the **Quack** remote protocol (client-server, polished in 2.0) or **DuckLake** with a PostgreSQL catalog (DuckLake 1.1 shipped alongside 2.0).
- Cross-process access relies on file locks: be cautious with database files on shared or network directories.

### Thread Model

> Source: https://duckdb.org/docs/2.0/data/io.html
> Source: https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html

- All threads run inside the host process address space, managed by DuckDB's internal pool.
- `threads` defaults to the number of CPU cores.
- **2.0: separate async I/O pool.** `async_threads` defaults to 4x system threads, capped at 256, and serves background reads for Parquet, uncompressed seekable UTF-8 CSV and native storage (JSON stays synchronous). The pool is per instance -- with many instances in one process, set `threads` and `async_threads` explicitly.
- Parallelism starts at the row-group level: a query using k threads needs at least k x 122,880 rows (one default row group per thread) to parallelize fully.

## Query Processing Pipeline

> Source: https://duckdb.org/docs/2.0/internals/overview.html

### 1. Parsing

> Source: https://duckdb.org/docs/2.0/sql/peg_parser.html
> Source: https://duckdb.org/docs/2.0/core_extensions/legacy_parser.html
> Source: https://duckdb.org/docs/2.0/operations_manual/migration.html

- **2.0: the PEG parser is the default.** The PostgreSQL-derived (Bison) parser moved to the `legacy_parser` extension (best-effort support). Pipeline: tokenizer -> PEG parser -> transformer -> binder. Packrat memoization costs a little memory and ms-level overhead; extensions can add grammar.
- **1.5:** PEG was experimental and opt-in via `CALL enable_peg_parser();` -- that call is "no longer required or available" in 2.0. (The setting name `pg_experimental_parser` never existed in official docs; do not use it.)
- Revert to the old parser only to diagnose a regression, then file a GitHub issue:

```sql
INSTALL AND LOAD legacy_parser;   -- INSTALL AND LOAD is new 2.0 syntax
SET enable_legacy_parser = true;  -- autoloads legacy_parser; set false to return
```

- Silent result changes under the 2.0 parser: `~`/`!~` now partial-match like PostgreSQL (`'abc' ~ 'b'` is true; `SET regex_match_operator_semantics = 'full'` restores, deprecated); `!` factorial binds tighter (`2 * 3!` = 12, was 720); `X'..'` -> BLOB, `B'..'` -> BITSTRING. Clause order is strict (`SELECT * WHERE true FROM t` is an error) and `AND` binds tighter than `OR`.

### 2. Binding and Type Resolution

The binder resolves table names, column references, function overloads, and implicit casts:

- Column aliases are resolved early (usable in WHERE, GROUP BY, HAVING -- the "Friendly SQL" behavior); not in a JOIN's ON clause.
- STRUCT/LIST/MAP types are resolved recursively.
- **2.0:** an untyped `NULL` keeps type `NULL` (was INTEGER): `CREATE TABLE t AS SELECT NULL AS x` creates a column that rejects non-NULL inserts. Cast explicitly (`NULL::VARCHAR`) or `SET legacy_disable_null_type = true;`.
- **2.0:** `preserve_identifier_case` is VARCHAR: `'preserve_case'` (default), `'lowercase'`, `'uppercase'`.

### 3. Optimization

> Source: https://duckdb.org/docs/2.0/configuration/overview.html
> Source: https://duckdb.org/docs/2.0/sql/query_syntax/with.html
> Source: https://duckdb.org/docs/2.0/guides/performance/indexing.html
> Source: https://github.com/duckdb/duckdb/releases/tag/v2.0.0
> Source: https://duckdb.org/2026/08/17/duckdb-20-highlights.html

**Rewrite rules:** expression rewriting, filter pushdown, projection pushdown, common subexpression elimination, IN-clause rewriting, subquery unnesting/flattening.

**CTEs:** materialized by default since 1.4. DuckDB can still inline a CTE when heuristics allow (or with `AS NOT MATERIALIZED`); explicit hints are generally not recommended.

**Join ordering:** dynamic programming (DPhyp). Approximate join ordering kicks in at `approximate_join_order_threshold` tables (default 12; configurable since 2.0). Disable individual rules with `disabled_optimizers` (debugging only; list via `duckdb_optimizers()`).

**Physical choices:** hash, merge, nested-loop and index joins; hash vs streaming aggregation; sequential vs index scan. An ART index scan is used only for single-column, non-expression indexes with equality/`IN` predicates, when the expected match count is below `MAX(index_scan_max_count = 2048, index_scan_percentage = 0.001 x rows)`. ART does not speed joins, aggregations or sorts.

**2.0 optimizer additions** (release notes): partial aggregates pushed below joins; grouping sets/ROLLUP/CUBE folded into CTEs; delim joins planned as CTEs by default (`delim_join_as_cte`); partition-aware planning for DuckLake, Iceberg and Hive-partitioned Parquet; remote pushdown that sends SQL to PostgreSQL/MySQL when using `CONNECT`.

**Statistics:** min/max per column per row group from storage, propagated through operators. Zonemaps and Parquet Bloom filters in 2.0 also prune row groups for structs, lists, decimals, UUIDs, `IN` filters and function predicates (e.g. `contains()`, `substr()`).

### 4. Execution

> Source: https://duckdb.org/docs/2.0/internals/vector.html
> Source: https://duckdb.org/docs/2.0/internals/overview.html

DuckDB uses a push-based, vectorized execution model.

#### Push-Based Model

Unlike Volcano-style (pull-based) engines where the root operator calls `next()` on children, DuckDB's operators push data downstream:

```
Source (Scan) --push--> Filter --push--> HashAggregate --push--> Sink (Result)
```

- Pipelines are broken at materialization points (hash table build side, sort, etc.).

#### Vectorized Execution

Operations process columns in batches (vectors) of `STANDARD_VECTOR_SIZE` -- 2048 tuples by default (compiled in; `standard_vector_size` is read-only):

```
Row-at-a-time:                       Vectorized (DuckDB):
  for each row:                        for each vector (2048 rows):
    filter(row); project(row)            filter(vector); project(vector)
```

Benefits: cache-friendly tight loops over one column, SIMD-friendly arithmetic, and per-vector rather than per-row interpretation overhead.

#### Vector Formats

Vectors are not always flat arrays: the engine also uses **constant**, **dictionary** and **sequence** vectors so operators can work without materializing every value. Dictionary vectors pair a child vector with a selection of indices -- this is how filters and dictionary-compressed data avoid copying. 2.0 adds a dictionary-aware cache operator and hash joins that keep dictionaries intact.

#### Parallelism

- Work is split at the row-group level across threads; each pipeline runs in parallel with thread-local state and synchronizes at pipeline breakers (hash table build/merge, sort merge).
- Do not expect parallel speedup on tables or files with fewer row groups than threads.

### 5. Result Materialization

Results are delivered depending on the client: DuckDB vectors/data chunks (C/C++), Arrow tables and readers, Pandas/Polars DataFrames (Python), or row-by-row fetch. (Python 2.0 API changes are in `language-integrations.md`.)

## Storage Architecture

> Source: https://duckdb.org/docs/2.0/internals/storage.html
> Source: https://duckdb.org/docs/2.0/sql/statements/attach.html

### Single-File Database

```
my_database.duckdb          -- main database file
my_database.duckdb.wal      -- write-ahead log (removed after a checkpoint)
```

- File header: `uint64` checksum, magic bytes `DUCK`, then a version field. **Do not trust the header number:** v2.0.0-format files store `999` there. Read the real version with:

```sql
ATTACH 'file.db' AS file_db (READ_ONLY);
SELECT database_name, tags['storage_version'] FROM duckdb_databases();
```

### Storage Versions (2.0 breaking change)

- **2.0 writes storage version 69 by default. DuckDB < 2.0 cannot open it** (1.5.6 errors: "can only read versions between 64 and 68").
- DuckDB 1.0 through 1.5 write version 64 by default; 65-68 only when explicitly opted in.
- 2.0 reads and writes older files and keeps their version, so untouched 1.x files stay readable by 1.x.
- Keep new files 1.x-readable with `ATTACH 'f.db' (STORAGE_VERSION 'v1.5.0')`, `SET storage_compatibility_version = 'v1.5.0'`, or CLI `-storage-version v1.5.6`. The value is the minimum DuckDB version that can read the file. Full upgrade/convert steps: `versions/2.0.md`.
- Backward compatibility (newer reads older) is a goal since 0.10; forward compatibility is best effort only.
- 2.0 format improvements: lazy column-metadata loading (wide tables and large indexes open faster), more compact delete storage, stronger corruption validation on read.

### Row Groups and Blocks

- Tables are horizontal partitions of row groups, default **122,880 rows** (`ROW_GROUP_SIZE` on ATTACH, new files only). Parallelism and compression work per row group.
- Block size default **262,144 bytes** (`BLOCK_SIZE` / `default_block_size`): power of two in [16384, 262144], settable only when creating a file.

```
Table: orders (500,000 rows)
├── Row Group 0: rows 0-122,879
│   ├── Column 'id':      compressed integer segment
│   ├── Column 'amount':  compressed double segment
│   └── Column 'region':  dictionary-encoded string segment
├── Row Group 1: rows 122,880-245,759
└── ...
```

### Column Compression

**Compression applies by default only to persistent databases, not to in-memory ones.** For an in-memory DB, `ATTACH ':memory:' AS db (COMPRESS)` then `CHECKPOINT` after loading.

| Compression | Data Types | Typical fit |
|---|---|---|
| **Constant** | Any | All values in a segment identical |
| **RLE** | Any | Long runs of repeated values |
| **Bit packing** | Integer | Values fit in fewer bits than the type width |
| **FOR** (frame of reference) | Integer | Values clustered around a base |
| **Dictionary** | String, numeric | Low cardinality |
| **FSST** | String | High-cardinality strings |
| **DICT_FSST** | String | Dictionary + FSST; **on by default in 2.0** |
| **ALP** | Float/Double | Floating-point with patterns |
| **Chimp / Patas** | Double | Time-series doubles |
| **Zstd** | String | General-purpose fallback (`zstd_min_string_length` 4096) |

Availability depends on the storage version. Override for testing with `SET force_compression = '...'` or `SET disabled_compression_methods = 'fsst,rle'`.

### Zonemaps (Min/Max Indexes)

> Source: https://duckdb.org/docs/2.0/sql/indexes.html

Min/max indexes are created automatically for general-purpose column types and persisted on disk. Scans skip row groups whose range cannot match:

```sql
-- Row group with min(date) = '2025-06-01', max(date) = '2025-06-30' is skipped:
SELECT * FROM orders WHERE date = '2025-01-15';
```

Zonemaps work best on naturally ordered data (timestamps, auto-increment IDs); sort on load if you filter on a column.

### Buffer Manager and Memory

> Source: https://duckdb.org/docs/2.0/configuration/pragmas.html
> Source: https://duckdb.org/docs/2.0/guides/performance/indexing.html

- Budget: `memory_limit` (default 80% of RAM; 2.0 also accepts percentages, e.g. `'60%'`). It limits the buffer manager only -- actual process memory can be higher.
- 2.0: per-connection `operator_memory_limit` caps sort/hash intermediates.
- Larger-than-memory GROUP BY, JOIN, ORDER BY and window functions spill to `temp_directory` (default `<database_file>.tmp`, or `.tmp` for in-memory), bounded by `max_temp_directory_size` (default 90% of free disk). 2.0 also spills aggregate states. `string_agg()` cannot spill; queries with several blocking operators can still OOM.
- **ART indexes are not buffer-managed in 2.0.0.** Index memory is registered with the buffer manager but never evicted, an index must fit in memory at creation, and large indexes can take much of the budget. Mitigate with `DETACH` + `ATTACH` (indexes deserialize lazily). The "buffer managed indexes" PRs in 2.0 are groundwork only.

```sql
SELECT * FROM duckdb_memory();        -- buffer usage by tag
SELECT * FROM pragma_database_size(); -- file and memory size per database
SELECT current_setting('memory_limit'), current_setting('temp_directory');
```

### Write-Ahead Log and Checkpoints

> Source: https://duckdb.org/docs/2.0/sql/statements/checkpoint.html
> Source: https://duckdb.org/2026/03/09/announcing-duckdb-150.html

- Committed changes go to the WAL; a checkpoint writes WAL contents into the main file. On crash the WAL is replayed at next open.
- Auto-checkpoint when the WAL reaches `checkpoint_threshold` (alias `wal_autocheckpoint`, **default 16 MiB**); `wal_autocheckpoint_entries` (default 0 = off) triggers on entry count.
- `CHECKPOINT;` **fails if transactions are running.** `FORCE CHECKPOINT;` waits for the checkpoint lock and blocks new transactions (before 1.4 it aborted running transactions).
- **Since 1.5.0 checkpointing is non-blocking** for concurrent reads, writes, inserts into indexed tables and deletes.
- Checkpoints reclaim space by merging row groups with many deletes (roughly 25% of rows in adjacent groups deleted); `VACUUM` does not trigger this. 2.0 remaps ART row IDs incrementally during checkpoint vacuum instead of rebuilding.
- `PRAGMA enable_checkpoint_on_shutdown;` checkpoints and deletes the WAL on shutdown; the CLI checkpoints and removes the `.wal` on exit. 2.0 adds per-session `checkpoint_on_detach`.
- Durability knobs: `fsync_mode` (`STANDARD` default, `FULL`, `NONE`); ATTACH `RECOVERY_MODE no_wal_writes` trades crash recovery for speed.

```sql
CHECKPOINT;
FORCE CHECKPOINT;
SET checkpoint_threshold = '1GB';   -- example; default 16 MiB
```

## Catalog System

> Source: https://duckdb.org/docs/2.0/sql/statements/attach.html
> Source: https://duckdb.org/docs/2.0/sql/statements/create_schema.html
> Source: https://duckdb.org/docs/2.0/core_extensions/sqlite.html

DuckDB maintains a transactional catalog:

### Database Hierarchy

```
Database Instance
├── database: memory (or file)
│   ├── schema: main (default)
│   │   ├── tables, views, macros, sequences, types, indexes, triggers (2.0)
│   │   └── nested schemas (2.0): CREATE SCHEMA finance.reports
│   ├── schema: information_schema
│   └── schema: pg_catalog (PostgreSQL compatibility)
├── database: temp (session-scoped temporary objects)
└── attached databases (ATTACH)
```

Nested schemas (2.0) are referenced by the full dot-separated path (`finance.reports.q3`); several catalog pieces are still marked work-in-progress, so avoid relying on resolution or DROP edge cases.

### ATTACH for Multi-Database Queries

```sql
ATTACH 'other.duckdb' AS other_db;
ATTACH 'other.duckdb' AS ro_db (READ_ONLY);
ATTACH 'dbname=mydb' AS pg_db (TYPE postgres);           -- postgres extension
ATTACH 'data.sqlite' AS sqlite_db (TYPE sqlite);          -- sqlite extension
ATTACH 'host=localhost database=mydb' AS my_db (TYPE mysql); -- mysql extension

SELECT a.*, b.* FROM main.orders a JOIN other_db.customers b ON a.customer_id = b.id;
DETACH other_db;
```

- Canonical extension names are `postgres`, `sqlite`, `mysql`; `postgres_scanner`, `sqlite_scanner`, `mysql_scanner` remain aliases. `sqlite_attach` is deprecated.
- Without `TYPE`, the type comes from a scheme prefix (`sqlite:file.db`) or the file header; `TYPE DUCKDB` disables path-based detection.
- **2.0:** paths and option values may be expressions (previously string literals only).
- HTTP/S3 attachments are read-only by default. Attachments are not persisted across sessions.

### Macro System

```sql
-- Scalar macro with a default parameter
CREATE MACRO add_tax(price, rate := 0.08) AS price * (1 + rate);
SELECT add_tax(100);       -- 108.0

-- Table macro
CREATE MACRO recent_orders(days := 30) AS TABLE
    SELECT * FROM orders WHERE order_date > current_date - INTERVAL (days) DAYS;
SELECT * FROM recent_orders(7);
```

## Extension Architecture

> Source: https://duckdb.org/docs/2.0/core_extensions/overview.html
> Source: https://duckdb.org/docs/2.0/extensions/overview.html
> Source: https://duckdb.org/docs/2.0/extensions/extension_repositories.html
> Source: https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/securing_extensions.html

### Loading Mechanism

- Extensions are `.duckdb_extension` binaries loaded at runtime from a local extension directory after `INSTALL` from a repository (default `core`; fallback mirror extensions.duckdb-backup.org).
- Binaries are tied to a DuckDB version and platform; a mismatch is refused, so extensions are rebuilt for every release. Run `UPDATE EXTENSIONS;` after upgrading.
- `LOAD` is needed again after each restart (autoloading covers core extensions).
- `core_functions` is built in; minimal embeddings may need `LOAD core_functions;`.

### Extension Categories

- **Core extensions** -- 31 listed in the 2.0 catalog: primary tier (community support) is only `httpfs`, `icu`, `json`, `parquet`; 22 DuckDB-team secondary-tier extensions (e.g. `spatial`, `iceberg`, `delta`, `ducklake`, `quack`, `legacy_parser`, `postgres`, `sqlite`, `mysql`, `odbc`, `avro`, `excel`, `vss`); third-party with no support tier: `lance`, `motherduck`, `sirius`, `ui`, `vortex`.
- **Community extensions** -- `INSTALL name FROM community;`. Built and signed by DuckDB's CI from published source, but not reviewed: treat as third-party code.
- **Custom repositories (new in 2.0)** -- organizations host extensions signed with their own RSA keys, pinned at `CREATE EXTENSION REPOSITORY ... WITH PREFIX '...'` time. Requires `SET allow_extension_repositories = 'allowed'` (default `undecided`, not persisted). The announcement flags the syntax as work in progress that may change. Details: `best-practices.md`.
- 2.0: `icu` now implements time zones, calendars and collations natively (no ICU library dependency; no query changes). C API v2 is revamped but not yet stable.

### Autoloading

Only core extensions autoload when a function or feature they provide is first used:

```sql
SELECT * FROM read_parquet('s3://bucket/data.parquet');  -- autoinstalls/loads httpfs

SET autoinstall_known_extensions = false;
SET autoload_known_extensions = false;
```

Custom-repository extensions never autoload: use `LOAD my_ext FROM my_repo;`.

### Extension Security

- Signatures are checked on every load (core key, community key, or a custom repository's pinned key).
- `allow_unsigned_extensions` can be set **only at startup** (`duckdb -unsigned` or client config) -- `SET` while running fails. Never enable it in production.
- `SET allow_community_extensions = false;` restricts loading to core and locks the setting.
- Extensions run in-process with full access to host memory and DuckDB's privileges. Load only trusted ones.

## Transaction Model

> Source: https://duckdb.org/docs/2.0/connect/concurrency.html
> Source: https://duckdb.org/docs/2.0/operations_manual/migration.html

DuckDB provides ACID transactions using MVCC with optimistic concurrency control, a fit for read-heavy analytics:

- **Implicit transactions** -- each statement runs in its own transaction unless inside `BEGIN ... COMMIT`.
- **Multiple writer threads** in one process can commit concurrently. **Appends never conflict**, even on the same table; threads may update different tables or different rows of one table.
- Two transactions modifying the **same rows** conflict: the second fails with `Transaction conflict: cannot update a table that has been altered!` Retry the transaction.
- `immediate_transaction_mode` (default false) controls whether `BEGIN` starts the transaction immediately or lazily.
- **2.0: any error inside an explicit transaction aborts it** (previously parser/binder errors left it usable). Later statements fail with "transaction is aborted" until `ROLLBACK`. Restore old behavior: `SET default_transaction_invalidation_policy = 'SYNTACTIC_ERRORS_DO_NOT_INVALIDATE';`

```sql
BEGIN TRANSACTION;
INSERT INTO orders VALUES (1, 'US', 100);
UPDATE inventory SET qty = qty - 1 WHERE id = 1;
COMMIT;
```

### Concurrency Rules

| Operation | Concurrent reads | Concurrent writes (same process) |
|---|---|---|
| Read query | Yes | Yes (reads see their snapshot) |
| Append (INSERT) | Yes | Yes -- appends never conflict |
| UPDATE/DELETE | Yes | Yes, unless two transactions touch the same rows (conflict error) |
| CHECKPOINT | Yes (non-blocking since 1.5.0) | Yes (since 1.5.0); plain `CHECKPOINT` fails while transactions run |
| Other processes | Only if all open read-only | Not natively -- use Quack or DuckLake |

## Data Type System

> Source: https://duckdb.org/docs/2.0/sql/data_types/variant.html
> Source: https://duckdb.org/2026/03/09/announcing-duckdb-150.html

### Numeric Types

| Type | Size | Range |
|---|---|---|
| `TINYINT` | 1 byte | -128 to 127 |
| `SMALLINT` | 2 bytes | -32,768 to 32,767 |
| `INTEGER` | 4 bytes | -2,147,483,648 to 2,147,483,647 |
| `BIGINT` | 8 bytes | -9.2e18 to 9.2e18 |
| `HUGEINT` | 16 bytes | -1.7e38 to 1.7e38 |
| `UHUGEINT` | 16 bytes | 0 to 3.4e38 |
| `UTINYINT`, `USMALLINT`, `UINTEGER`, `UBIGINT` | varies | Unsigned variants |
| `FLOAT` | 4 bytes | IEEE 754 single precision |
| `DOUBLE` | 8 bytes | IEEE 754 double precision |
| `DECIMAL(p, s)` | varies | Exact numeric with precision p, scale s |

2.0: integer `//` and `%` by zero raise an error (were NULL; `TRY(1 // 0)` or `SET error_on_division_by_zero = false` restores NULL); `1 / 0` still returns `inf`. HUGEINT SUM/AVG overflow now throws.

### String Types

| Type | Description |
|---|---|
| `VARCHAR` | Variable-length string (no maximum length) |
| `BLOB` | Binary large object (2.0: `X'..'` literals produce BLOB) |
| `BIT` | Bit string (2.0: `B'..'` literals produce BITSTRING) |

### Date/Time Types

| Type | Description | Example |
|---|---|---|
| `DATE` | Calendar date | `DATE '2025-01-15'` |
| `TIME` | Time of day | `TIME '14:30:00'` |
| `TIMESTAMP` | Date + time (microsecond) | `TIMESTAMP '2025-01-15 14:30:00'` |
| `TIMESTAMP WITH TIME ZONE` | Timestamp + timezone | `TIMESTAMPTZ '2025-01-15 14:30:00+05:00'` |
| `INTERVAL` | Time interval | `INTERVAL 3 DAYS` |

### Complex Types

| Type | Description | Literal |
|---|---|---|
| `LIST` | Ordered array of values | `[1, 2, 3]` |
| `STRUCT` | Named fields (like a row) | `{'name': 'Alice', 'age': 30}` |
| `MAP` | Key-value pairs | `map(['a', 'b'], [1, 2])` |
| `UNION` | Tagged union (sum type) | `union_value(str := 'hello')` |
| `ARRAY` | Fixed-size array | `[1, 2, 3]::INTEGER[3]` |
| `ENUM` | Enumerated type | `CREATE TYPE mood AS ENUM ('happy', 'sad')` |
| `VARIANT` (1.5+) | Typed binary, per-row type metadata | `{'name': 'Alice'}::VARIANT` |
| `GEOMETRY` (1.5+) | Built-in geometry (little-endian WKB, optional CRS) | Spatial data |
| `NULL` (2.0) | Type of an untyped `NULL` column | `SELECT NULL AS x` |

**VARIANT in 2.0:** fully integrated -- shredding in DuckDB files (common same-typed fields stored as typed columns for row groups with at least `variant_minimum_shredding_size` rows, default 30,000; `-1` disables), shredded execution from storage, extraction pushdown into scans, and shredded Parquet read/write. Syntax and `variant_*` functions: `versions/2.0.md`.

## Parallel Execution Details

> Source: https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html
> Source: https://duckdb.org/docs/2.0/dev/profiling.html

### Pipeline Construction

The physical plan is split into pipelines separated by pipeline breakers:

```
Query: SELECT region, sum(amount) FROM orders WHERE amount > 100 GROUP BY region ORDER BY 2 DESC

Pipeline 1 (parallel):  Scan(orders) → Filter(amount > 100) → HashAggregate (sink)
Pipeline breaker:       hash table finalization
Pipeline 2:             HashAggregate (source) → Sort → Result collector
```

### Operator Notes

- Scans parallelize across row groups; filters and projections inherit that parallelism.
- Hash joins: in plans the **probe side is the left operand, the build side the right**.
- Blocking operators that can run larger than memory: GROUP BY, JOIN, ORDER BY, window functions.
- `preserve_insertion_order = false` lets DuckDB reorder results without ORDER BY, cutting memory for large imports/exports; 2.0 also parallelizes `UNION ALL` in that mode.
- Avoid nested-loop joins in favor of hash joins and watch for exploding intermediate cardinality; inspect with `EXPLAIN ANALYZE` (see `diagnostics.md`).

## Sources

- https://duckdb.org/docs/2.0/internals/overview.html
- https://duckdb.org/docs/2.0/internals/vector.html
- https://duckdb.org/docs/2.0/internals/storage.html
- https://duckdb.org/docs/2.0/connect/concurrency.html
- https://duckdb.org/docs/2.0/data/io.html
- https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html
- https://duckdb.org/docs/2.0/guides/performance/indexing.html
- https://duckdb.org/docs/2.0/sql/peg_parser.html
- https://duckdb.org/docs/2.0/core_extensions/legacy_parser.html
- https://duckdb.org/docs/2.0/operations_manual/migration.html
- https://duckdb.org/docs/2.0/configuration/overview.html
- https://duckdb.org/docs/2.0/configuration/pragmas.html
- https://duckdb.org/docs/2.0/sql/query_syntax/with.html
- https://duckdb.org/docs/2.0/sql/statements/attach.html
- https://duckdb.org/docs/2.0/sql/statements/checkpoint.html
- https://duckdb.org/docs/2.0/sql/statements/create_schema.html
- https://duckdb.org/docs/2.0/sql/indexes.html
- https://duckdb.org/docs/2.0/sql/data_types/variant.html
- https://duckdb.org/docs/2.0/core_extensions/overview.html
- https://duckdb.org/docs/2.0/core_extensions/sqlite.html
- https://duckdb.org/docs/2.0/extensions/overview.html
- https://duckdb.org/docs/2.0/extensions/extension_repositories.html
- https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/securing_extensions.html
- https://duckdb.org/docs/2.0/dev/profiling.html
- https://duckdb.org/2026/03/09/announcing-duckdb-150.html
- https://duckdb.org/2026/08/17/duckdb-20-highlights.html
- https://duckdb.org/2026/10/21/announcing-duckdb-200.html
- https://github.com/duckdb/duckdb/releases/tag/v2.0.0

Fetched: 2026-11-13
