# Sarah-nourish

## Working with the dataset

This repo stores the large CSV and SQLite snapshots via Git LFS. After cloning, run:

```bash
git lfs install
git lfs pull
```

To materialize an analytics-friendly Parquet copy inside your ephemeral environment, use the helper script (requires `pip install duckdb`):

```bash
python scripts/prepare_parquet.py --csv data.csv --out artifacts/nourish_members.parquet
```

Adjust `--out` if you want the file in a different location or compression format.
