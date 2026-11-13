# DuckDB Language Integrations Reference

Python, WASM (browser/Node.js), R, and other client notes for DuckDB 2.0. All primary clients (C, CLI,
Java, Go, Node.js node-neo, ODBC, Python, R, Rust, WebAssembly) ship 2.0.0; the C# (.NET) client was
still on 1.5.6 at fetch time. Only the Python and Go clients have official 2.0 migration notes -- for
other clients, test before upgrading rather than assuming compatibility.

> Source: https://duckdb.org/docs/2.0/clients/overview.html

---

## Python Integration

> Source: https://duckdb.org/docs/2.0/clients/python/overview.html
> Source: https://duckdb.org/docs/2.0/clients/python/migration
> Source: https://github.com/duckdb/duckdb-python/releases/tag/v2.0.0

**2.0 baseline:** Python 3.11+ only; free-threaded CPython builds are unsupported. On Python 3.10,
`pip install duckdb` silently installs a 1.x release.

```python
import duckdb

# In-memory connection (default)
con = duckdb.connect()

# Persistent database
con = duckdb.connect('my_database.duckdb')

# Configuration at connection time (database, read_only, config)
con = duckdb.connect(config={'threads': 4, 'memory_limit': '8GB'})

# Keep a 2.0-written file openable by DuckDB 1.5
con = duckdb.connect('shared.duckdb', config={'storage_compatibility_version': 'v1.5.0'})

# Query files directly; duckdb.sql() runs on a global in-memory database
df = duckdb.sql("SELECT * FROM 'data.parquet' WHERE amount > 100").df()

# Query Pandas / Polars DataFrames and Arrow tables by variable name (read-only sources)
import pandas as pd
orders_df = pd.DataFrame({'id': [1, 2, 3], 'value': [10, 20, 30]})
result = con.sql("SELECT * FROM orders_df WHERE value > 15").df()

# Result conversion
rel = con.sql("SELECT * FROM orders")
rel.df(); rel.pl(); rel.fetchall(); rel.fetchnumpy()
rel.to_arrow_table()          # replaces .arrow() / fetch_arrow_table()
rel.to_arrow_reader()         # replaces fetch_record_batch(); batches of 131,072 rows by default

# Use execute() for DDL/DML; con.sql("CREATE TABLE ...") now returns a relation
con.execute("CREATE TABLE t (id INTEGER, name VARCHAR)")

# Prepared statements -- read the result before running another query
con.execute("SELECT * FROM orders WHERE region = ? AND amount > ?", ['US', 100])
rows = con.fetchall()

# Appender (new in duckdb-python 2.0.0): flushes when the with-block exits
with con.appender("t") as appender:
    appender.append_row(1, "a")
    appender.append_rows([(2, "b"), (3, "c")])
```

**2.0 breaking changes -- fix these on upgrade:**

- `execute()` results lost `fetch_arrow_table()`, `fetch_record_batch()`, `arrow()`, `pl()`. Use
  `con.sql(q).to_arrow_table()` / `.to_arrow_reader()` / `.pl()`.
- Relations lost `fetchone()`, `fetchmany(n)`, `execute()`, `fetch_df_chunk()`: a relation keeps no
  result and reruns its query on every read (printing one reruns it too). Use `con.execute(q)` for row
  loops, `rel.iter_rows()`, `rel.to_arrow_reader()`, or `rel.materialize()`.
- An open `execute()` result blocks other queries on that connection with `ResourceInUseException`
  until it is read to the end or closed with `con.complete()` / `con.abort()`. Sharing one connection
  across threads also raises it -- give each thread `con.cursor()`.
- A failed `execute()` aborts the transaction (`TransactionException` until `con.rollback()`).
- In expressions, bare strings are values: use `col("x")` for columns, `lit("x")` for literals;
  `ColumnExpression("t.x")` is one column name (use `col("t", "x")`).
- New relation methods (`offset`, `sample`, `head`, `rename`, `pivot`, `drop`, `unnest`, `unpivot`,
  `preview`, `group_by`) shadow same-named columns -- use `rel["offset"]`.
- Dicts with non-string keys become MAP, not STRUCT. `Decimal("1E+2")` maps to `DECIMAL(3,0)`.
- `write_csv` / `write_parquet` with `overwrite=False` raise `IOException` if the file exists.
- `import duckdb` no longer opens the default database until first use.

## WASM Deployment

> Source: https://duckdb.org/docs/2.0/clients/wasm/overview.html
> Source: https://duckdb.org/2026/09/18/opfs-wasm.html

DuckDB compiles to WebAssembly (`npm install @duckdb/duckdb-wasm`). The docs' pattern selects a bundle
from jsDelivr and starts a same-origin worker:

