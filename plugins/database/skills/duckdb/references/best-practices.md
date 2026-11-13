# DuckDB Best Practices Reference

Current as of DuckDB 2.0.0 LTS. Version-specific behavior is labeled; upgrade hazards live in `versions/2.0.md`.

## Memory and Resource Configuration

> Source: https://duckdb.org/docs/2.0/guides/performance/environment.html
> Source: https://duckdb.org/docs/2.0/configuration/overview.html
> Source: https://duckdb.org/docs/2.0/configuration/pragmas.html

### Memory Limit

```sql
-- Default: 80% of system RAM. Suitable for dedicated analytics workloads.
SELECT current_setting('memory_limit');

SET memory_limit = '8GB';
SET memory_limit = '60%';      -- 2.0: percentages accepted (alias: max_memory)
```

- `memory_limit` caps the buffer manager only; actual process memory can be higher.
- Size by threads: aim for **1-4 GB per thread**. Aggregation-heavy work needs about 1-2 GB/thread, join-heavy about 3-4 GB/thread. Minimum is about 125 MB/thread (8 threads need at least 1 GB).
- When memory is constrained, reduce `threads` (e.g. `SET threads = 4;`) rather than starving each thread.

**When to lower memory_limit:**
- DuckDB shares the machine or container with other memory-hungry processes
- Embedding in an application that runs many instances or connections

**When to raise memory_limit:**
- Dedicated analytics hosts with ample RAM
- Large joins/sorts that spill (check `FROM duckdb_temporary_files();` for spill files)

### Per-Connection Guardrails (new in 2.0)

```sql
SET max_execution_time = 5000;          -- wall-clock ms; default 0 = no limit; RESET restores global
SET operator_memory_limit = '256MB';    -- per-connection cap for sort buffers / hash tables; default NULL
SET max_temp_directory_size = '4GB';    -- default 90% of available disk
```

### Thread Configuration

```sql
-- Default: number of CPU cores
SELECT current_setting('threads');
SET threads = 4;
```

**Guidelines:**
- Default (all cores) suits interactive and dedicated workloads. On HyperThreading hosts DuckDB can launch too many threads; lower `threads` if you see slowdowns.
- Parallelism is per row group: k threads need at least k x 122,880 rows to all be busy.
- **2.0 async I/O:** Parquet, uncompressed seekable UTF-8 CSV, and DuckDB files read through a separate async pool (`async_threads`, default 4x cores, max 256). Do not raise `threads` for these; if remote bandwidth is not saturated, tune `async_threads` and `read_ahead_depth` (default `-1` = unlimited, bounded by memory; `0` = off).
- Synchronous formats (JSON, compressed CSV with many small requests): raise `threads` to roughly 2-5x the core count for remote reads.
- Many DuckDB instances in one process: set `threads` and `async_threads` explicitly; the async pool is per instance.

### Temp Directory

```sql
-- Default: '<database_file>.tmp' next to the database file; '.tmp' for in-memory databases
SELECT current_setting('temp_directory');
SET temp_directory = '/fast-ssd/duckdb_temp.tmp/';
```

**Best practices:**
- Point to fast local storage (SSD/NVMe); HDDs perform poorly, especially for writes.
- Cap spill with `max_temp_directory_size` on shared hosts.
- Larger-than-memory works for GROUP BY, JOIN, ORDER BY, and window functions, in both persistent and in-memory modes. Limits: queries with several blocking operators can still OOM, `string_agg()` cannot spill, and order-sensitive aggregates can OOM on large data.
- For big Parquet/CSV imports or exports that run out of memory, `SET preserve_insertion_order = false;` (results without ORDER BY may be reordered).
- Network storage: read-only use is fine. Avoid the native database format in read-write mode on NFS/SMB; consider DuckLake on object storage instead.

## File Format Selection

> Source: https://duckdb.org/docs/2.0/guides/performance/file_formats.html
> Source: https://duckdb.org/docs/2.0/data/parquet/overview.html
> Source: https://duckdb.org/docs/2.0/data/partitioning/partitioned_writes.html
> Source: https://duckdb.org/2026/10/26/gems-of-duckdb-200.html

### When to Use Parquet

Parquet is the recommended interchange format for DuckDB analytics:

- **Columnar** -- DuckDB reads only needed columns
- **Row-group statistics** -- filters skip row groups; 2.0 extends zonemap and Bloom-filter pruning to structs, lists, decimals, UUIDs, `IN` filters, and function predicates
- **Schema embedded** -- No need to specify column types
- **Parallel** -- row groups are the unit of parallelism; keep total row groups across files >= thread count
- **Async I/O (2.0)** -- reads and writes overlap I/O automatically, mainly helping `s3://` reads

