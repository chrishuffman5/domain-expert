# DuckDB Quack Remote Protocol Reference

> **Status (as of DuckDB 2.0.0, 2026-10-21).** Quack first shipped as a core extension in **v1.5.3**
> (2026-05-20, beta). DuckDB 2.0.0 ships "a polished version of the Quack protocol with substantial
> performance and stability improvements" and adds `CONNECT` plus `duckdb -serve` / `-connect`.
> **The Quack FAQ still labels it beta and says the protocol is not yet stable** -- breaking changes
> to the protocol, function names, and default settings are expected. Never call it GA or stable.
> Pin the DuckDB version on client and server, and re-review settings on every upgrade.

> Source: https://duckdb.org/quack/faq
> Source: https://duckdb.org/2026/10/21/announcing-duckdb-200.html
> Source: https://duckdb.org/docs/2.0/core_extensions/quack.html

## What Quack Is

> Source: https://duckdb.org/docs/2.0/quack/overview.html
> Source: https://duckdb.org/docs/2.0/connect/concurrency.html

Quack is an HTTP-based RPC protocol that turns DuckDB into a client-server database: a server process
exposes its full SQL surface, and other DuckDB processes query it as if the remote tables were local.

It is the documented answer to DuckDB's single-writer limit: "Writing to DuckDB's native database
format from multiple processes is supported through the Quack remote protocol." The other answer is
DuckLake with a PostgreSQL catalog (DuckLake 1.1 shipped with 2.0). Quack does **not** do distributed
query processing; it is point-to-point client/server access.

**Transport:**

- HTTP (the FAQ says HTTP v2.0); HTTPS for non-local servers.
- After the connection handshake, each query is one request/response pair; large results stream back
  in chunks via follow-up `FETCH` requests. Every interaction is client-initiated.
- DuckDB-Wasm can speak Quack natively (May 2026 announcement).

## Installation

> Source: https://duckdb.org/docs/2.0/core_extensions/quack.html

Autoinstalled and autoloaded on first use. Explicit forms: `INSTALL quack; LOAD quack;`. Support tier:
DuckDB team, secondary. Source repo: https://github.com/duckdb/duckdb-quack.

## Server Setup

> Source: https://duckdb.org/docs/2.0/quack/overview.html
> Source: https://duckdb.org/docs/2.0/quack/reference.html

```sql
-- URI is optional; quack_serve() listens on quack:localhost (port 9494)
CALL quack_serve('quack:localhost');
CALL quack_serve(token = 'super_secret');                 -- explicit token, min 4 characters
CALL quack_serve('quack:0.0.0.0:9494', allow_other_hostname = true);  -- testing only
CALL quack_stop('quack:localhost');
```

```bash
duckdb my.duckdb -serve        # CLI: serve the opened database (binds localhost)
```

`quack_serve` returns the listen URI, the HTTP URL and, when the default authentication function is in
use, the `auth_token` clients need.

| `quack_serve` parameter | Default | Notes |
|---|---|---|
| `listen_uri` (positional) | `quack:localhost` | |
| `allow_other_hostname` | `false` | required to bind a non-local host such as `0.0.0.0` |
| `token` | generated | min 4 chars; if omitted: default `quack` secret's token, else random |
| `secret` | unset | name of an existing `quack` secret whose token to use |
| `create_secret_if_not_exists` | `false` | persist the generated token as the default `quack` secret |
| `disable_ssl` | `true` local, `false` otherwise | serve plain HTTP |
| `ssl_cert_file`, `ssl_key_file` | generated | omitted on non-local URIs -> self-signed certificate |

URI forms (`quack:` scheme, default port 9494): `quack:localhost`, `quack://localhost`,
`quack:myhost:9000`, `quack:127.0.0.1`, `quack:[::1]:1234`. Validate with `quack_uri_parser(uri, ssl)`.

Other server functions: `quack_server_list()`, `quack_active_connections()`,
`quack_generate_keys(directory = path)` (self-signed `server.pem` + `private_key.pem`),
`quack_identify(name, provider, hostname, region, meta)` and the `whoami()` macro for node identity.

| Setting | Default |
|---|---|
| `quack_server_max_connections` | `1024` (new connections refused beyond it) |
| `quack_server_keep_alive_timeout` | `300` seconds |
| `quack_target_batch_bytes` | 32 MiB |
| `quack_server_stream_buffer_bytes` | 256 MiB |
| `quack_result_ttl` | `3600` |
| `quack_enable_reconnects` | `false` |