```javascript
import * as duckdb from '@duckdb/duckdb-wasm';

const bundle = await duckdb.selectBundle(duckdb.getJsDelivrBundles());
// Worker scripts must be same-origin: your helper wraps the bundle's CDN worker script in a
// Blob URL and returns new Worker(blobUrl) -- see the WASM instantiation docs for the exact code.
const worker = makeSameOriginWorker(bundle);   // hypothetical helper, not a DuckDB API -- not documented code
const db = new duckdb.AsyncDuckDB(new duckdb.ConsoleLogger(), worker);
await db.instantiate(bundle.mainModule, bundle.pthreadWorker);

const conn = await db.connect();
const result = await conn.query("SELECT 42 AS answer");
console.log(result.toArray());
await conn.close();
```

**Constraints:** single-threaded by default (multithreading is experimental); 4 GB WebAssembly memory
cap; reading remote Parquet through the built-in httpfs path may download the whole file (duckdb-wasm
issue #2153). `@duckdb/duckdb-wasm@next` tracks `main` -- testing only. The securing guide recommends
duckdb-wasm as a sandbox for untrusted SQL.

**Persistence (OPFS, pre-2.0 post):** `await db.open({ path: 'opfs://analytics.duckdb', accessMode:
duckdb.DuckDBAccessMode.READ_WRITE });` survives reloads; run `CHECKPOINT` after write batches. That post
found OPFS writes broken on one npm `latest` build and pinned 1.32.0 -- verify OPFS on your package
version before relying on it.

## R Integration

> Source: https://duckdb.org/docs/2.0/clients/r.html

```r
library(duckdb)

# In-memory
con <- dbConnect(duckdb())

# Persistent
con <- dbConnect(duckdb(), "my_database.duckdb")

# Query files
dbGetQuery(con, "SELECT * FROM read_parquet('data.parquet') LIMIT 10")

# Copy a data.frame into a table, or register it as a virtual table (no copy)
dbWriteTable(con, "mtcars_tbl", mtcars)
duckdb_register(con, "mtcars_view", mtcars)
dbGetQuery(con, "SELECT cyl, avg(mpg) FROM mtcars_tbl GROUP BY cyl")

# dplyr integration via dbplyr; duckplyr offers a dplyr-compatible API
library(dplyr)
tbl(con, "orders") %>%
  filter(amount > 100) %>%
  group_by(region) %>%
  summarize(total = sum(amount))

dbDisconnect(con)
# Shut the database instance down with duckdb_shutdown() on the driver returned by duckdb()
```

## Other Clients (2.0 facts only)

> Source: https://duckdb.org/docs/2.0/clients/go/overview.html
> Source: https://duckdb.org/docs/2.0/clients/node_neo/overview.html
> Source: https://duckdb.org/docs/2.0/clients/java/overview.html
> Source: https://duckdb.org/docs/2.0/clients/rust/overview.html

- **Go:** module `github.com/duckdb/duckdb-go/v2` (moved from `github.com/marcboeker/go-duckdb` at
  v2.5.0; rewrite imports with `gofmt -w -r`, then `go mod tidy`). The client version encodes the DuckDB
  version: DuckDB 2.0.0 = `v2.20000.0`. Arrow is opt-in via build tag `duckdb_arrow`; JSON scanning is
  stricter. cgo required.
- **Node.js:** packages `@duckdb/node-api` (high-level) and `@duckdb/node-bindings` (C API). Still
  unfinished: binding/appending MAP and UNION, user-defined functions, Arrow APIs.
- **Java:** Maven `org.duckdb:duckdb_jdbc`, URL `jdbc:duckdb:` or `jdbc:duckdb:/path/db`; a JDBC URL can
  open a DuckLake catalog directly.
- **Rust:** `cargo add duckdb --features bundled`; crate versions since 1.5.0 take the form
  `1.<major_minor_patch>.x` (the 2.0 docs example pins `~1.20000.0`).
- **Julia:** removed from the core repo in 2.0 in favor of duckdb/DuckDB.jl.

## Sources

- https://duckdb.org/docs/2.0/clients/overview.html
- https://duckdb.org/docs/2.0/clients/python/overview.html
- https://duckdb.org/docs/2.0/clients/python/migration
- https://github.com/duckdb/duckdb-python/releases/tag/v2.0.0
- https://duckdb.org/2026/10/26/gems-of-duckdb-200.html
- https://duckdb.org/docs/2.0/clients/wasm/overview.html
- https://duckdb.org/2026/09/18/opfs-wasm.html
- https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/overview.html
- https://duckdb.org/docs/2.0/clients/r.html
- https://duckdb.org/docs/2.0/clients/go/overview.html
- https://duckdb.org/docs/2.0/clients/node_neo/overview.html
- https://duckdb.org/docs/2.0/clients/java/overview.html
- https://duckdb.org/docs/2.0/clients/rust/overview.html
- https://github.com/duckdb/duckdb/releases/tag/v2.0.0

Fetched: 2026-11-13
