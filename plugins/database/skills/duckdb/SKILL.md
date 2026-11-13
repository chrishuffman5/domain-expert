---
name: duckdb
description: "DuckDB as a database engine (2.0 LTS, 1.5, 1.4): internals, SQL dialect, storage format and versions, indexing, extension system, the Quack remote/client-server protocol, upgrades, and query optimization/tuning. Use for \"DuckDB\", \"DuckDB 2.0\", \"duckdb CLI\", \"embedded OLAP\", \"DuckDB extension\", \"httpfs\", \"spatial\", \"duckdb_fdw\", \"DuckDB WASM\", \"duckdb-wasm\", \"Friendly SQL\", \"DuckDB pivot\", \"DuckDB VARIANT\", \"DuckDB CREATE TRIGGER\", \"DuckDB storage version\", \"DuckDB Quack\", \"quack_serve\", \"DuckDB remote protocol\", \"DuckDB client-server\", \"DuckDB performance tuning\". Do NOT use for DuckDB as an ETL/pipeline transformation step (dbt-duckdb, ingesting/transforming files in a data pipeline) — that's the `duckdb` skill in the `etl` plugin. Do NOT use for DuckDB as a BI/analytics query backend (dashboarding, ad-hoc analyst queries) — that's the `duckdb` skill in the `analytics` plugin."
license: MIT
---

# DuckDB

DuckDB is an in-process analytical (OLAP) SQL database. This skill owns the engine angle: internals, storage, configuration, the SQL dialect, extensions, Quack, versions and diagnostics. **DuckDB 2.0.0 LTS (released 2026-10-21) is the current release and the default for every answer**; 1.5 and 1.4 are covered for users still on them.

## Routing

| Request | Load |
|---|---|
| How DuckDB works internally: execution, storage, buffer manager, concurrency, catalog | `references/architecture.md` |
| Memory/threads/temp tuning, file-format choices, loading, security hardening, encryption, secrets, deployment, backup | `references/best-practices.md` |
| Slow query, EXPLAIN/profiling, logging, PRAGMAs, catalog queries, errors after an upgrade | `references/diagnostics.md` |
| Quack server/client setup, `CONNECT`, securing remote access | `references/quack.md` |
| Python, WASM, R, Go, Node, Java, Rust client code | `references/language-integrations.md` |
| Read an unknown file format (`read_any` macro) | `references/file-reading.md` |
| "What's new / breaking in 2.0", storage version 69, upgrading from 1.x, triggers, VARIANT shredding, async I/O | `references/versions/2.0.md` |
| Running 1.5 (VARIANT/GEOMETRY introduced, PEG opt-in, Quack beta) | `references/versions/1.5.md` |
| Running 1.4 LTS (encryption, MERGE, Iceberg writes) | `references/versions/1.4.md` |
| Comparison with other databases | the `overview` skill |

## Versions and Support

| Version | Status (2026-11-13) | Key features | Reference |
|---|---|---|---|
| **DuckDB 2.0** "Cinnamon Teal" | **Current LTS**, released 2026-10-21, EOL 2027-10-22 | Quack + `CONNECT`, async I/O, VARIANT shredding, triggers, PEG parser default, CLI agent mode, extension repositories, storage version 69 | `references/versions/2.0.md` |
| **DuckDB 1.5** "Variegata" | Non-LTS, support extended to 2027-03-01; latest 1.5.6 | VARIANT and GEOMETRY types, Friendly CLI, opt-in PEG parser, ODBC scanner, Azure writes, Quack beta (1.5.3) | `references/versions/1.5.md` |
| **DuckDB 1.4** "Andium" | Previous LTS, **EOL 2026-11-17**; latest 1.4.5 | Encryption (AES-256-GCM), MERGE, Iceberg writes, materialized CTEs | `references/versions/1.4.md` |

