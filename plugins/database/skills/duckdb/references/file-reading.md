# DuckDB Universal File Reading Reference

The `read_any` table macro pattern for auto-detecting and reading arbitrary file formats. `read_any` is a
convention from the duckdb-skills plugin (its `read-file` skill), not a DuckDB built-in -- define it
yourself before use.

---

## Universal File Reading with read_any Macro

> Source: https://github.com/duckdb/duckdb-skills
> Source: https://duckdb.org/docs/2.0/core_extensions/overview.html

The macro dispatches to the right reader by file extension. Useful when the format is unknown or when
building tools that accept arbitrary data files:

```sql
-- The read_any macro dispatches to the correct reader based on file extension
CREATE OR REPLACE MACRO read_any(file_name) AS TABLE
  WITH json_case AS (FROM read_json_auto(file_name))
     , csv_case AS (FROM read_csv(file_name))
     , parquet_case AS (FROM read_parquet(file_name))
     , avro_case AS (FROM read_avro(file_name))
     , blob_case AS (FROM read_blob(file_name))
     , spatial_case AS (FROM st_read(file_name))
     , excel_case AS (FROM read_xlsx(file_name))
  FROM query_table(
    CASE
      WHEN file_name ILIKE '%.json' OR file_name ILIKE '%.jsonl'
        OR file_name ILIKE '%.ndjson' OR file_name ILIKE '%.geojson' THEN 'json_case'
      WHEN file_name ILIKE '%.csv' OR file_name ILIKE '%.tsv'
        OR file_name ILIKE '%.tab' OR file_name ILIKE '%.txt' THEN 'csv_case'
      WHEN file_name ILIKE '%.parquet' OR file_name ILIKE '%.pq' THEN 'parquet_case'
      WHEN file_name ILIKE '%.avro' THEN 'avro_case'
      WHEN file_name ILIKE '%.xlsx' THEN 'excel_case'
      WHEN file_name ILIKE '%.shp' OR file_name ILIKE '%.gpkg'
        OR file_name ILIKE '%.fgb' OR file_name ILIKE '%.kml' THEN 'spatial_case'
      ELSE 'blob_case'
    END
  );

-- Usage
FROM read_any('data.csv') LIMIT 10;
DESCRIBE FROM read_any('mystery_file.parquet');
```

**Supported formats via read_any:**

| Extension | Reader | Extension Required |
|---|---|---|
| `.json`, `.jsonl`, `.ndjson`, `.geojson` | `read_json_auto` | `json` (primary core extension, autoloads) |
| `.csv`, `.tsv`, `.tab`, `.txt` | `read_csv` | none (core engine) |
| `.parquet`, `.pq` | `read_parquet` | `parquet` (primary core extension, autoloads) |
| `.avro` | `read_avro` | `avro` (secondary core extension) |
| `.xlsx` | `read_xlsx` | `excel` (autoloads on first use) |
| `.shp`, `.gpkg`, `.fgb`, `.kml` | `st_read` | `spatial` |

## Formats Deliberately Left Out of the Macro

> Source: https://duckdb.org/docs/2.0/core_extensions/excel.html
> Source: https://duckdb.org/docs/2.0/core_extensions/sqlite.html
> Source: https://duckdb.org/docs/2.0/core_extensions/vortex.html

- **`.xls`** -- never route it to `read_xlsx`: the `excel` extension does not support `.xls`. Convert to
  `.xlsx` first.
- **SQLite files (`.db`, `.sqlite`, `.sqlite3`)** -- the extension is now named `sqlite` (aliases
  `sqlite_scanner`, `sqlite3`). The documented route is attaching, not a table function:
  `ATTACH 'file.db' (TYPE sqlite);` then query its tables. `sqlite_attach` is deprecated.
- **Vortex (`.vortex`)** -- `INSTALL AND LOAD vortex;` then `read_vortex('f.vortex')`. Always write with
  an explicit `FORMAT vortex`; without the extension loaded, `COPY ... TO 'f.vortex'` silently writes CSV.
- **Lance (`.lance`)** -- third-party `lance` extension; read with `FROM 'example.lance'`.

## 2.0 Reader Options Worth Knowing

> Source: https://duckdb.org/docs/2.0/data/parquet/overview.html
> Source: https://duckdb.org/docs/2.0/data/csv/overview.html

- `read_parquet(..., allow_empty = true)` and `read_csv(..., allow_empty = true)` return an empty result
  (single BOOL column `empty`) instead of erroring when a glob matches no files. Use this in macros fed
  by user-supplied globs.
- `read_parquet(..., utf8_validation = 'replace' | 'ignore')` tolerates invalid UTF-8 (default `strict`
  errors).
- Excel: `read_xlsx` defaults to the first sheet; `sheet`, `range`, `all_varchar`, `ignore_errors`
  options are available.

## Sources

- https://github.com/duckdb/duckdb-skills
- https://duckdb.org/docs/2.0/core_extensions/overview.html
- https://duckdb.org/docs/2.0/core_extensions/excel.html
- https://duckdb.org/docs/2.0/core_extensions/sqlite.html
- https://duckdb.org/docs/2.0/core_extensions/vortex.html
- https://duckdb.org/2026/03/23/announcing-duckdb-151.html
- https://duckdb.org/docs/2.0/data/parquet/overview.html
- https://duckdb.org/docs/2.0/data/csv/overview.html

Fetched: 2026-11-13