```sql
-- Write. COMPRESSION defaults to snappy; zstd, lz4, lz4_raw, brotli, uncompressed also valid.
COPY orders TO 'orders.parquet' (FORMAT PARQUET, COMPRESSION ZSTD, ROW_GROUP_SIZE 122880);

-- Hive-style partitioned writes (col=value directories)
COPY orders TO 'output' (FORMAT PARQUET, PARTITION_BY (year, month));

-- 2.0: sort rows before writing (within each partition when combined)
COPY orders TO 'orders_sorted' (FORMAT PARQUET, PARTITION_BY (year, month), ORDER_BY (amount DESC NULLS LAST));

-- 2.0: custom partition layout; must be relative, no '..', distinct per partition, requires PARTITION_BY
COPY sales TO 'sales' (FORMAT PARQUET, PARTITION_BY (region),
    PARTITION_PATH CASE WHEN region = 'eu' THEN 'europe' ELSE 'region=' || coalesce(region, 'unknown') END);
```

**Sizing:** row groups of 100K-1M rows (the writer rounds up to a multiple of 2,048); files of 100 MB-10 GB each; aim for >= 100 MB per partition. Prefer lightweight compression (Snappy, LZ4, zstd) over gzip; reserve high zstd levels for write-once/read-many data.

**2.0 read options worth knowing:** `allow_empty` (no matching files returns an empty result instead of an error), `bound_schema`, `int96_as`, `prefetch_strategy`, `utf8_validation` (`strict` default, `replace`, `ignore`), virtual column `file_row_group_number`.

### Query Files Directly vs. Load Into DuckDB

- Query Parquet directly for projection/filter/aggregation workloads or when disk space is limited.
- Load into DuckDB tables for join-heavy workloads, repeated queries on the same data, or when a Parquet query gets a bad join order (native tables carry better statistics). On TPC-H SF30 the docs measured native tables 1.1-4.1x faster (2.8x median) than querying Parquet.

### When to Use CSV

- Source data arrives as CSV (one-time import)
- Interoperability with tools that don't support Parquet
- Human-readable output for small datasets

```sql
SELECT * FROM read_csv('data.csv', header = true);   -- sniffer samples 20,480 rows by default; parallel is on by default

-- Many small CSVs with the same schema: skip sniffing, declare the dialect and types
SELECT * FROM read_csv('data/*.csv', auto_detect = false, header = true, delim = ',',
    columns = {'id': 'INTEGER', 'name': 'VARCHAR'});
```

- `.csv.gz` can be read directly. Non-UTF-8 files need the `encodings` extension.
- 2.0 adds `allow_empty` and `rejects_line_size_limit` to `read_csv`.

### When to Use JSON

- API responses and logs with nested structures
- Semi-structured data exploration

```sql
SELECT * FROM read_json_auto('logs.ndjson', format = 'newline_delimited');
```

JSON stays on synchronous I/O in 2.0; convert hot JSON to Parquet or a DuckDB table for repeated queries.

## Data Loading Strategies

> Source: https://duckdb.org/docs/2.0/guides/performance/import.html
> Source: https://duckdb.org/docs/2.0/sql/statements/merge_into.html
> Source: https://duckdb.org/docs/2.0/operations_manual/migration
> Source: https://duckdb.org/docs/2.0/guides/performance/indexing.html

### Bulk Loading into Tables

Order of preference: a scanner extension (PostgreSQL/MySQL/SQLite/ODBC) > export to Parquet/CSV then load > the client Appender. Avoid single-row INSERTs in loops unless the data is under ~100k rows.

```sql
-- CREATE TABLE AS -- simplest initial load
CREATE TABLE orders AS SELECT * FROM read_parquet('orders/*.parquet');

-- INSERT INTO ... SELECT
INSERT INTO orders SELECT * FROM read_parquet('new_orders.parquet');

-- COPY FROM
COPY orders FROM 'data.csv' (FORMAT CSV, HEADER true);
```

Create indexes and avoid PRIMARY KEY/UNIQUE constraints during bulk loads unless you need them; adding them after the load is faster.

### Incremental Loading Patterns

```sql
-- Append new data
INSERT INTO orders SELECT * FROM read_parquet('new_data_20250115.parquet');

-- Upsert with MERGE (no primary key required; custom match condition)
MERGE INTO orders AS target
USING read_parquet('updates.parquet') AS source
ON target.order_id = source.order_id
WHEN MATCHED THEN UPDATE
WHEN NOT MATCHED THEN INSERT BY NAME;

-- Replace a partition
DELETE FROM orders WHERE year = 2025 AND month = 1;
INSERT INTO orders SELECT * FROM read_parquet('2025/01/*.parquet');
```

- **2.0:** a target row matched by more than one source row in an UPDATE/DELETE branch raises `MERGE INTO command cannot affect the same target row more than once`. Deduplicate the source or make the `ON` condition unique.
- `UPDATE ... FROM` with multiple matches updates the row from one arbitrary source row; it is deterministic only when each target matches at most one source row.
- MERGE also supports `WHEN NOT MATCHED BY SOURCE THEN DELETE` and `RETURNING`. MERGE is not supported on tables with triggers (2.0).