- **Always determine the version first** when behavior differs: VARIANT shredding, triggers, `CONNECT` and `$var` are 2.0+; VARIANT/GEOMETRY types 1.5+; MERGE and encryption 1.4+. Ask if unclear; check with `SELECT version();`.
- **2.0.1 is planned for 2026-11-18; 2.1 ("Islandica") for 2027 H1.** For mission-critical systems, the official advice is to test 2.0.0 on a shadow system and consider waiting for 2.0.1.
- **Never assume a file written by 2.0 is readable by 1.x** -- see Storage below.

## In-Process OLAP Architecture

DuckDB runs inside the host process: no server, daemon, port or authentication by default. A persistent database is a single file (plus WAL); it queries host-language data (Pandas/Polars/Arrow) in place and ships as a library for C/C++, Python, R, Node.js, Java, Go, Rust and WASM.

**Concurrency rules (2.0 docs):**
- **Read-write mode:** one process reads and writes the file. Inside that process, multiple writer threads run concurrently under optimistic concurrency control. Appends never conflict; two transactions changing the same rows fail with `Transaction conflict: cannot update a table that has been altered!` -- retry the transaction.
- **Read-only mode:** many processes can read only if **every** process opens the file read-only (`ATTACH ... (READ_ONLY)`, `duckdb -readonly`, `read_only=True`).
- **Multi-process writes:** never point several read-write processes at one file. Use the **Quack** protocol (a server process owns the file) or **DuckLake** with a PostgreSQL catalog.
- **Shared/network storage:** avoid the native format in read-write mode on NFS/SMB; read-only use is fine.

DuckDB is still not a multi-user OLTP server. For high-concurrency OLTP use PostgreSQL/MySQL; for multi-engine lakehouse writes use DuckLake.

## Remote Access via the Quack Protocol

Quack turns a DuckDB process into an HTTP(S) server that other DuckDB processes attach to. It first shipped as a beta core extension in 1.5.3; **2.0 ships a "polished" version with `CONNECT` and `duckdb -serve` / `-connect`, but the Quack FAQ still calls it beta and says the protocol is not yet stable.** Never call it GA. Pin versions on both ends.

```sql
-- Server (binds quack:localhost, port 9494; token min 4 chars)
CALL quack_serve(token = 'super_secret');

-- Client
CREATE SECRET (TYPE quack, TOKEN 'super_secret', SCOPE 'quack:localhost');
ATTACH 'quack:localhost' AS qk (TYPE quack);
CONNECT qk;           -- route the session to the server
FROM my_table;
DISCONNECT;
```

- Clients use plain HTTP for local URIs and HTTPS otherwise. Non-local servers serve HTTPS with a **self-signed certificate** unless given `ssl_cert_file` / `ssl_key_file`.
- **Never expose Quack directly to the internet.** Bind to localhost behind a TLS-terminating reverse proxy; `allow_other_hostname = true` is for testing only.
- The default authorization is permissive: an authenticated client gets the full SQL surface. Install a `quack_authorization_function` for least privilege.

Load `references/quack.md` for parameters, hooks, hardening and limits.

## Execution Engine and Storage

- **Vectorized, push-based execution** over vectors of 2,048 values (`STANDARD_VECTOR_SIZE`). Parallelism starts at the row-group level: a query using k threads needs at least k x 122,880 rows to parallelize fully.
- **Columnar storage in row groups** of 122,880 rows (`ROW_GROUP_SIZE`, new files only), blocks of 256 KiB (`BLOCK_SIZE`, power of two 16 KiB-256 KiB, new files only). Lightweight compression (constant, RLE, bit packing, FOR, dictionary, FSST, ALP, Chimp, Patas, Zstd; `DICT_FSST` on by default in 2.0). Compression applies only to persistent databases unless you `ATTACH ':memory:' AS db (COMPRESS)`.
- **Zonemaps** (min/max per column per row group) are automatic and skip row groups. 2.0 extends pruning to structs, lists, decimals, UUIDs, `IN` lists and function predicates.
- **Spilling:** GROUP BY, JOIN, ORDER BY and window functions can exceed memory via the temp directory. `string_agg()` cannot spill, and queries stacking several blocking operators can still OOM.

### Storage versions (the 2.0 upgrade hazard)