`quack_debug_*` settings exist for protocol testing only -- never set them in production.

## Client Setup

> Source: https://duckdb.org/docs/2.0/quack/overview.html
> Source: https://duckdb.org/docs/2.0/sql/statements/connect.html

### 1. Stateless one-off query -- `quack_query`

```sql
FROM quack_query('quack:localhost', 'SELECT 42', token = 'super_secret');
-- disable_ssl = true forces plain HTTP to a remote host (avoid outside testing)
```

### 2. Attach, then `CONNECT` (recommended, 2.0+)

```sql
ATTACH 'quack:localhost' AS qk (TOKEN 'super_secret');
CONNECT qk;                    -- unqualified SQL now runs on the server; results stream back
SELECT count(*) FROM hello;
DISCONNECT;                    -- back to the local database (error if none active)

FROM qk.query('SELECT 42');    -- ad-hoc remote SQL without CONNECT
DETACH qk;
```

`CONNECT` is not Quack-specific: it also targets PostgreSQL and MySQL (`postgres:` + libpq string),
where the 2.0 remote pushdown optimizer sends SQL to the server instead of pulling tables. In-process
local databases (in-memory, database files) cannot be `CONNECT` targets. CLI: `duckdb -connect`; in the
CLI the first Ctrl+D disconnects a `CONNECT`ed remote, the second exits.

ATTACH options: `TOKEN`, `DISABLE_SSL`, `TYPE`, `SSL_FINGERPRINT`, `CLIENT_ID`, `HEARTBEAT_TIMEOUT`.

**Caveat:** `ATTACH` binds every remote table definition on the client; one definition that fails to
bind (e.g. lazily resolved Iceberg tables on the server) fails the whole attach. For Iceberg catalogs on
the server, attach them with `TABLE_RESOLUTION 'eager'`.

### 3. Secret-based auth (keeps tokens out of SQL)

```sql
CREATE SECRET (TYPE quack, TOKEN 'super_secret', SCOPE 'quack:localhost');
ATTACH 'quack:localhost' AS remote (TYPE quack);
```

An explicit `TOKEN` / `token =` always overrides a matching secret.

## Security

> Source: https://duckdb.org/docs/2.0/quack/security.html
> Source: https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/overview.html

A Quack server exposes the **full SQL surface** of the underlying DuckDB instance. Any client holding the
token has full SQL access. Treat a running server as a published database endpoint.

### Transport: HTTP for local, HTTPS otherwise

- Clients pick plain HTTP for `localhost`, `127.0.0.1`, `::1` and HTTPS for everything else.
- Servers do **not** use TLS for local URIs. Non-local servers serve **HTTPS with a self-signed
  certificate** unless `ssl_cert_file` and `ssl_key_file` are passed. A self-signed cert does not
  replace a trusted certificate in production.
- `DISABLE_SSL` / `disable_ssl = true` overrides the choice. Never use it for non-local traffic --
  queries and tokens cross the network in clear text.

### Recommended endpoint: TLS-terminating reverse proxy

"Do not expose Quack directly to the internet." Bind the server to localhost and put a proven HTTP
reverse proxy (nginx or Caddy recipes in the docs) in front of it to terminate TLS. Use the proxy
instead of `allow_other_hostname`, which the 2.0 announcement calls "only meant for testing".

```
client --HTTPS:443--> reverse proxy (TLS termination) --HTTP--> quack server (localhost:9494)
```

The deployment docs ship one recipe today: an AWS CloudFormation template running the quack extension on
EC2 behind nginx with Let's Encrypt, opening only ports 80 (ACME challenge) and 443 (HTTPS).

### Authentication and authorization hooks

| Setting (GLOBAL) | Default | Fires on | Signature |
|---|---|---|---|
| `quack_authentication_function` | `quack_check_token` | `CONNECTION_REQUEST` | `(session_id, client_token, server_token)` |
| `quack_authorization_function` | `quack_nop_authorization` | `PREPARE_REQUEST` (per query) | `(connection_id, query)` |

- The default authentication compares the client token with the server token. The default authorization
  is permissive: it returns the query unchanged.
- A callback that returns `false` or `NULL`, or errors, rejects the request (`Authentication failed` /
  `Authorization failed`). Return BOOLEAN to admit. An authorization function may instead return a
  VARCHAR, which runs in place of the client's query.
