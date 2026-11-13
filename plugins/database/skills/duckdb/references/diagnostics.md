# DuckDB Diagnostics Reference

Current as of DuckDB 2.0.0 LTS. Version-specific changes are marked "2.0". Assign settings with `SET name = value`; the `PRAGMA name = value` assignment form is deprecated in 2.0 and emits a warning (function-style PRAGMAs such as `PRAGMA table_info('t')` are unaffected).

## System Catalog Queries

> Source: https://duckdb.org/docs/2.0/configuration/pragmas.html
> Source: https://duckdb.org/docs/2.0/sql/meta/duckdb_table_functions.html
> Source: https://duckdb.org/docs/2.0/internals/storage.html

### Database Size and Storage

```sql
-- 1. File and memory size per database
PRAGMA database_size;
SELECT * FROM pragma_database_size();

-- 2. Storage info for a specific table (per-column segments and compression)
PRAGMA storage_info('orders');

-- 3. Storage info as a query (allows filtering)
SELECT * FROM pragma_storage_info('orders')
WHERE column_name = 'amount';

-- 4. 2.0: table-function form can add a segment_info column
SELECT * FROM pragma_storage_info('orders', include_segment_info := true);

-- 5. Table info (column names, types, nullability)
PRAGMA table_info('orders');
SELECT * FROM pragma_table_info('orders');

-- 6. Show tables
SHOW TABLES;
SHOW ALL TABLES;

-- 7. Describe a table or query
DESCRIBE orders;
DESCRIBE SELECT * FROM orders;
-- 2.0: `SHOW orders;` to describe a table is deprecated (prints a warning) -- use DESCRIBE.
-- 2.0: `SHOW threads;` prints a setting when no table has that name
--      (controlled by show_behavior = 'auto' | 'table' | 'setting').

-- 8. Block-level metadata
PRAGMA metadata_info;   -- block_id, total_blocks, free_blocks, free_list
```

### Storage Version of a Database File (2.0)

```sql
-- 9. Read the storage version from duckdb_databases() tags
ATTACH 'file.db' AS file_db (READ_ONLY);
SELECT database_name, tags['storage_version'] FROM duckdb_databases();
-- Do NOT trust the header number after the magic bytes: v2.0.0-format files store 999 there.
```

2.0 writes storage version 69 by default; DuckDB before 2.0 cannot open such files. An older reader fails with:
`IO Error: Trying to read a database file with version number 69, but we can only read versions between 64 and 68.`
DuckDB 1.5.5 and earlier report 999 instead of 69 in that message. Fix by writing a copy with an older storage version (see Backup and Export Diagnostics) or by upgrading every reader to 2.0.

### System Metadata Functions

```sql
-- 10. Tables with size/shape metadata
SELECT table_name, estimated_size, column_count, index_count, has_primary_key, temporary
FROM duckdb_tables();

-- 11. Columns (2.0 adds is_generated, generation_expression)
SELECT * FROM duckdb_columns() WHERE table_name = 'orders';

-- 12. Indexes, views, sequences, schemas, types, constraints
SELECT * FROM duckdb_indexes();
SELECT * FROM duckdb_views();
SELECT * FROM duckdb_sequences();
SELECT * FROM duckdb_schemas();
SELECT * FROM duckdb_types();
SELECT * FROM duckdb_constraints();

-- 13. All databases (including attached); path, type, readonly, options, tags
SELECT * FROM duckdb_databases();

-- 14. Functions (2.0 adds extension_name; window functions are now catalog entries)
SELECT DISTINCT function_name, function_type, return_type
FROM duckdb_functions()
WHERE function_name LIKE '%parquet%';

-- 15. 2.0 additions
SELECT * FROM duckdb_triggers();               -- trigger_name, table_name, action_timing, event_manipulation, for_each
SELECT * FROM duckdb_extension_repositories(); -- custom extension repositories
SELECT * FROM duckdb_secret_types();           -- registered secret types
SELECT * FROM duckdb_available_metrics();      -- profiling metrics

-- 16. Other session/catalog introspection
SELECT * FROM duckdb_prepared_statements();
SELECT * FROM duckdb_variables();
SELECT * FROM duckdb_dependencies();
SELECT * FROM duckdb_optimizers();             -- rule names usable in disabled_optimizers
SELECT * FROM duckdb_connection_count();

-- 17. Version and platform
SELECT version();
PRAGMA version;
PRAGMA platform;
```

### Information Schema (SQL Standard)

```sql
-- 18. Tables, columns, schemata via information_schema
SELECT table_schema, table_name, table_type FROM information_schema.tables;
SELECT table_name, column_name, data_type, is_nullable
FROM information_schema.columns WHERE table_schema = 'main'
ORDER BY table_name, ordinal_position;
SELECT * FROM information_schema.schemata;
```

## Extension Management

> Source: https://duckdb.org/docs/2.0/extensions/overview.html
> Source: https://duckdb.org/docs/2.0/extensions/versioning_of_extensions.html
> Source: https://duckdb.org/docs/2.0/extensions/extension_repositories.html
> Source: https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/securing_extensions.html

