# Sarah-nourish

## Working with the dataset

The repository ships with the raw CSV (`data.csv`) and SQLite snapshot (`nourish_members.sqlite`) checked in directly. No Git LFS step is required—just clone or pull as usual. Both files are ~70–80 MB, so the first clone may take a moment.

## Optional: create a Parquet copy

For faster analytics inside ephemeral environments you can materialize a compressed Parquet file (requires `pip install duckdb`):

```bash
python scripts/prepare_parquet.py --csv data.csv --out artifacts/nourish_members.parquet
```

Adjust the output path or compression options as needed.