- **2.0 creates files in storage version 69; DuckDB 1.x cannot open them** (`IO Error: Trying to read a database file with version number 69, but we can only read versions between 64 and 68.`).
- 1.0 through 1.5 write version 64 by default. 2.0 reads and writes older files without upgrading them.
- **Keep files readable by 1.x:** `ATTACH 'f.duckdb' (STORAGE_VERSION 'v1.5.0')`, `SET storage_compatibility_version = 'v1.5.0'`, or CLI `-storage-version v1.5.6`.
- **Check a file:** `SELECT database_name, tags['storage_version'] FROM duckdb_databases();` -- never the file header (2.0 files store 999 there).
- **Convert:** old binary `EXPORT DATABASE 'tmp'` -> 2.0 `IMPORT DATABASE 'tmp'`; or `COPY FROM DATABASE src TO dst` into a file pinned to an older `STORAGE_VERSION`.

## Friendly SQL Dialect

```sql
-- Aliases usable in WHERE / GROUP BY / HAVING (not in JOIN ... ON), and laterally
SELECT price * quantity AS total FROM orders WHERE total > 100;
SELECT i + 1 AS j, j + 2 AS k FROM range(5) t(i);

-- Column selection and transformation
SELECT * EXCLUDE (internal_id) FROM customers;
SELECT * REPLACE (upper(name) AS name) FROM customers;
SELECT min(COLUMNS(*)), max(COLUMNS(*)) FROM measurements;
SELECT COLUMNS('price|quantity') FROM orders;                 -- regex
SELECT COLUMNS(lambda c: c LIKE '%price%') FROM orders;       -- 2.0 lambda syntax

-- Aggregation shortcuts
SELECT count() FROM orders;
SELECT count() FILTER (WHERE region = 'US') AS us FROM orders;
SELECT region, product, sum(sales) FROM orders GROUP BY ALL ORDER BY ALL;
SELECT region, product, sum(sales) FROM orders GROUP BY CUBE (region, product);

-- FROM-first, prefix aliases, trailing commas, percentage LIMIT
FROM orders WHERE amount > 100;
SELECT x: 42, y: 'hello';
SELECT region, sum(sales), FROM orders GROUP BY ALL;
SELECT * FROM orders LIMIT 10%;

-- Set operations and inserts by name
SELECT * FROM jan UNION ALL BY NAME SELECT * FROM feb;
INSERT INTO orders BY NAME SELECT * FROM staging_orders;
INSERT OR REPLACE INTO orders SELECT * FROM updated_orders;
CREATE OR REPLACE TABLE summary AS SELECT region, sum(amount) FROM orders GROUP BY ALL;

-- Strings, lists, formatting, dot chaining
SELECT 'DuckDB'[1:4], 'DuckDB'[-2:];                           -- 'Duck', 'DB'
SELECT 'hello world'.upper().replace('WORLD', 'DuckDB');
SELECT [x * 2 FOR x IN [1, 2, 3, 4, 5] IF x > 2];             -- [6, 8, 10]
SELECT format('{} sold {} units', product, quantity) FROM orders;

-- Variables ($name is 2.0+ shorthand for getvariable('name'))
SET VARIABLE my_threshold = 100;
SELECT * FROM orders WHERE amount > $my_threshold;

-- Profiling helpers
DESCRIBE orders;
SUMMARIZE orders;
```

### Lambdas: always use the 2.0 syntax

```sql
SELECT list_transform([1, 2, 3], lambda x : x * 2);       -- [2, 4, 6]
SELECT list_filter([1, 2, 3, 4, 5], lambda x : x > 3);    -- [4, 5]
SELECT list_reduce([1, 2, 3], lambda acc, x : acc + x);   -- 6
SELECT list_filter([1, 3, 1, 5], lambda x, i : x > i);    -- optional 1-based index last
```

Never emit `x -> x + 1` for 2.0: single-arrow lambdas are disabled by default (`SET lambda_syntax = 'enable_single_arrow';` is a temporary bridge, removed in 2.1). On 1.3-1.5 both syntaxes work, so the Python-style form is portable.