### Loading from Multiple Sources

```sql
-- Combine files with different schemas
SELECT * FROM read_parquet('data/*.parquet', union_by_name = true);

-- Hive-partitioned S3 data (hive_partitioning is auto-detected by default)
CREATE TABLE sales AS
SELECT * FROM read_parquet('s3://bucket/sales/year=*/month=*/*.parquet');

-- Mix file types
SELECT * FROM read_csv('data.csv')
UNION ALL BY NAME
SELECT * FROM read_parquet('data.parquet');
```

## Query Optimization Best Practices

> Source: https://duckdb.org/docs/2.0/sql/dialect/friendly_sql.html
> Source: https://duckdb.org/docs/2.0/guides/performance/indexing.html
> Source: https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html

### Select Only What You Need

The optimizer pushes projections and filters into scans automatically, but a query that genuinely needs fewer columns and rows reads less. Select needed columns and filter remote Parquet; sort or partition data by commonly filtered columns.

```sql
SELECT id, amount FROM read_parquet('large_file.parquet') WHERE sale_date > '2025-01-01';
```

### Leverage Zonemap-Friendly Data Layout

Zonemaps (automatic min/max per row group) prune best on ordered data.

```sql
CREATE TABLE events AS
SELECT * FROM read_parquet('events.parquet')
ORDER BY event_date;

SELECT * FROM events WHERE event_date = '2025-06-15';   -- skips many row groups
```

Prefer auto-increment INTEGER keys over UUIDs for selective lookups. Use the right column types (timestamps as TIMESTAMP, not VARCHAR).

### Avoid Unnecessary Materialization

```sql
-- BAD: intermediate table
CREATE TABLE temp AS SELECT * FROM large_table WHERE condition;
SELECT region, count(*) FROM temp GROUP BY region;
DROP TABLE temp;

-- GOOD: write it directly
SELECT region, count(*) FROM large_table WHERE condition GROUP BY region;
```

### Use QUALIFY Instead of Subqueries

```sql
SELECT * FROM orders
QUALIFY row_number() OVER (PARTITION BY customer ORDER BY date DESC) = 1;
```

### Use GROUP BY ALL and ORDER BY ALL

```sql
SELECT region, product, sum(sales)
FROM orders
GROUP BY ALL
ORDER BY ALL;
```

### Use COLUMNS() for Repetitive Operations

```sql
SELECT min(COLUMNS(*)), max(COLUMNS(*)) FROM measurements;
SELECT avg(COLUMNS('price|quantity|discount')) FROM orders;   -- regex filter
SELECT COLUMNS(lambda c: c LIKE '%price%') FROM orders;        -- 2.0: Python-style lambda; `c -> ...` errors by default
```

### Use FILTER Clause for Conditional Aggregation

```sql
SELECT
    count() FILTER (WHERE region = 'US') AS us_count,
    sum(amount) FILTER (WHERE status = 'completed') AS completed_total
FROM orders;
```

### Use Top-N Per Group Functions

```sql
SELECT region, arg_max(product, amount, 3) AS top_3_products FROM orders GROUP BY region;
SELECT region, max(amount, 5) AS top_5_amounts FROM orders GROUP BY region;
```

### Use ASOF Joins for Time-Series Data

```sql
-- Closest preceding match for point-in-time lookups
SELECT t.*, q.price
FROM trades t
ASOF JOIN quotes q ON t.ticker = q.ticker AND t.ts >= q.ts;
```

### Use INSERT BY NAME for Schema Flexibility

```sql
INSERT INTO target BY NAME SELECT * FROM source;   -- matches columns by name, not position
```

### Prepared Statements and Connections

- Prepared statements pay off mainly for queries under ~100 ms repeated with different parameters.
- Reuse one connection; reconnecting adds overhead and cached metadata is dropped when the last connection closes. Pools help only when non-CPU bottlenecks (network) dominate.

## Python Integration Best Practices

> Source: https://duckdb.org/docs/2.0/clients/python/overview.html
> Source: https://duckdb.org/docs/2.0/clients/python/migration
> Source: https://github.com/duckdb/duckdb-python/releases/tag/v2.0.0
> Source: https://duckdb.org/2026/10/26/gems-of-duckdb-200.html

**2.0 baseline:** the Python client requires Python 3.11+ (free-threaded CPython unsupported; on 3.10 `pip install duckdb` installs a 1.x release).

### Connection Management

```python
import duckdb

# Context manager closes the connection at the end of the block
with duckdb.connect('my_db.duckdb') as con:
    result = con.sql("SELECT * FROM orders").df()

# Notebooks: module-level default in-memory database
duckdb.sql("SELECT 42").show()

# Applications/packages: explicit connection objects with config
con = duckdb.connect('app.duckdb', config={
    'threads': 4,
    'memory_limit': '4GB',
    'temp_directory': '/tmp/duckdb.tmp',
})
```

