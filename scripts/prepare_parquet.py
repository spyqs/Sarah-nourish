#!/usr/bin/env python3
"""Utility to materialize the Nourish dataset as Parquet for fast analytics.

Usage:
    python scripts/prepare_parquet.py --csv data.csv --out data/parquet/nourish_members.parquet

All arguments are optional; defaults assume the repository root paths. The script
requires the DuckDB Python module (`pip install duckdb`). We use DuckDB's
`read_csv_auto` because it handles the mixed typing in the feed and keeps
null-aware parsing.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

try:
    import duckdb  # type: ignore
except ModuleNotFoundError as exc:  # pragma: no cover - dependency check
    sys.stderr.write(
        "DuckDB Python package is required. Install with `pip install duckdb`.\n"
    )
    raise SystemExit(1) from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        type=Path,
        default=Path("data.csv"),
        help="Path to the CSV exported from Git LFS",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("artifacts/nourish_members.parquet"),
        help="Destination Parquet path (directories will be created if missing)",
    )
    parser.add_argument(
        "--compression",
        default="zstd",
        choices=["zstd", "snappy", "gzip", "none"],
        help="Parquet compression codec to use",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.csv.exists():
        raise SystemExit(f"CSV not found at {args.csv}. Run `git lfs pull` first.")

    args.out.parent.mkdir(parents=True, exist_ok=True)

    compression = "UNCOMPRESSED" if args.compression == "none" else args.compression.upper()

    # DuckDB reads and writes in-process, so we open an in-memory connection.
    con = duckdb.connect()
    con.execute(
        f"""
        COPY (
            SELECT *
            FROM read_csv_auto('{args.csv.as_posix()}', ALL_VARCHAR=TRUE)
        ) TO '{args.out.as_posix()}'
        (FORMAT 'parquet', COMPRESSION '{compression}');
        """
    )
    con.close()
    print(f"Parquet file written to {args.out} with compression={args.compression}.")


if __name__ == "__main__":
    main()