### PEG parser (2.0 default) -- silent result changes

- `~` / `!~` now match **partially** (`'abc' ~ 'b'` is true). Anchor the pattern when you mean a full match.
- `2 * 3!` is 12 (factorial binds tighter); parenthesize.
- `X'..'` and `B'..'` produce BLOB / BITSTRING, not VARCHAR.
- Clause order is strict; `ORDER BY true` is rejected. Revert while porting: `INSTALL AND LOAD legacy_parser; SET enable_legacy_parser = true;`.

## SQL Additions in 2.0

```sql
-- Triggers (AFTER row/statement triggers; see 2.0.md for unsupported combinations)
CREATE TRIGGER trg_audit AFTER UPDATE ON target
REFERENCING OLD TABLE AS o NEW TABLE AS n FOR EACH STATEMENT
    INSERT INTO audit SELECT n.id, o.val, n.val FROM o JOIN n ON o.id = n.id;

-- Data-modifying CTEs
WITH moved AS MATERIALIZED (DELETE FROM staging RETURNING *)
INSERT INTO archive SELECT * FROM moved;

-- Nested schemas, JSON mutation, standard pagination, GROUP BY UNNEST
CREATE SCHEMA finance.reports;
SELECT json_set('{"a": 1}', '$.b', '2');
SELECT * FROM t ORDER BY id OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY;
SELECT unnest(tags) AS tag, count(*) FROM posts GROUP BY unnest(tags);

-- Nearest-neighbor join (example form; formal grammar not documented here)
SELECT q.user_id, t.product_id
FROM users q LEFT JOIN products t NEAREST 1
    BY DISTANCE array_distance(q.embedding, t.embedding);
```

- **Triggers break upserts:** `MERGE INTO` fails on any table with triggers, and `INSERT ... ON CONFLICT` / `INSERT OR REPLACE` / `INSERT OR IGNORE` fail on tables with UPDATE or DELETE triggers. `BEFORE ... FOR EACH ROW` and `UPDATE ... FOR EACH ROW` are not supported yet.
- **MERGE INTO** errors when a target row matches several source rows; `UPDATE ... FROM` silently picks an arbitrary matching row. Deduplicate sources.
- Also new: `JOIN BY (TYPE semi|anti|mark|...)`, `setval()`, `regexp_extract(s, p, 'i')` options, `CREATE SECURE VIEW`, `SHOW <setting>` (and `SHOW <table>` deprecated -- use `DESCRIBE`).

## Joins, Top-N, Windows, PIVOT

```sql
-- ASOF: closest preceding match on ordered keys
SELECT t.*, q.price FROM trades t ASOF JOIN quotes q ON t.ticker = q.ticker AND t.ts >= q.ts;
-- POSITIONAL and LATERAL
SELECT * FROM table_a POSITIONAL JOIN table_b;
SELECT c.name, o.* FROM customers c,
    LATERAL (SELECT * FROM orders WHERE customer_id = c.id ORDER BY amount DESC LIMIT 3) o;

-- Top-N per group without window functions
SELECT region, max(amount, 3), arg_max(product, amount, 3), max_by(product, revenue, 5)
FROM sales GROUP BY region;

-- QUALIFY filters window results directly
SELECT customer_id, order_date,
       row_number() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
FROM orders QUALIFY rn = 1;

-- PIVOT / UNPIVOT
PIVOT orders ON product USING sum(amount) GROUP BY region;
UNPIVOT monthly_sales ON COLUMNS(* EXCLUDE (id, name)) INTO NAME month VALUE sales;
```

## Complex Types and VARIANT

```sql
SELECT [1, 2, 3] AS l, {'name': 'Alice', 'age': 30} AS s, map(['k1'], ['v1']) AS m;
SELECT union_value(str := 'hello')::UNION(str VARCHAR, num INTEGER);
SELECT unnest([1, 2, 3]);

-- VARIANT: typed binary per row (1.5+); shredded storage and full variant_* set in 2.0
SELECT '{"user": {"id": 42}}'::JSON::VARIANT AS v;
SELECT data.name, variant_typeof(data), variant_extract_string(data, 'name') FROM events;
```