**Always:**
- Use `con.execute()` for DDL/DML. In 2.0 `con.sql("CREATE TABLE ...")` returns a relation (the statement still runs), and printing a relation re-runs its query.
- Use one `con.cursor()` per thread. A connection handles one call at a time; concurrent use raises `ResourceInUseException`.
- Finish an `execute()` result (read it, `con.complete()`, or `con.abort()`) before the next query, or it raises `ResourceInUseException`.
- After a failed `execute()`, call `con.rollback()`; the transaction is aborted until then.
- To keep a file readable by DuckDB 1.5: `duckdb.connect('f.db', config={'storage_compatibility_version': 'v1.5.0'})`.

### Querying DataFrames In Place

```python
import duckdb
import pandas as pd
import polars as pl
import pyarrow.parquet as pq

df = pd.read_csv('large_file.csv')
duckdb.sql("SELECT region, sum(amount) FROM df GROUP BY region").df()

pdf = pl.read_parquet('data.parquet')
duckdb.sql("SELECT * FROM pdf WHERE amount > 100")

table = pq.read_table('data.parquet')
duckdb.sql("SELECT * FROM table")
```

Pandas DataFrames, Polars DataFrames, and Arrow tables are queried by variable name and are read-only sources.

### Result Conversion

```python
arrow_table = con.sql("SELECT * FROM orders").to_arrow_table()   # .arrow() is not the 2.0 API
reader = con.sql("SELECT * FROM orders").to_arrow_reader()       # batches (default batch size 131,072 rows in 2.0)
df = con.sql("SELECT * FROM orders").df()
polars_df = con.sql("SELECT * FROM orders").pl()
rows = con.sql("SELECT * FROM orders LIMIT 10").fetchall()
```

2.0 removed `fetch_arrow_table()`, `fetch_record_batch()`, `arrow()`, `pl()` from `execute()` results, and `fetchone()`, `fetchmany()`, `execute()`, `fetch_df_chunk()` from relations (use `rel.iter_rows()`, `rel.to_arrow_reader()`, `rel.materialize()`).

### Bulk Insert with Appender (2.0 API)

```python
con.execute("CREATE TABLE events (id INTEGER, label VARCHAR)")
with con.appender("events") as appender:
    appender.append_row(1, "a")
    appender.append_rows([(2, "b"), (3, "c")])
# rows flush when the with-block exits; flush() and clear() also exist
```

## R Integration Best Practices

> Source: https://duckdb.org/docs/2.0/clients/r.html

```r
library(duckdb)
library(DBI)

drv <- duckdb()
con <- dbConnect(drv, dbdir = "analytics.duckdb")

# dbplyr: queries are pushed to DuckDB until collect()
library(dplyr)
orders_tbl <- tbl(con, "orders")
result <- orders_tbl %>%
  filter(amount > 100) %>%
  group_by(region) %>%
  summarize(total = sum(amount, na.rm = TRUE)) %>%
  collect()

# Register an R data.frame as a virtual table (no data transferred yet)
duckdb_register(con, "mtcars_view", mtcars)
dbGetQuery(con, "SELECT cyl, avg(mpg) FROM mtcars_view GROUP BY cyl")

dbDisconnect(con)
duckdb_shutdown(drv)   # shut the database instance down
```

Use `dbWriteTable()` to copy a data frame in. For a dplyr-compatible API backed by DuckDB, see `duckplyr`.

## Deployment Models

> Source: https://duckdb.org/docs/2.0/clients/wasm/overview.html
> Source: https://duckdb.org/docs/2.0/core_extensions/overview.html

### Local Development / Data Science

```python
import duckdb
con = duckdb.connect()   # in-memory
con.sql("SELECT * FROM 'data/*.parquet' LIMIT 10").show()
```

In-memory tables are uncompressed by default. For large in-memory working sets use `ATTACH ':memory:' AS db (COMPRESS); USE db;` and `CHECKPOINT` after loading.

### Persistent Local Database

```python
con = duckdb.connect('analytics.duckdb')
con.execute("CREATE TABLE IF NOT EXISTS orders AS SELECT * FROM 'raw_orders.parquet'")
```

A disk-backed database can outperform in-memory because compression is on by default for disk.

### ETL Pipeline

```python
con = duckdb.connect()
con.execute("""
    COPY (
        SELECT region, date_trunc('month', order_date) AS month, sum(amount) AS total
        FROM read_parquet('s3://bucket/raw/*.parquet')
        GROUP BY ALL
    ) TO 's3://bucket/aggregated/monthly_sales.parquet' (FORMAT PARQUET, COMPRESSION ZSTD)
""")
```

### Browser / Edge (WASM)