- Set with `SET GLOBAL quack_authentication_function = 'check_token';`. Plain `RESET` leaves a stale
  value for these global-only settings; use `RESET GLOBAL`.
- Callbacks run on a fresh transient server-side connection: no session-local state, Python UDFs from
  `con.create_function` are not visible, and SQL macros cannot do DML.
- For enforced read-only access, attach the served database read-only or inspect the **parsed statement
  type**. A regex on the query prefix is not a robust filter (`WITH ... INSERT` passes it).

### Hardening checklist

- Supply your own strong token (min 4 characters), store it as a `quack` secret, rotate it, keep it out
  of source control. `duckdb -serve` stores its token in a **persistent, unencrypted** `quack` secret.
- Keep the server on localhost; reach it only through the reverse proxy; firewall port 9494.
- Never set `DISABLE_SSL` for remote clients.
- Install an authorization function for least privilege; use per-user tokens when several clients connect.
- Never enable developer-mode authentication outside a sandbox.
- Pin the DuckDB version on both ends: the protocol is not yet declared stable.

## Logging

> Source: https://duckdb.org/docs/2.0/quack/reference.html

```sql
CALL enable_logging('Quack');
FROM duckdb_logs_parsed('Quack');
CALL enable_logging('HTTP');          -- transport-level detail: duckdb_logs_parsed('HTTP')
```

## Quack as a DuckLake Catalog

> Source: https://ducklake.select/docs/stable/duckdb/usage/choosing_a_catalog_database.html

Serve the DuckDB metadata file with `quack_serve`, then on clients:
`ATTACH 'ducklake:quack:localhost' AS my_ducklake (DATA_PATH '/abs/shared/path/');`. Use an absolute or
object-storage `DATA_PATH` (relative paths resolve per client working directory). `set_option` changes
are not undone by `ROLLBACK`. The Quack FAQ calls this use experimental.

## Protocol Summary

> Source: https://duckdb.org/docs/2.0/quack/overview.html

| Aspect | Value |
|---|---|
| Transport | HTTP (v2.0 per FAQ) |
| URI scheme | `quack:` |
| Default port | `9494` |
| Local transport | plain HTTP (localhost / 127.0.0.1 / ::1) |
| Remote transport | HTTPS; server self-signs unless given cert + key |
| Recommended production endpoint | HTTPS via TLS-terminating reverse proxy |
| Interaction model | client-driven request/response; results streamed via `FETCH` |

## Limitations and Caveats

> Source: https://duckdb.org/quack/faq
> Source: https://duckdb.org/2026/05/12/quack-remote-protocol.html

- **Not yet stable.** FAQ: beta, protocol not yet stable, breaking changes expected.
- **No distributed query processing.** Native storage served over Quack scales to "a few terabytes" (FAQ).
- **Write throughput.** FAQ: "a few thousand writes per second on a server with 8 CPUs and 32 GB RAM".
  The May 2026 benchmark saw small-write throughput stop scaling at 8 threads because of a DuckDB limit
  on concurrent inserts into the same table; no thread cap is documented for 2.0.
- **Full SQL surface exposed** -- without an authorization function an authenticated client can do
  anything the server session can.
- **All-or-nothing ATTACH** -- one unbindable remote table definition fails the attach.

## Sources

- https://duckdb.org/quack/faq
- https://duckdb.org/quack/
- https://duckdb.org/docs/2.0/quack/overview.html
- https://duckdb.org/docs/2.0/quack/reference.html
- https://duckdb.org/docs/2.0/quack/security.html
- https://duckdb.org/docs/2.0/quack/setup/deployment.html
- https://duckdb.org/docs/2.0/core_extensions/quack.html
- https://duckdb.org/docs/2.0/sql/statements/connect.html
- https://duckdb.org/docs/2.0/connect/concurrency.html
- https://duckdb.org/docs/2.0/operations_manual/securing_duckdb/overview.html
- https://duckdb.org/2026/10/21/announcing-duckdb-200.html
- https://duckdb.org/2026/05/20/announcing-duckdb-153.html
- https://duckdb.org/2026/05/12/quack-remote-protocol.html
- https://ducklake.select/docs/stable/duckdb/usage/choosing_a_catalog_database.html

Fetched: 2026-11-13