- Prefer VARIANT over JSON text for semi-structured columns you query repeatedly on 2.0: common structure is shredded into typed columns (row groups with at least `variant_minimum_shredding_size` = 30,000 rows; `-1` disables).
- A `JSON` type backed by VARIANT is planned, not shipped.

## File Format Integration

```sql
SELECT * FROM 'data.parquet';                                    -- auto-detected reader
SELECT * FROM read_parquet('data/year=*/month=*/*.parquet', hive_partitioning = true);
SELECT * FROM read_csv('data/*.csv', union_by_name = true, filename = true);
SELECT * FROM read_json('data.json');
SELECT * FROM read_xlsx('report.xlsx', sheet = 'Sheet1');        -- .xlsx only; .xls unsupported
SELECT * FROM read_parquet('in/*.parquet', allow_empty = true);  -- 2.0: no error on empty glob

-- Remote files: authenticate with secrets, never SET s3_* or URL parameters
CREATE SECRET (TYPE s3, PROVIDER credential_chain);
SELECT * FROM read_parquet('s3://my-bucket/data/*.parquet');
SELECT * FROM read_csv('https://example.com/data.csv');
```

- `SET s3_access_key_id` and friends are deprecated; 2.0 also treats `?s3_...=` URL parameters as part of the object key.
- Querying Parquet directly is efficient for scans, filters and aggregates; load into DuckDB tables for join-heavy or repeated workloads (better statistics; the docs measured 1.1-4.1x faster queries, 2.8x median, on TPC-H SF30 with default settings).

### Writing and exporting

```sql
COPY orders TO 'orders.parquet' (FORMAT PARQUET, COMPRESSION ZSTD);   -- default compression: Snappy
COPY orders TO 'out' (FORMAT PARQUET, PARTITION_BY (year, month), ORDER_BY (amount DESC));  -- ORDER_BY 2.0+
COPY orders TO 'out' (FORMAT PARQUET, PARTITION_BY (region),
    PARTITION_PATH 'region=' || coalesce(region, 'unknown'));        -- 2.0+: custom relative paths
COPY orders TO 'orders.xlsx' (FORMAT xlsx, HEADER true);
EXPORT DATABASE 'backup_dir' (FORMAT PARQUET);
IMPORT DATABASE 'backup_dir';
ATTACH 'target.duckdb' AS target_db;
COPY FROM DATABASE memory TO target_db;
```

Universal reader macro: `references/file-reading.md`.

## Extension Ecosystem

```sql
INSTALL httpfs; LOAD httpfs;          -- core extensions also autoload on first use
INSTALL AND LOAD spatial;             -- 2.0 syntax
INSTALL h3 FROM community; LOAD h3;
SELECT extension_name, installed, extension_version FROM duckdb_extensions();
UPDATE EXTENSIONS;                    -- always after upgrading DuckDB
```

| Extension | Tier (2.0 catalog) | Purpose |
|---|---|---|
| `httpfs` (aliases http, https, s3), `json`, `parquet`, `icu` | Primary | Remote files/S3; JSON; Parquet; time zones, calendars, collations (native since 2.0, ICU library removed) |
| `spatial`, `excel`, `avro`, `fts`, `inet`, `vss`, `encodings` | Secondary | GIS; .xlsx read/write; Avro; full-text search; IP types; vector similarity; CSV in 1,000+ encodings |
| `sqlite`, `postgres`, `mysql`, `odbc` | Secondary | Federation; old `*_scanner` names are aliases. Attach with `ATTACH ... (TYPE sqlite)` |
| `iceberg`, `delta`, `ducklake`, `unity_catalog` | Secondary | Lakehouse formats/catalogs (DuckLake 1.1 requires 2.0) |
| `aws`, `azure` | Secondary | Credential chains; Azure Blob/ADLS |
| `quack` | Secondary | Remote client-server protocol |
| `legacy_parser` | Secondary | Pre-2.0 parser bridge |
| `autocomplete`, `tpch`, `tpcds` | Secondary | CLI completion; benchmark generators |
| `lance`, `vortex`, `ui`, `motherduck`, `sirius` | Third party | Not covered by DuckDB team support |