```javascript
import * as duckdb from '@duckdb/duckdb-wasm';
const bundle = await duckdb.selectBundle(duckdb.getJsDelivrBundles());
// Worker scripts must be same-origin: wrap the CDN worker script in a Blob URL (see the WASM docs)
const worker = new Worker(workerBlobUrl);
const db = new duckdb.AsyncDuckDB(new duckdb.ConsoleLogger(), worker);
await db.instantiate(bundle.mainModule, bundle.pthreadWorker);
const conn = await db.connect();
```

Limits: single-threaded by default (multithreading experimental), 4 GB memory cap, and remote Parquet through the built-in httpfs path may download the whole file. DuckDB-Wasm is also the docs' first suggestion for sandboxing untrusted SQL.

### MotherDuck

`motherduck` (alias `md`) is a third-party extension; its syntax and hybrid execution are outside this skill's scope.

## Backup and Recovery

> Source: https://duckdb.org/docs/2.0/operations_manual/migration
> Source: https://duckdb.org/docs/2.0/internals/storage.html
> Source: https://duckdb.org/docs/2.0/sql/statements/attach.html

### Full Database Backup

```sql
-- Export to Parquet (portable, version-independent)
EXPORT DATABASE 'backup_20250115' (FORMAT PARQUET, COMPRESSION ZSTD);

-- Cross-database copy
ATTACH 'backup.duckdb' AS backup;
COPY FROM DATABASE main TO backup;
DETACH backup;

-- Backup that DuckDB 1.x can still open (2.0 otherwise writes storage version 69)
ATTACH 'backup_v15.duckdb' AS b15 (STORAGE_VERSION 'v1.5.0');
COPY FROM DATABASE main TO b15;
```

- **2.0 hazard:** new files created by 2.0 use storage version 69, which no 1.x release can open. Pin `STORAGE_VERSION` / `storage_compatibility_version` / CLI `-storage-version` when backups must restore on 1.x.
- Copying the raw `.duckdb` file is only safe while no process has it open for writing.
- Check a file's format with `SELECT database_name, tags['storage_version'] FROM duckdb_databases();`, not the header bytes (2.0-format files store 999 there).

### Recovery

```sql
IMPORT DATABASE 'backup_20250115';
SELECT table_name, estimated_size FROM duckdb_tables();
```

### Incremental Backup Pattern

```sql
COPY (SELECT * FROM orders WHERE modified_at > '2025-01-14')
TO 'incremental_20250115.parquet' (FORMAT PARQUET);
```

## Security Best Practices

> Source: https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/overview.html
> Source: https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/securing_extensions.html
> Source: https://duckdb.org/docs/2.0/configuration/secrets_manager.html
> Source: https://duckdb.org/docs/2.0/sql/statements/attach.html

### Untrusted SQL: Isolate First

SQL runs with the full privileges of the invoking OS user. Treat SQL as code. For untrusted SQL, isolate first (duckdb-wasm, a restricted container, a VM or low-privilege process, OS sandboxing, network isolation, application-level timeouts); DuckDB settings are defense in depth, not a replacement. Never run DuckDB as root. Prepared statements prevent injection only when you control the query structure. Non-SQL APIs (e.g. Python relational filters, which can contain subqueries) can still read files or reach the network, so validate their inputs too.

### File Access Control

```sql
SET enable_external_access = false;
-- Blocks: ATTACH of file databases, COPY to/from files, and read_csv/read_parquet/read_json etc. on external sources
```

### Sandboxed Execution Recipe (order matters, irreversible)

```sql
LOAD httpfs;                                          -- load needed extensions FIRST
SET allowed_directories = ['s3://bucket/prefix/'];    -- or allowed_paths for single files; URLs need their extension loaded first
SET enable_external_access = false;                   -- after this, allow-lists cannot change
SET disabled_filesystems = 'LocalFileSystem';         -- runtime only; also blocks all INSTALL/LOAD until restart
SET allowed_configs = ['memory_limit', 'threads'];    -- optional: keep these adjustable
SET lock_configuration = true;                        -- resource settings do not self-lock
```

- Allow-listed paths are writable as well as readable.
- Before 2.0.0, an `s3://` allow-list entry set without httpfs loaded was silently stored as a local path.
- httpfs reads its CA bundle from the local filesystem. After locking down, HTTPS fails unless an earlier HTTPS request already loaded it, the bundle path is in `allowed_paths`, or `ca_cert_file` points to a certificate.
- The secrets manager opens `secret_directory` lazily. Run `SELECT count(*) FROM duckdb_secrets();` or `SET allow_persistent_secrets = false;` before lockdown, or it stays unusable.
- CLI: `duckdb -safe` (or `.safe_mode`) blocks access to files other than the database.

### Connection Configuration for Untrusted Input