```sql
-- 19. Installed / loaded extensions
SELECT extension_name, loaded, installed, extension_version, install_mode, installed_from
FROM duckdb_extensions();

-- 20. Built-in (statically linked) extensions
SELECT extension_name FROM duckdb_extensions() WHERE install_mode = 'STATICALLY_LINKED';

-- 21. Install and load (separately, or in one step -- INSTALL AND LOAD is 2.0 syntax)
INSTALL httpfs;
LOAD httpfs;
INSTALL AND LOAD httpfs;

-- 22. Autoloading: core extensions only. Using a function or URL scheme that needs a core
--     extension installs and loads it on first use.
SELECT * FROM read_parquet('s3://bucket/data.parquet');

-- 23. Community repository
INSTALL h3 FROM community;
LOAD h3;

-- 24. Force reinstall / pin a version
FORCE INSTALL httpfs;
INSTALL httpfs VERSION '<version>';

-- 25. Update all or specific extensions
--     Output columns: extension_name, repository, update_result, previous_version, current_version
UPDATE EXTENSIONS;
UPDATE EXTENSIONS (httpfs, azure);

-- 26. Disable auto-install / auto-load
SET autoinstall_known_extensions = false;
SET autoload_known_extensions = false;

-- 27. Block community extensions (self-locks for the session)
SET allow_community_extensions = false;

-- 28. 2.0: signature fingerprint per extension; custom repositories
SELECT extension_name, signature_key_fingerprint FROM duckdb_extensions() WHERE installed;
SELECT repository_name, prefix, key_fingerprints FROM duckdb_extension_repositories();
```