- Autoloading applies only to core extensions. Extension binaries are tied to a DuckDB version and platform.
- **2.0 custom extension repositories** (`CREATE EXTENSION REPOSITORY ... WITH PREFIX ...`, gated by `allow_extension_repositories`) let organizations host extensions signed with their own keys. The syntax may change. See `references/versions/2.0.md`.
- `substrait` is no longer in the core catalog; `osx_amd64` support is dropped in 2.1.

## Client Integrations

Load `references/language-integrations.md`. Key 2.0 facts: the Python client requires Python 3.11+, results use `.to_arrow_table()` (not `.arrow()`), an unread `execute()` result raises `ResourceInUseException`, and `con.appender("t")` is a context manager. Go moved to `github.com/duckdb/duckdb-go/v2`.

## Query Optimization

### EXPLAIN and profiling

```sql
EXPLAIN SELECT region, sum(amount) FROM orders GROUP BY region;
EXPLAIN ANALYZE SELECT region, sum(amount) FROM orders GROUP BY region;
EXPLAIN (FORMAT json) SELECT ...;            -- text, graphviz, html, json, mermaid, web (CLI)

CALL enable_profiling(format := 'json', save_location := '/tmp/profile.json');
SELECT region, sum(amount) FROM orders GROUP BY region;
CALL disable_profiling();
SET tracked_metrics = ['query.*', 'operator.*'];   -- replaces custom_profiling_settings
```

- Read `EXPLAIN ANALYZE` for the dominant operator, estimated vs. actual cardinality, and (for remote reads) total requests and bytes transferred. Hash join: probe side left, build side right.
- Never assign settings with `PRAGMA x = y` on 2.0 (deprecated); use `SET`. `profiling_mode` has no effect in 2.0.

### Performance tuning

```sql
SET memory_limit = '8GB';          -- default 80% of RAM; 2.0 also accepts '60%'
SET threads = 8;                   -- default: CPU cores
SET temp_directory = '/fast/ssd/duckdb_tmp';   -- default <dbfile>.tmp, or .tmp for in-memory
SET max_temp_directory_size = '100GB';         -- default 90% of free disk
SET preserve_insertion_order = false;          -- lowers memory on huge Parquet/CSV import/export
SET max_execution_time = 60000;                -- 2.0: wall-clock ms limit
SET operator_memory_limit = '2GB';             -- 2.0: per-connection cap for sorts/hash tables
SET checkpoint_threshold = '16MB';             -- alias wal_autocheckpoint; 16 MiB is the default
```

- **Size memory at 1-4 GB per thread** (about 1-2 GB for aggregation-heavy, 3-4 GB for join-heavy; at least 125 MB per thread). When memory is tight, reduce `threads` before lowering `memory_limit`.
- **Async I/O (2.0):** never raise `threads` to speed up Parquet, seekable CSV or native-file reads -- tune `async_threads` (default 4 x cores, max 256) and `read_ahead_depth` (default `-1`) instead. Raise `threads` to about 2-5x cores only for synchronous formats such as JSON or compressed CSV.
- **Parquet layout:** files of 100 MB-10 GB, row groups of 100K-1M rows, at least as many total row groups as threads.
- **Types matter:** store timestamps as TIMESTAMP, not VARCHAR; avoid unneeded PK/UNIQUE constraints on bulk loads (or add them after loading).
- **Reuse connections:** cached metadata is lost when the last connection closes.

### Indexing

```sql
CREATE INDEX idx_orders_id ON orders(order_id);    -- ART index; no OR REPLACE
SELECT * FROM duckdb_indexes();
```