```python
con = duckdb.connect(config={
    'enable_external_access': False,
    'allow_unsigned_extensions': False,
    'allow_community_extensions': False,
    'threads': 2,
    'memory_limit': '512MB',
    'max_temp_directory_size': '1GB',
})
```

### Extension Security

- Signatures are checked on every load. Default trust is core + community. `SET allow_community_extensions = false;` blocks community extensions and locks the setting.
- `allow_unsigned_extensions` can only be set at startup (`duckdb -unsigned` or the client config); `SET` while running fails. Development only.
- Turn off autoinstall/autoload for locked-down hosts: `SET autoinstall_known_extensions = false; SET autoload_known_extensions = false;`.
- **2.0 custom extension repositories** are gated by `allow_extension_repositories` (`undecided` default, `allowed`, `forbidden`; not persisted). Set `'forbidden'` to distrust all custom repositories.

```sql
SELECT extension_name, install_mode, installed_from, signature_key_fingerprint
FROM duckdb_extensions() WHERE installed;
```

### Database Encryption (since 1.4)

```sql
LOAD httpfs;   -- OpenSSL via httpfs is much faster than the built-in mbedtls
ATTACH 'secure.duckdb' AS secure (ENCRYPTION_KEY 'my_secret_key');
ATTACH 'secure2.duckdb' AS secure2 (ENCRYPTION_KEY 'my_secret_key', ENCRYPTION_CIPHER 'GCM');  -- CBC, CTR, or GCM
```

- Default AES-256-GCM. Covers the main database file, WAL, and temporary files. Requires storage version 1.4.0 or later.
- `ENCRYPTION_CONFIG {key: ...}` is not valid syntax; always use `ENCRYPTION_KEY`.
- `temp_file_encryption` (default `false`) is listed as a separate setting; set it explicitly if spill files must be encrypted, since the docs do not reconcile it with the statement that temp files are covered.

### Cloud Credential Management with Secrets

```sql
-- S3: credential chain (AWS SDK) or explicit keys
CREATE SECRET (TYPE s3, PROVIDER credential_chain);
CREATE SECRET my_s3 (TYPE s3, KEY_ID 'AKIAIOSFODNN7EXAMPLE',
    SECRET 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY', REGION 'us-east-1');

-- GCS: HMAC keys generated for GCS interoperability
CREATE SECRET my_gcs (TYPE gcs, KEY_ID 'my_hmac_key_id', SECRET 'my_hmac_secret');

-- Azure
CREATE SECRET my_az (TYPE azure, PROVIDER credential_chain, ACCOUNT_NAME 'myaccount');

-- 2.0: connection-scoped (visible only to this connection, always temporary)
CREATE SECRET tmp_s3 IN connection (TYPE s3, PROVIDER credential_chain);

FROM duckdb_secrets();                                      -- redacted by default
FROM which_secret('s3://my-bucket/file.parquet', 's3');     -- which secret applies
DROP SECRET my_s3;
```

- Never use `SET s3_access_key_id` and the other `s3_*` settings; they are deprecated. 2.0 also disables S3 settings in URL query strings (`?s3_access_key_id=...` becomes part of the object key).
- `SCOPE 's3://my-bucket'` restricts a secret to a prefix; the longest matching prefix wins. Any query can use any defined secret, so a write-capable secret lets queries write to that bucket.
- `CREATE PERSISTENT SECRET` writes the secret **unencrypted** to `~/.duckdb/stored_secrets` (mode 600). Prefer temporary or `IN connection` secrets on shared hosts.
- `allow_unredacted_secrets` can only be set at startup. Avoid it.

### Quack Remote Protocol Security

> Source: https://duckdb.org/docs/2.0/quack/security.html
> Source: https://duckdb.org/docs/2.0/quack/reference.html
> Source: https://duckdb.org/docs/2.0/quack/setup/deployment.html
> Source: https://duckdb.org/quack/faq

A Quack server exposes the **full SQL surface** of its DuckDB instance to anyone holding the token. 2.0 ships a polished Quack, but the Quack FAQ still labels it beta with the protocol not yet stable and breaking changes expected. Pin versions and re-review settings on every upgrade. See `quack.md` for the protocol reference.

```sql
-- Server: localhost bind is the default; supply your own strong token (minimum 4 characters)
CALL quack_serve('quack:localhost', token = 'use_a_long_random_token');

-- Non-local bind is an explicit opt-in, meant only for testing
CALL quack_serve('quack:0.0.0.0:9494', allow_other_hostname = true);

-- Client: keep the token in a secret
CREATE SECRET (TYPE quack, TOKEN 'use_a_long_random_token', SCOPE 'quack:localhost');
ATTACH 'quack:localhost' AS remote (TYPE quack);
```

**Transport.** Local URIs (`localhost`, `127.0.0.1`, `::1`) use plain HTTP. Non-local servers serve HTTPS with a **self-signed certificate** unless `quack_serve` gets `ssl_cert_file` and `ssl_key_file`; clients assume HTTPS for non-local URIs. Never set `DISABLE_SSL` for remote clients.