- `allow_unsigned_extensions` can only be set at startup (CLI `duckdb -unsigned`, or the client's config), not with `SET` on a running database.
- 2.0 custom extension repositories need `SET allow_extension_repositories = 'allowed';` (default `undecided`, not persisted). Extensions from them are never autoloaded, plain `LOAD my_ext;` does not find them (use `LOAD my_ext FROM my_repo;`), and `UPDATE EXTENSIONS` skips them (use `FORCE INSTALL my_ext FROM my_repo;`). The announcement calls the syntax work in progress.
- Extension binaries are tied to a DuckDB version and platform; after upgrading DuckDB run `UPDATE EXTENSIONS;`.

## Configuration and Settings

> Source: https://duckdb.org/docs/2.0/configuration/overview.html
> Source: https://duckdb.org/docs/2.0/configuration/pragmas.html

```sql
-- 29. All settings (2.0: duckdb_settings() accepts debug / deprecated / include_all
--     parameters and adds a typed_value column)
SELECT name, value, description, input_type, scope FROM duckdb_settings();

-- 30. One setting
SELECT current_setting('memory_limit');
SELECT current_setting('threads');
SHOW threads;   -- 2.0

-- 31. Settings matching a pattern
SELECT name, value, description
FROM duckdb_settings()
WHERE name LIKE '%memory%';

-- 32. Memory and spill (memory_limit default 80% of RAM; 2.0 accepts percentages)
SET memory_limit = '8GB';
SET memory_limit = '60%';
SET temp_directory = '/tmp/duckdb_temp';   -- default <database_file>.tmp, or .tmp for in-memory
SET max_temp_directory_size = '50GB';      -- default 90% of available disk

-- 33. Threads (default = CPU cores); 2.0 async I/O pool (default 4x cores, max 256)
SET threads = 8;
SET async_threads = 48;

-- 34. 2.0 per-connection guards
SET max_execution_time = 5000;          -- wall-clock ms, 0 = no limit
SET operator_memory_limit = '256MB';    -- sort buffers / hash tables, default NULL

-- 35. Progress bar
SET enable_progress_bar = true;
PRAGMA enable_progress_bar;
PRAGMA enable_print_progress_bar;

-- 36. Checkpoint threshold (alias wal_autocheckpoint; default 16 MiB of WAL)
SET checkpoint_threshold = '1GB';
SET checkpoint_on_detach = 'ENABLED';   -- 2.0: ENABLED | DISABLED | DEFAULT

-- 37. Insertion order: false lowers memory for large Parquet/CSV loads/exports;
--     results without ORDER BY may then be reordered
SET preserve_insertion_order = false;

-- 38. Remote-file caching. enable_object_cache is deprecated and does nothing in 2.0.
SET enable_external_file_cache = true;  -- default true; shared by all connections
SET parquet_metadata_cache = true;      -- default false

-- 39. Null ordering and collation
SET default_null_order = 'NULLS_LAST';  -- default
SET default_collation = 'nocase';

-- 40. External access (security setting; see Sandboxed Query Execution)
SET enable_external_access = true;
-- enable_fsst_vectors (default false) is a scan optimization, not an access control.

-- 41. Reset
RESET memory_limit;
RESET ALL;
```

## Query Profiling and EXPLAIN

> Source: https://duckdb.org/docs/2.0/dev/profiling.html
> Source: https://duckdb.org/docs/2.0/configuration/pragmas.html

```sql
-- 42. Plan without running
EXPLAIN SELECT region, sum(amount) FROM orders GROUP BY region;

-- 43. Run and show per-operator timings and cardinalities
--     (for remote scans also total requests and bytes transferred)
EXPLAIN ANALYZE SELECT region, sum(amount) FROM orders GROUP BY region;

-- 44. Output formats: text (default), graphviz, html, json, mermaid, web (CLI only, 2.0)
EXPLAIN (FORMAT json) SELECT region, sum(amount) FROM orders GROUP BY region;
EXPLAIN ANALYZE (FORMAT html) SELECT region, sum(amount) FROM orders GROUP BY region;
-- CLI: `.web` renders the previous query's plan in a browser (disabled in safe mode)

-- 45. Which plans EXPLAIN prints
SET explain_output = 'all';            -- physical_only (default) | optimized_only | all

-- 46. Profiling to a file (formats: query_tree (default), json, query_tree_optimizer, no_output)
SET enable_profiling = 'json';
SET profiling_output = '/tmp/query_profile.json';   -- overwritten for every query
SELECT region, sum(amount) FROM orders GROUP BY region;
PRAGMA disable_profiling;

-- 47. Function form (since 1.5.0)
CALL enable_profiling(format := 'json', save_location := '/tmp/profile.json',
                      coverage := 'select',
                      metrics := ['query.total_time', 'operator.timing']);
SELECT region, sum(amount) FROM orders GROUP BY region;
CALL disable_profiling();

-- 48. 2.0: choose metrics with tracked_metrics (glob patterns; json and no_output formats only)
SET tracked_metrics = ['query.*', 'optimizer.*'];
SELECT metric_name, metric_type, unit FROM duckdb_available_metrics();

-- 49. Profile all statements, not only SELECT
SET profiling_coverage = 'ALL';
```

- `profiling_mode` is deprecated in 2.0 and has no effect: detailed planner/optimizer metrics are always collected. `custom_profiling_settings` is removed; use `tracked_metrics`.
- Render a JSON profile as an HTML query graph: `python -m duckdb.query_graph /tmp/profile.json` (needs the duckdb Python package).
- Hash joins: the probe side is the left operand, the build side the right.
- Operator names in plans (e.g. scan, hash join, hash group-by) are not enumerated by the docs and vary by version; read them from your own `EXPLAIN` output rather than matching fixed strings.

## Logging

> Source: https://duckdb.org/docs/2.0/operations_manual/logging/overview.html
> Source: https://duckdb.org/docs/2.0/operations_manual/migration

```sql
-- 50. Enable logging (levels: FATAL, ERROR, WARNING, INFO (default), DEBUG, TRACE)
CALL enable_logging(level = 'debug');

-- 51. Specific log types: QueryLog, FileSystem, HTTP, PhysicalOperator, Metrics
CALL enable_logging('HTTP');
CALL enable_logging(['HTTP', 'QueryLog']);

-- 52. Query logs
SELECT timestamp, message FROM duckdb_logs WHERE log_level = 'WARNING';
SELECT request.url, request.duration_ms, response.status FROM duckdb_logs_parsed('HTTP');
DESCRIBE FROM duckdb_logs_parsed('HTTP');
SELECT * FROM duckdb_log_contexts();

-- 53. Persist to CSV (path ending .csv = denormalized; a directory = normalized files)
CALL enable_logging(storage = 'file', storage_config = {'path': 'path/to/logs.csv'});

-- 54. Unbuffered (when debugging crashes, buffered messages can be lost)
CALL enable_logging(storage = 'memory', storage_buffer_size = 0);

-- 55. Housekeeping
CALL truncate_duckdb_logs();
CALL disable_logging();
SET log_query_path = '/tmp/duckdb_log/';   -- '' disables
```

- CLI: since 1.5.0 the CLI logs to `shell_log_storage` (prints warnings, not queryable). To query `duckdb_logs` in the CLI run `CALL enable_logging(storage = 'memory');`; restore console output with `CALL enable_logging(storage = 'shell_log_storage');`. Other clients default to `memory`.
- 2.0 removed `enable_http_logging` and `http_logging_output`; use `CALL enable_logging('HTTP')` plus `duckdb_logs_parsed('HTTP')`. `redact_http_logs` defaults to true.
- Deprecated syntax and settings are logged at WARNING. Logs may contain secrets or credentials; treat log files as sensitive.

## Memory Diagnostics

> Source: https://duckdb.org/docs/2.0/sql/meta/duckdb_table_functions.html
> Source: https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html
> Source: https://duckdb.org/docs/2.0/guides/performance/indexing.html

```sql
-- 56. Buffer-manager memory by tag (in memory and in temporary storage)
SELECT tag, memory_usage_bytes, temporary_storage_bytes FROM duckdb_memory();

-- 57. Limits in effect
SELECT current_setting('memory_limit') AS memory_limit,
       current_setting('temp_directory') AS temp_directory,
       current_setting('max_temp_directory_size') AS max_temp;

-- 58. Temporary (spill) files currently on disk
SELECT path, size FROM duckdb_temporary_files();
-- Run your query, then check: rows here mean it spilled to disk

-- 59. Table size estimates
SELECT table_name, estimated_size, column_count, index_count
FROM duckdb_tables();

-- 60. Per-column storage breakdown
SELECT column_name, column_id, segment_type, compression, count, stats
FROM pragma_storage_info('orders');

-- 61. Aggregate storage by compression type
SELECT compression, count(*) AS segment_count, sum(count) AS total_rows
FROM pragma_storage_info('orders')
GROUP BY compression;

-- 62. Remote file cache contents
FROM duckdb_external_file_cache();
```

- `memory_limit` bounds the buffer manager only; process RSS can be higher.
- ART indexes are NOT buffer-managed in 2.0.0: index memory is registered with the buffer manager but never evicted, so indexes can occupy a large share of memory. Mitigate with `DETACH` + `ATTACH` (index memory is deserialized lazily). An ART index must fit in memory when it is created.
- Blocking operators that can spill: GROUP BY, JOIN, ORDER BY, window functions. Queries with several blocking operators can still run out of memory; `string_agg()` cannot spill.

## File Scanning and Format Diagnostics

> Source: https://duckdb.org/docs/2.0/data/parquet/overview.html
> Source: https://duckdb.org/docs/2.0/data/csv/overview.html

### Parquet File Inspection

```sql
-- 63. File metadata (row groups, column chunks, statistics, sizes)
SELECT * FROM parquet_metadata('data.parquet');
SELECT * FROM parquet_file_metadata('data.parquet');

-- 64. Schema and key-value metadata
SELECT * FROM parquet_schema('data.parquet');
SELECT * FROM parquet_kv_metadata('data.parquet');

-- 65. Read with options (hive_partitioning is auto-detected by default;
--     filename is an automatic virtual column since 1.3.0)
SELECT * FROM read_parquet('data.parquet',
    binary_as_string = true,
    file_row_number = true,
    hive_partitioning = true
);

-- 66. 2.0 read options
SELECT * FROM read_parquet('data/*.parquet', allow_empty = true);       -- no match: empty result, not an error
SELECT * FROM read_parquet('legacy.parquet', int96_as = 'timestamp_ns'); -- timestamp | timestamp_ns | struct
SELECT * FROM read_parquet('dirty.parquet', utf8_validation = 'replace'); -- strict (default) | replace | ignore
SELECT * FROM read_parquet('data.parquet', prefetch_strategy = 'whole_group'); -- auto (default) | whole_group
SELECT * FROM read_parquet('data/*.parquet', hive_partitioning = false,
    bound_schema = {'a': 'BIGINT', 'b': 'VARCHAR'});                     -- fixed ordered output schema

-- 67. 2.0 virtual column: row group index within each file (0-based)
SELECT filename, file_row_group_number, count(*)
FROM read_parquet('data/*.parquet')
GROUP BY ALL;

-- 68. Row group statistics for one column
SELECT * FROM parquet_metadata('data.parquet')
WHERE path_in_schema = 'amount';

-- 69. Globs and heterogeneous schemas
SELECT * FROM read_parquet('data/year=*/month=*/*.parquet', hive_partitioning = true);
SELECT * FROM read_parquet('data/*.parquet', union_by_name = true);
```

### CSV File Inspection

```sql
-- 70. Auto-detect (sniffer: auto_detect true, sample_size 20480, files_to_sniff 10)
SELECT * FROM read_csv('data.csv');

-- 71. Explicit options
SELECT * FROM read_csv('data.csv',
    header = true,
    delim = '|',
    quote = '"',
    escape = '\\',
    dateformat = '%Y-%m-%d',
    ignore_errors = true,
    max_line_size = 2000000      -- default
);

-- 72. Inspect the sniffer's result (sniff_csv is not on the 2.0 CSV overview page; verify on your version)
SELECT * FROM sniff_csv('data.csv');

-- 73. Explicit column types (disables schema detection)
SELECT * FROM read_csv('data.csv',
    columns = {'id': 'INTEGER', 'name': 'VARCHAR', 'amount': 'DOUBLE'}
);

-- 74. Keep rejected rows for inspection (tables reject_errors / reject_scans)
SELECT * FROM read_csv('data.csv', store_rejects = true);
FROM reject_errors;

-- 75. 2.0 options
SELECT * FROM read_csv('data/*.csv', allow_empty = true);             -- no match: empty result
SELECT * FROM read_csv('data.csv', store_rejects = true,
                       rejects_line_size_limit = 0);                  -- 0 = do not truncate stored lines

-- 76. Filename column, custom null string
SELECT *, filename FROM read_csv('data/*.csv');
SELECT * FROM read_csv('data.csv', nullstr = 'NA');
```

Non-UTF-8 CSV: use the `encodings` extension (1,000+ encodings) or convert first.

### JSON File Inspection

```sql
-- 77. Auto-detection
SELECT * FROM read_json_auto('data.json');

-- 78. Newline-delimited JSON
SELECT * FROM read_json_auto('data.ndjson', format = 'newline_delimited');

-- 79. Explicit schema
SELECT * FROM read_json('data.json',
    columns = {'id': 'INTEGER', 'name': 'VARCHAR', 'tags': 'VARCHAR[]'},
    format = 'array'
);
```

JSON reading stays synchronous in 2.0 (no async I/O); for remote JSON, raise `threads` to roughly 2-5x the core count.

### Remote File Access

> Source: https://duckdb.org/docs/2.0/core_extensions/httpfs/s3api.html
> Source: https://duckdb.org/docs/2.0/core_extensions/azure.html
> Source: https://duckdb.org/docs/2.0/configuration/secrets_manager.html

```sql
-- 80. S3: use secrets (legacy SET s3_* settings are deprecated)
CREATE SECRET my_s3 (TYPE s3, KEY_ID '...', SECRET '...', REGION 'us-east-1');
-- or the AWS SDK credential chain (aws extension)
CREATE SECRET (TYPE s3, PROVIDER credential_chain);
-- Scope a secret to a prefix; the longest matching SCOPE wins
CREATE SECRET bucket_a (TYPE s3, PROVIDER credential_chain, SCOPE 's3://bucket-a');

-- 81. Which secret applies to a path
FROM which_secret('s3://bucket-a/file.parquet', 's3');
FROM duckdb_secrets();   -- redacted by default

-- 82. 2.0: connection-scoped temporary secret
CREATE SECRET my_conn_secret IN connection (TYPE s3, PROVIDER credential_chain);

-- 83. List objects
SELECT * FROM glob('s3://bucket/path/*');

-- 84. GCS: GCS secret with HMAC keys, gs:// or gcs:// URLs
CREATE SECRET (TYPE gcs, KEY_ID 'HMAC_KEY_ID', SECRET 'HMAC_SECRET');
SELECT * FROM read_parquet('gs://bucket/data.parquet');

-- 85. Azure: secrets preferred (azure_* connection-string variables are deprecated)
CREATE SECRET (TYPE azure, PROVIDER credential_chain, ACCOUNT_NAME 'myaccount');
SELECT * FROM read_parquet('az://container/path/data.parquet');      -- Blob: az:// or azure://
SELECT * FROM read_parquet('abfss://container/path/data.parquet');   -- ADLS Gen2: abfss:// or abfs://

-- 86. HTTPS
SELECT * FROM read_parquet('https://example.com/data.parquet');
```

- 2.0 disables S3 settings in URL query strings: `?s3_access_key_id=...` now becomes part of the object key. Use secrets; the legacy opt-in (after `LOAD httpfs`) is `SET s3_enable_deprecated_url_parameters = true;`.
- Persistent secrets (`CREATE PERSISTENT SECRET`) are stored unencrypted on disk (mode 600) under `secret_directory` (default `~/.duckdb/stored_secrets`).

## Performance Diagnostics

> Source: https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html
> Source: https://duckdb.org/docs/2.0/guides/performance/indexing.html
> Source: https://duckdb.org/docs/2.0/dev/profiling.html

### Query Performance Analysis

```sql
-- Time a query (CLI)
.timer on

-- Per-operator timing and cardinalities; look for the dominant operator and for
-- estimate-vs-actual cardinality gaps
EXPLAIN ANALYZE
SELECT o.region, c.name, sum(o.amount)
FROM orders o JOIN customers c ON o.customer_id = c.id
WHERE o.order_date > '2025-01-01'
GROUP BY ALL ORDER BY 3 DESC LIMIT 10;

-- Zonemap pruning works best on data ordered by the filter column
EXPLAIN ANALYZE SELECT * FROM orders WHERE order_date BETWEEN '2025-01-01' AND '2025-01-31';

-- Projection pushdown (fewer columns read) and filter pushdown into the Parquet reader
EXPLAIN ANALYZE SELECT id, amount FROM orders;
EXPLAIN ANALYZE SELECT * FROM read_parquet('orders.parquet') WHERE order_date > '2025-01-01';

-- Did the query spill?
SELECT * FROM duckdb_temporary_files();
```

- Parallelism starts at row-group level: a query on k threads needs at least k x 122,880 rows (default row group size) to use them all.
- Prefer hash joins over nested loop joins; push filters down; avoid exploding intermediate cardinalities. If a join over Parquet files gets a bad order, load the data into DuckDB tables for better statistics.
- ART indexes help only point lookups, `IN (...)` lists and very selective filters (single column, no expression); they do not speed up joins, aggregations or sorts.
- Remote Parquet, uncompressed seekable UTF-8 CSV and native DuckDB files use async I/O in 2.0. If reads do not saturate bandwidth, tune `async_threads` and `read_ahead_depth` (default -1 = unlimited, bounded by memory; 0 = off). Async Parquet reads work best with at least as many row groups as threads.

## CLI Commands

> Source: https://duckdb.org/docs/2.0/clients/cli/dot_commands.html
> Source: https://duckdb.org/docs/2.0/clients/cli/overview.html
> Source: https://duckdb.org/docs/2.0/clients/cli/arguments.html
> Source: https://duckdb.org/docs/2.0/clients/cli/agent_mode.html
> Source: https://duckdb.org/2026/10/26/gems-of-duckdb-200.html

```sql
-- 87. Help, databases, tables
.help
.databases
.tables

-- 88. Timer
.timer on

-- 89. Output format: markdown, csv, json, jsonlines, line, box, table, duckbox, latex, insert, ...
.mode markdown
.mode trash   -- discard output (benchmarking)

-- 90. Headers, output redirection
.headers on
.output results.csv
SELECT * FROM orders;
.output   -- back to stdout

-- 91. Run a script; import a file (--csv, --json, --parquet)
.read my_script.sql
.import data.csv orders

-- 92. Open another database; read-only
.open my_database.duckdb
.open --readonly my_database.duckdb

-- 93. 2.0 additions
.manual list_%            -- function signatures/examples (LIKE wildcards); CLI: duckdb -manual <name>
.history 10               -- recent commands
.schema                   -- pretty-printed by default in 2.0
.schema --no-indent       -- old single-line form (alias --no-format)
.safe_mode                -- block access to external files other than the database
.web                      -- render the previous query's plan in a browser

-- 94. Search command history as a table (2.0)
SELECT sql FROM shell_history() WHERE sql ILIKE '%copy%';

-- 95. Quit
.quit
```

Useful flags: `-readonly`, `-c "<SQL>"`, `-init <file>`, `-csv`, `-json`, `-markdown`, `-safe`, `-unsigned`, `-storage-version <v>`, `-ui`; 2.0 adds `-serve` (start a Quack server), `-connect` (connect to one), `-agent` / `-no-agent`.

Agent mode (2.0) turns on automatically when a known agent environment variable is set (e.g. `AI_AGENT`, `CLAUDECODE`), stdout is not a terminal and no output-format flag is given. It prints compact Markdown tables (whole result up to 1,000 rows / 10,000 bytes, else first and last rows plus a count), errors as JSON on stderr, and a planner estimate for statements expected to read 1M+ rows. Override with `-agent`/`-no-agent` or `DUCKDB_AGENT_MODE=1|0`; tune with `.maxrows`, `.maxbytes`, `.maxcellwidth`; `.help agent` lists the rules.

## Data Integrity Checks

> Source: https://duckdb.org/docs/2.0/sql/meta/duckdb_table_functions.html

```sql
-- 96. Constraints on a table
SELECT * FROM duckdb_constraints()
WHERE table_name = 'orders';

-- 97. Duplicate rows
SELECT *, count(*) AS cnt
FROM orders
GROUP BY ALL
HAVING cnt > 1;

-- 98. Orphaned foreign key references
SELECT o.*
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.id
WHERE c.id IS NULL;

-- 99. 2.0: a CTAS from an untyped NULL creates a column of type "NULL" that rejects later
--      non-NULL inserts (documented). Recreate such columns with an explicit type.
--      Untested suggestion, NOT a documented example -- verify the data_type value against your own catalog:
SELECT table_name, column_name FROM duckdb_columns() WHERE data_type = 'NULL';
```

## Backup and Export Diagnostics

> Source: https://duckdb.org/docs/2.0/internals/storage.html
> Source: https://duckdb.org/docs/2.0/operations_manual/migration

```sql
-- 100. Export / import a whole database
EXPORT DATABASE 'backup' (FORMAT PARQUET);
EXPORT DATABASE 'backup_csv' (FORMAT CSV, HEADER true);
IMPORT DATABASE 'backup';

-- 101. Single table to Parquet (default compression is Snappy; ZSTD is a valid choice)
COPY orders TO 'orders_backup.parquet' (FORMAT PARQUET, COMPRESSION ZSTD);
COPY orders TO 'orders.parquet' (FORMAT PARQUET, ROW_GROUP_SIZE 122880);

-- 102. Cross-database copy
ATTACH 'backup.duckdb' AS backup_db;
COPY FROM DATABASE memory TO backup_db;

-- 103. 2.0: write a copy that DuckDB 1.x can still open (needs a writer >= 1.2.0)
ATTACH 'file1.db';
ATTACH 'compat.db' (STORAGE_VERSION 'v1.0.0');
COPY FROM DATABASE file1 TO compat;
```

- A database file created by 2.0 is unreadable by 1.x. Before handing a file to a 1.x process, create it with `-storage-version v1.5.6` (CLI), `SET storage_compatibility_version = 'v1.5.0'`, or ATTACH `STORAGE_VERSION`. Files created by older versions keep their storage version when 2.0 writes to them.
- Convert an old file to the 2.0 format: old binary `EXPORT DATABASE 'tmp'`, then 2.0 binary `IMPORT DATABASE 'tmp'`.

## Troubleshooting Common Issues

> Source: https://duckdb.org/docs/2.0/configuration/pragmas.html
> Source: https://duckdb.org/docs/2.0/sql/statements/checkpoint.html
> Source: https://duckdb.org/docs/2.0/connect/concurrency.html
> Source: https://duckdb.org/docs/2.0/operations_manual/migration
> Source: https://duckdb.org/docs/2.0/guides/performance/environment.html

### Out of Memory

Check `duckdb_memory()` and `duckdb_temporary_files()` (see Memory Diagnostics), then in order: point `temp_directory` at a disk with space; reduce `threads` (aim for 1-4 GB of memory per thread, ~125 MB minimum); `SET preserve_insertion_order = false` for large Parquet/CSV loads or exports; raise `memory_limit`. If ART indexes hold memory (not evicted in 2.0.0), `DETACH` and re-`ATTACH` the database to reload them lazily.

### Slow Queries

```sql
-- 104. Profile the query
EXPLAIN ANALYZE <your_query>;

-- 105. Inspect min/max stats for a column's segments (ordered data prunes better)
SELECT column_name, stats
FROM pragma_storage_info('orders')
WHERE column_name = 'order_date';

-- 106. ART index for point lookups or very selective filters (single column, no expression)
CREATE INDEX idx_order_id ON orders(order_id);

-- 107. Compare against the unoptimized plan
PRAGMA disable_optimizer;
EXPLAIN ANALYZE <your_query>;
PRAGMA enable_optimizer;

-- 108. Stop runaway queries (2.0)
SET max_execution_time = 60000;
```

### Extension and File Access Issues

```sql
-- Installed, loaded, from where?
SELECT extension_name, loaded, installed, extension_version, installed_from
FROM duckdb_extensions() WHERE extension_name = 'httpfs';
FORCE INSTALL httpfs; LOAD httpfs;

-- S3 connectivity with HTTP request logging
CREATE SECRET (TYPE s3, PROVIDER credential_chain);
CALL enable_logging('HTTP');
SELECT * FROM glob('s3://bucket/path/*');
SELECT request.url, response.status FROM duckdb_logs_parsed('HTTP');
```

If `LOAD` fails after a DuckDB upgrade, the binary was built for another version: `UPDATE EXTENSIONS;` or reinstall. A custom-repository extension needs `LOAD name FROM repo`.

### Concurrency Issues

```sql
-- 109. Database locked by another process
-- Only one process can open a file read-write; a second open fails with a lock error.
-- Check for other DuckDB processes on the same file. To share reads, every process
-- must open read-only:
--   CLI:    duckdb -readonly my_database.duckdb
--   Python: duckdb.connect('my_database.duckdb', read_only=True)
--   SQL:    ATTACH 'my_database.duckdb' (READ_ONLY);

-- 110. Same-row conflict between transactions:
--   Transaction conflict: cannot update a table that has been altered!
-- Rerun the transaction. Appends never conflict.

-- 111. Checkpoint behavior
CHECKPOINT;          -- fails if transactions are running
FORCE CHECKPOINT;    -- waits for the checkpoint lock, blocks new transactions
PRAGMA force_checkpoint;   -- makes CHECKPOINT run even when nothing changed (not garbage collection)
```

Multi-process writes to the native format are not supported in-process: use the Quack remote protocol or DuckLake with a PostgreSQL catalog. Avoid read-write use of the native format on NFS/SMB.

### Errors After Upgrading to 2.0

| Symptom | Cause | Fix / revert |
|---|---|---|
| "transaction is aborted" after any failed statement | 2.0: any error in an explicit transaction aborts it | `ROLLBACK;` or `SET default_transaction_invalidation_policy = 'SYNTACTIC_ERRORS_DO_NOT_INVALIDATE';` |
| `x -> x + 1` lambda fails | single-arrow lambdas disabled by default | `lambda x : x + 1`; temporary `SET lambda_syntax = 'enable_single_arrow';` (removed in 2.1) |
| `1 // 0` or `1 % 0` raises an error | integer division/modulo by zero now errors | `TRY(1 // 0)`; `SET error_on_division_by_zero = false;` (`1 / 0` still returns `inf`) |
| `'abc' ~ 'b'` now true; `2 * 3!` = 12 | PEG parser default: partial regex match, tighter factorial | `SET regex_match_operator_semantics = 'full';` / `(2 * 3)!` |
| Query that parsed on 1.x is a syntax error | PEG parser | Compare with `INSTALL AND LOAD legacy_parser; SET enable_legacy_parser = true;` and report a regression |
| Insert into CTAS column fails | untyped NULL column has type "NULL" | `NULL::VARCHAR AS x`; `SET legacy_disable_null_type = true;` |
| MERGE fails "cannot affect the same target row more than once" | multiple source rows match one target row | deduplicate the source or make the ON condition unique |
| S3 credentials in URL ignored | URL parameters disabled | use secrets; `SET s3_enable_deprecated_url_parameters = true;` |

Check whether a statement parses without running it: `SELECT json_serialize_sql('SELEC 42')::JSON->>'error' AS parse_error;` (returns true on a parse error).

## Advanced Diagnostics

> Source: https://duckdb.org/docs/2.0/data/parquet/overview.html
> Source: https://duckdb.org/docs/2.0/configuration/pragmas.html

### Sampling and Approximation

```sql
-- 112. Sample rows
SELECT * FROM orders USING SAMPLE 1000;
SELECT * FROM orders USING SAMPLE 10%;
SELECT * FROM orders TABLESAMPLE reservoir(1000);

-- 113. Approximate distinct count and quantiles
SELECT approx_count_distinct(customer_id) FROM orders;
SELECT approx_quantile(amount, 0.5) AS median,
       approx_quantile(amount, 0.95) AS p95,
       approx_quantile(amount, 0.99) AS p99
FROM orders;
```

### Metadata about Parquet Files

```sql
-- 114. Column chunk statistics
SELECT path_in_schema, type, num_values,
       stats_min, stats_max, stats_null_count,
       compression, total_compressed_size, total_uncompressed_size
FROM parquet_metadata('data.parquet');

-- 115. Compression ratio
SELECT
    sum(total_compressed_size) AS compressed_bytes,
    sum(total_uncompressed_size) AS uncompressed_bytes,
    round(100.0 * sum(total_compressed_size) / sum(total_uncompressed_size), 1) AS compression_pct
FROM parquet_metadata('data.parquet');

-- 116. Row groups per file (want 100K-1M rows each, and at least as many row groups as threads)
SELECT filename, max(file_row_group_number) + 1 AS row_groups, count(*) AS rows
FROM read_parquet('data/*.parquet')
GROUP BY filename;
```

### System Resource Monitoring

```sql
-- Performance-related settings at a glance
SELECT name, value FROM duckdb_settings()
WHERE name IN ('threads', 'async_threads', 'memory_limit', 'temp_directory',
               'max_temp_directory_size', 'preserve_insertion_order',
               'checkpoint_threshold', 'read_ahead_depth');

-- Force or disable compression methods (debugging)
SET force_compression = 'bitpacking';
SET disabled_compression_methods = 'fsst,rle';
```

### Data Quality Profiling

```sql
-- 117. Profile all columns of a table or query
SUMMARIZE orders;
SUMMARIZE SELECT * FROM read_parquet('data.parquet');

-- 118. Selected SUMMARIZE columns
SELECT column_name, count, null_percentage, approx_unique, min, max, avg
FROM (SUMMARIZE orders);
```

### Comparing Data Across Sources

```sql
-- 119. Compare two Parquet files
SELECT * FROM read_parquet('v1.parquet')
EXCEPT
SELECT * FROM read_parquet('v2.parquet');

-- 120. Schema diff between two tables
SELECT a.column_name, a.data_type AS type_a, b.data_type AS type_b
FROM (SELECT * FROM duckdb_columns() WHERE table_name = 'orders_v1') a
FULL OUTER JOIN (SELECT * FROM duckdb_columns() WHERE table_name = 'orders_v2') b
ON a.column_name = b.column_name
WHERE a.data_type IS DISTINCT FROM b.data_type
   OR a.column_name IS NULL
   OR b.column_name IS NULL;
```

## Other File Formats

> Source: https://duckdb.org/docs/2.0/core_extensions/overview.html
> Source: https://duckdb.org/docs/2.0/core_extensions/avro.html
> Source: https://duckdb.org/docs/2.0/core_extensions/sqlite.html
> Source: https://duckdb.org/docs/2.0/core_extensions/excel.html

For a universal reader that dispatches by file extension, see `references/file-reading.md` (the `read_any` macro).

```sql
-- 121. Avro: the avro core extension (not built into the engine)
SELECT * FROM read_avro('data.avro') LIMIT 10;
DESCRIBE FROM read_avro('data.avro');

-- 122. Spatial files via the spatial extension
INSTALL spatial; LOAD spatial;
SELECT * FROM st_read('boundaries.gpkg') LIMIT 10;
SELECT * FROM st_read('data.shp') LIMIT 10;

-- 123. SQLite: extension name is sqlite (aliases sqlite_scanner, sqlite3); attach the file
INSTALL AND LOAD sqlite;
ATTACH 'legacy.db' AS legacy (TYPE sqlite);
SHOW ALL TABLES;
SELECT * FROM legacy.users LIMIT 10;

-- 124. Excel: .xlsx only -- .xls is NOT supported
SELECT * FROM read_xlsx('report.xlsx', sheet = 'Sheet1');
```

## SQL Variables and Session State

> Source: https://duckdb.org/docs/2.0/sql/statements/set_variable.html
> Source: https://github.com/duckdb/duckdb-skills

```sql
-- 125. SQL-level variables
SET VARIABLE my_threshold = 100;
SET VARIABLE my_region = 'US';
SELECT * FROM orders
WHERE amount > getvariable('my_threshold')
  AND region = getvariable('my_region');

-- 126. 2.0: $name shorthand (errors if unset; getvariable returns NULL instead)
SELECT * FROM orders WHERE amount > $my_threshold AND region = $my_region;
SELECT * FROM duckdb_variables();

-- 127. Session state file pattern (duckdb-skills plugin)
-- A state.sql file persists ATTACH, USE, LOAD, secrets and macros across sessions:
--   ATTACH IF NOT EXISTS '/path/to/analytics.duckdb' AS analytics;
--   USE analytics;
--   LOAD httpfs;
-- Restore via: duckdb -init state.sql -c "SHOW TABLES;"
```

## Sandboxed Query Execution

> Source: https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/overview.html

Settings are defense in depth only. For untrusted SQL, isolate first (duckdb-wasm, a restricted container, VM or low-privilege process, network isolation, query timeouts), and never run DuckDB as root.

```sql
-- 128. Lock down to one S3 prefix. ORDER MATTERS and each step is irreversible for the session.
LOAD httpfs;                                    -- load needed extensions first
SELECT count(*) FROM duckdb_secrets();          -- initialize the secrets manager before lockdown
SET allowed_directories = ['s3://bucket/prefix/'];  -- allow-listed paths are readable AND writable
SET enable_external_access = false;             -- allow-lists cannot change after this
SET disabled_filesystems = 'LocalFileSystem';   -- also blocks all INSTALL/LOAD
SET threads = 4; SET memory_limit = '4GB'; SET max_temp_directory_size = '4GB';
SET allowed_configs = ['memory_limit', 'threads'];  -- optional: keep these adjustable
SET lock_configuration = true;

-- 129. Local-file variant
SET allowed_paths = ['data.parquet', '/path/to/other_file.csv'];
SET enable_external_access = false;
SET allow_persistent_secrets = false;
SET lock_configuration = true;
SELECT * FROM 'data.parquet' WHERE amount > 100;
```

- With `enable_external_access = false`, ATTACH cannot open database files, COPY cannot read/write files, and file-reading functions cannot reach external sources; blocked paths raise "Permission Error".
- 2.0: set `allowed_paths`/`allowed_directories` URL entries only after loading the scheme's extension (before 2.0.0 an `s3://` entry without httpfs was silently stored as a local path).
- httpfs reads its CA bundle from the local file system; after lockdown point `ca_cert_file` at a certificate or allow-list the bundle path.
- Security settings self-lock; resource settings do not, hence `lock_configuration`. `allow_unredacted_secrets` can only be set at startup.
- CLI equivalent for quick use: `duckdb -safe` or `.safe_mode`.

## Sources

- https://duckdb.org/docs/2.0/configuration/pragmas.html
- https://duckdb.org/docs/2.0/configuration/overview.html
- https://duckdb.org/docs/2.0/configuration/secrets_manager.html
- https://duckdb.org/docs/2.0/dev/profiling.html
- https://duckdb.org/docs/2.0/operations_manual/logging/overview.html
- https://duckdb.org/docs/2.0/operations_manual/migration
- https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/overview.html
- https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/securing_extensions.html
- https://duckdb.org/docs/2.0/sql/meta/duckdb_table_functions.html
- https://duckdb.org/docs/2.0/sql/statements/checkpoint.html
- https://duckdb.org/docs/2.0/sql/statements/set_variable.html
- https://duckdb.org/docs/2.0/internals/storage.html
- https://duckdb.org/docs/2.0/connect/concurrency.html
- https://duckdb.org/docs/2.0/guides/performance/how_to_tune_workloads.html
- https://duckdb.org/docs/2.0/guides/performance/indexing.html
- https://duckdb.org/docs/2.0/guides/performance/environment.html
- https://duckdb.org/docs/2.0/clients/cli/overview.html
- https://duckdb.org/docs/2.0/clients/cli/dot_commands.html
- https://duckdb.org/docs/2.0/clients/cli/arguments.html
- https://duckdb.org/docs/2.0/clients/cli/agent_mode.html
- https://duckdb.org/docs/2.0/data/parquet/overview.html
- https://duckdb.org/docs/2.0/data/csv/overview.html
- https://duckdb.org/docs/2.0/core_extensions/overview.html
- https://duckdb.org/docs/2.0/core_extensions/avro.html
- https://duckdb.org/docs/2.0/core_extensions/sqlite.html
- https://duckdb.org/docs/2.0/core_extensions/excel.html
- https://duckdb.org/docs/2.0/core_extensions/httpfs/s3api.html
- https://duckdb.org/docs/2.0/core_extensions/azure.html
- https://duckdb.org/docs/2.0/extensions/overview.html
- https://duckdb.org/docs/2.0/extensions/versioning_of_extensions.html
- https://duckdb.org/docs/2.0/extensions/extension_repositories.html
- https://duckdb.org/2026/10/26/gems-of-duckdb-200.html
- https://github.com/duckdb/duckdb-skills

Fetched: 2026-11-13