- Rely on zonemaps first; sort or partition data on common filter columns to tighten them.
- ART indexes speed up point lookups and very selective (<0.1%) filters on a single non-expression column, and enforce PK/UNIQUE. They do nothing for joins, aggregations or sorts.
- **ART indexes are not buffer-managed in 2.0.0:** index buffers are never evicted and an index must fit in memory at creation. Create indexes after bulk loads; `DETACH` + `ATTACH` to shed index memory. UPDATEs on indexed columns run as DELETE + INSERT.

## Security Essentials

```sql
-- Encryption (1.4+): AES-256-GCM over the file, WAL and temp files
LOAD httpfs;                                                  -- OpenSSL backend, much faster
ATTACH 'secure.duckdb' AS secure (ENCRYPTION_KEY 'from-a-secret-manager');

-- Lockdown order matters and is irreversible until restart
LOAD httpfs;
SET allowed_directories = ['s3://bucket/prefix/'];
SET enable_external_access = false;
SET disabled_filesystems = 'LocalFileSystem';
SET lock_configuration = true;
```

- Never write `ENCRYPTION_CONFIG {key: ...}` -- the options are `ENCRYPTION_KEY` and `ENCRYPTION_CIPHER` (`GCM` default, `CBC`, `CTR`).
- SQL runs with the invoking user's privileges. Run untrusted SQL in a sandbox (container, VM, duckdb-wasm); settings are defense in depth only.
- Persistent secrets are stored unencrypted on disk. Use `CREATE SECRET ... IN connection` (2.0) for connection-scoped, temporary secrets.
- `allow_unsigned_extensions` can only be set at startup (`duckdb -unsigned`). Set `allow_community_extensions = false` for untrusted workloads.

Full checklist: `references/best-practices.md`.

## Common Pitfalls

1. **Upgrading one process to 2.0 in a mixed fleet** -- it creates version-69 files that 1.x readers reject. Pin `storage_compatibility_version` until every reader runs 2.0.
2. **Copying 1.x SQL into 2.0 unchanged** -- `->` lambdas fail; `~` regex, `!` factorial and `X''` literals return different results; integer `//` / `%` by zero now error; `CREATE TABLE AS SELECT NULL` creates an unusable `"NULL"` column.
3. **Ignoring transaction aborts** -- in 2.0 any error inside `BEGIN ... COMMIT` aborts the transaction; issue `ROLLBACK` before continuing.
4. **Several read-write processes on one file** -- only one process may open it read-write. Use read-only mode, Quack, or DuckLake.
5. **Treating Quack as production-stable or exposing it directly** -- the protocol is not yet declared stable; always use a TLS-terminating reverse proxy and an authorization function.
6. **Adding triggers to upserted tables** -- MERGE and `INSERT OR REPLACE` / `ON CONFLICT` stop working on those tables.
7. **Raising `threads` for remote Parquet on 2.0** -- async I/O already overlaps reads; tune `async_threads` / `read_ahead_depth`.
8. **Setting `memory_limit` too low** -- forces spilling; reduce threads first. Remember `string_agg()` cannot spill.
9. **Expecting ART indexes to be evicted** -- in 2.0.0 they stay in memory; avoid indexes that do not fit.
10. **Credentials in `SET s3_*` or URLs** -- deprecated and, for URL parameters, ignored in 2.0. Use `CREATE SECRET`.
11. **Docker without a volume for the database file** -- data is lost when the container stops.
12. **Skipping `UPDATE EXTENSIONS` after an upgrade** -- extension binaries are version-specific; community extensions publish per-version compatibility matrices.

## Reference Files