**Endpoint.** Do not expose Quack directly to the internet. Keep it on localhost behind a proven reverse proxy that terminates TLS, and use the proxy instead of `allow_other_hostname`. The documented AWS recipe runs the extension behind nginx with Let's Encrypt, opening only ports 80 (ACME challenge) and 443.

```
client ──HTTPS:443──▶ reverse proxy (TLS termination) ──HTTP──▶ quack server (localhost:9494)
```

**Quack hardening checklist:**
- Keep the server bound to localhost; firewall port 9494 so only the proxy and loopback reach it.
- Supply your own strong token via `CREATE SECRET (TYPE quack, ...)`; rotate it; never commit it. `duckdb -serve` stores its token in a persistent, unencrypted `quack` secret.
- Authentication hook `quack_authentication_function` (default `quack_check_token`) and authorization hook `quack_authorization_function` (default `quack_nop_authorization`, which allows everything) are GLOBAL settings. Returning `false`/`NULL` or erroring rejects; the authorization hook may return a VARCHAR that replaces the client query.
- For read-only access, attach the database read-only or inspect the **parsed statement type**. A regex on query text is not a filter (`WITH ... INSERT` passes a prefix check).
- Callbacks run on a fresh transient connection: no session state, and Python `create_function` UDFs are not visible.
- Use per-user or per-token auth when several clients connect.

## Common Operational Patterns

> Source: https://duckdb.org/docs/2.0/core_extensions/overview.html
> Source: https://duckdb.org/docs/2.0/sql/statements/connect.html

### Format Conversion

```sql
COPY (SELECT * FROM read_csv('input.csv')) TO 'output.parquet' (FORMAT PARQUET, COMPRESSION ZSTD);
COPY (SELECT * FROM read_json_auto('input.ndjson')) TO 'output.parquet' (FORMAT PARQUET);
COPY (SELECT * FROM read_parquet('input.parquet')) TO 'output.csv' (FORMAT CSV, HEADER true);
COPY (SELECT * FROM read_csv('data/*.csv', union_by_name = true)) TO 'combined.parquet' (FORMAT PARQUET);
```

### Data Federation

```sql
-- Extension names are now postgres / mysql / sqlite (postgres_scanner etc. remain aliases)
INSTALL postgres; LOAD postgres;
ATTACH 'dbname=analytics host=localhost' AS pg (TYPE POSTGRES);

SELECT d.customer_id, d.total_orders, c.customer_name
FROM main.order_summary d
JOIN pg.public.customers c ON d.customer_id = c.id;

-- 2.0: route the whole session to PostgreSQL/MySQL; the remote pushdown optimizer sends SQL to the server
CONNECT 'postgres:dbname=analytics host=localhost';
SELECT count(*) FROM orders;
DISCONNECT;
```

### Scheduling and Automation

```bash
# CLI one-liner for cron jobs
duckdb my_db.duckdb -c "COPY (SELECT * FROM orders WHERE date = current_date - 1) TO 'daily_export.parquet' (FORMAT PARQUET)"
```

Set `max_execution_time` in scheduled jobs so a runaway query cannot hold the database file indefinitely.

### Data Validation Pipeline

```sql
CREATE TEMP TABLE validation AS
SELECT *,
    CASE WHEN amount < 0 THEN 'negative_amount'
         WHEN customer_id IS NULL THEN 'null_customer'
         WHEN order_date > current_date THEN 'future_date'
         ELSE 'valid'
    END AS validation_status
FROM read_parquet('incoming_orders.parquet');

INSERT INTO orders SELECT * EXCLUDE (validation_status) FROM validation WHERE validation_status = 'valid';
COPY (SELECT * FROM validation WHERE validation_status != 'valid') TO 'rejected_orders.parquet' (FORMAT PARQUET);
```

Remember that in 2.0 any error inside an explicit transaction aborts it until `ROLLBACK`.

## Session State Management

> Source: https://github.com/duckdb/duckdb-skills
> Source: https://duckdb.org/docs/2.0/clients/cli/arguments.html

### State File Pattern (duckdb-skills Convention)

When working with DuckDB interactively across multiple sessions or tools, a `state.sql` file can persist session state (attached databases, loaded extensions, macros, secrets):

```sql
-- state.sql: idempotent setup commands
ATTACH IF NOT EXISTS '/absolute/path/to/analytics.duckdb' AS analytics;
USE analytics;
LOAD httpfs;
CREATE SECRET IF NOT EXISTS (TYPE S3, PROVIDER credential_chain);
-- Restore: duckdb -init state.sql
```

**Best practices for state files:**
- Use `ATTACH IF NOT EXISTS` to make statements idempotent (safe to re-run)
- Use absolute paths for database files to avoid working directory issues
- Store per-project state either in `.duckdb-skills/state.sql` (colocated with project) or `~/.duckdb-skills/<project-id>/state.sql` (keeps repo clean)
- The file is append-only -- add new statements, don't edit existing ones
- Gitignore the state file if it contains secrets or local paths

### DuckDB CLI Session Patterns

```bash
# One-liner query against a database
duckdb analytics.duckdb -csv -c "SELECT region, sum(amount) FROM orders GROUP BY ALL"

# Execute a SQL script
duckdb analytics.duckdb < transform.sql

# Restore session from state file and run a query
duckdb -init state.sql -csv -c "FROM orders LIMIT 10"

# Create a file that DuckDB 1.5 can still open
duckdb my.db -storage-version v1.5.6 -c "CREATE TABLE t (x INT);"
```

Use a quoted heredoc (`<<'SQL'`) for multi-line queries to avoid shell quoting issues.

Other useful flags: `-readonly`, `-json`, `-markdown`, `-safe`, `-ui`, and in 2.0 `-serve`, `-connect`, `-agent` / `-no-agent`.

## Performance Anti-Patterns to Avoid

> Source: https://duckdb.org/docs/2.0/guides/performance/file_formats.html
> Source: https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html

1. **Re-scanning Parquet for join-heavy or repeated queries** -- Direct file queries are fine for projection/filter/aggregation; load into DuckDB tables when queries join heavily or repeat on the same data.

2. **Using row-by-row Python loops instead of SQL** -- Push computation into SQL; use `INSERT ... SELECT`, `COPY`, or the Appender for bulk data.

3. **Too many small Parquet files or tiny row groups** -- Aim for 100 MB-10 GB files and 100K-1M-row row groups; very small row groups (2,048 rows) are several times slower.

4. **Heavyweight compression on hot data** -- Snappy (default), LZ4, and zstd decompress fast; avoid gzip for data you query repeatedly.

5. **Ignoring union_by_name for heterogeneous file sets** -- When file schemas evolve, `union_by_name = true` matches by name.

6. **Raising `threads` to speed up remote Parquet on 2.0** -- Async I/O already overlaps reads; tune `async_threads`/`read_ahead_depth` instead.

7. **Using ORDER BY without LIMIT for large results** -- If you need only top-N results, add LIMIT.

8. **Not partitioning large Parquet exports** -- Use `PARTITION_BY (year, month)` for time-series data; filter-friendly Hive partitions pay off most on remote storage.

9. **Default settings in constrained environments** -- In containers or shared servers, set `memory_limit`, `threads`, `temp_directory`, and `max_temp_directory_size` explicitly.

10. **Running musl builds for compute-heavy work** -- Prefer glibc; musl builds can be >5x slower on compute-heavy workloads.

## Sources

- https://duckdb.org/docs/2.0/guides/performance/environment.html
- https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html
- https://duckdb.org/docs/2.0/guides/performance/file_formats.html
- https://duckdb.org/docs/2.0/guides/performance/import.html
- https://duckdb.org/docs/2.0/guides/performance/indexing.html
- https://duckdb.org/docs/2.0/configuration/overview.html
- https://duckdb.org/docs/2.0/configuration/pragmas.html
- https://duckdb.org/docs/2.0/configuration/secrets_manager.html
- https://duckdb.org/docs/2.0/data/parquet/overview.html
- https://duckdb.org/docs/2.0/data/csv/overview.html
- https://duckdb.org/docs/2.0/data/partitioning/partitioned_writes.html
- https://duckdb.org/docs/2.0/sql/statements/merge_into.html
- https://duckdb.org/docs/2.0/sql/statements/attach.html
- https://duckdb.org/docs/2.0/sql/statements/connect.html
- https://duckdb.org/docs/2.0/sql/dialect/friendly_sql.html
- https://duckdb.org/docs/2.0/internals/storage.html
- https://duckdb.org/docs/2.0/operations_manual/migration
- https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/overview.html
- https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/securing_extensions.html
- https://duckdb.org/docs/2.0/core_extensions/overview.html
- https://duckdb.org/docs/2.0/clients/python/overview.html
- https://duckdb.org/docs/2.0/clients/python/migration
- https://github.com/duckdb/duckdb-python/releases/tag/v2.0.0
- https://duckdb.org/docs/2.0/clients/r.html
- https://duckdb.org/docs/2.0/clients/wasm/overview.html
- https://duckdb.org/docs/2.0/clients/cli/arguments.html
- https://duckdb.org/docs/2.0/quack/security.html
- https://duckdb.org/docs/2.0/quack/reference.html
- https://duckdb.org/docs/2.0/quack/setup/deployment.html
- https://duckdb.org/quack/faq
- https://duckdb.org/2026/10/26/gems-of-duckdb-200.html
- https://github.com/duckdb/duckdb-skills

Fetched: 2026-11-13