- `references/architecture.md` -- execution engine, storage format and versions, buffer manager, concurrency, catalog, extensions internals, data types. Read for "how does DuckDB work internally".
- `references/diagnostics.md` -- EXPLAIN/profiling, logging, PRAGMAs and `duckdb_*` catalog functions, memory and spill diagnostics, file-reader options, CLI commands, errors after upgrading to 2.0.
- `references/best-practices.md` -- memory/threads/async I/O tuning, file formats, loading, client patterns, deployment, backup, security hardening, encryption, secrets, Quack security.
- `references/quack.md` -- Quack server/client setup, `CONNECT`, parameters, auth hooks, hardening, limits.
- `references/language-integrations.md` -- Python (2.0 breaking changes), WASM, R, Go/Node/Java/Rust notes.
- `references/file-reading.md` -- the `read_any` macro and formats it deliberately skips.
- `references/versions/2.0.md` -- 2.0 release status, features with syntax, breaking changes and revert switches, storage compatibility, upgrade checklist, 2.1 removals.
- `references/versions/1.5.md`, `references/versions/1.4.md` -- per-line features, patch history, support status.

## External Resources

- **DuckDB Skills plugin (Claude Code)** -- https://github.com/duckdb/duckdb-skills -- official plugin with `attach-db`, `query`, `read-file`, `duckdb-docs`, `install-duckdb`, `read-memories`; skills share a `state.sql` session file. Install via `/plugin marketplace add duckdb/duckdb-skills`, then `/plugin install duckdb-skills@duckdb-skills`.
- **DuckDB documentation** -- https://duckdb.org/docs/2.0/ (also reachable as `/docs/current/`).
- **DuckDB blog / release notes** -- https://duckdb.org/news/
- **DuckLake documentation** -- https://ducklake.select/docs/stable/

## Sources

- https://duckdb.org/release_calendar
- https://duckdb.org/2026/10/21/announcing-duckdb-200.html
- https://duckdb.org/2026/10/26/gems-of-duckdb-200.html
- https://duckdb.org/docs/2.0/operations_manual/migration.html
- https://duckdb.org/docs/2.0/internals/storage.html
- https://duckdb.org/docs/2.0/internals/overview.html
- https://duckdb.org/docs/2.0/sql/statements/attach.html
- https://duckdb.org/docs/2.0/connect/concurrency.html
- https://duckdb.org/docs/2.0/sql/dialect/friendly_sql.html
- https://duckdb.org/docs/2.0/sql/functions/lambda.html
- https://duckdb.org/docs/2.0/sql/peg_parser.html
- https://duckdb.org/docs/2.0/sql/statements/create_trigger.html
- https://duckdb.org/docs/2.0/sql/query_syntax/with.html
- https://duckdb.org/docs/2.0/sql/query_syntax/from.html
- https://duckdb.org/docs/2.0/sql/statements/merge_into.html
- https://duckdb.org/docs/2.0/sql/data_types/variant.html
- https://duckdb.org/docs/2.0/quack/overview.html
- https://duckdb.org/docs/2.0/quack/security.html
- https://duckdb.org/quack/faq
- https://duckdb.org/docs/2.0/core_extensions/overview.html
- https://duckdb.org/docs/2.0/extensions/overview.html
- https://duckdb.org/docs/2.0/extensions/extension_repositories.html
- https://duckdb.org/docs/2.0/core_extensions/httpfs/s3api.html
- https://duckdb.org/docs/2.0/core_extensions/excel.html
- https://duckdb.org/docs/2.0/data/parquet/overview.html
- https://duckdb.org/docs/2.0/data/partitioning/partitioned_writes.html
- https://duckdb.org/docs/2.0/data/io.html
- https://duckdb.org/docs/2.0/configuration/overview.html
- https://duckdb.org/docs/2.0/configuration/pragmas.html
- https://duckdb.org/docs/2.0/dev/profiling.html
- https://duckdb.org/docs/2.0/guides/performance/environment.html
- https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html
- https://duckdb.org/docs/2.0/guides/performance/file_formats.html
- https://duckdb.org/docs/2.0/guides/performance/schema.html
- https://duckdb.org/docs/2.0/guides/performance/indexing.html
- https://duckdb.org/docs/2.0/sql/indexes.html
- https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/overview.html
- https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/securing_extensions.html
- https://duckdb.org/docs/2.0/configuration/secrets_manager.html
- https://duckdb.org/docs/2.0/clients/python/migration.html
- https://duckdb.org/roadmap
- https://github.com/duckdb/duckdb-skills

Fetched: 2026-11-13
