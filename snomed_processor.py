import polars as pl
import pandas as pd
from pathlib import Path
from datetime import date

file_path = Path('input/sct2_Description_Full-en_US1000124_20250301 3.txt')

df = pl.read_csv(
    file_path,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={

    }
)

df = (
    df.select(["id", "term"])
      .with_columns(pl.lit(date.today().isoformat()).alias("last_updated"))
)



output_file = Path('output/sct2_output.csv')
output_file.parent.mkdir(exist_ok=True)

df.write_csv(output_file)

print(f"Successfully parsed {len(df)} records from SNOMED CT file")
print(f"Saved to {output_file.resolve()}")
print(f"Dataset shape: {df.shape}")
print(f"\nColumn names: {df.columns}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

print(f"\nActive terms count: {df.filter(pl.col('active') == 1).height}")
print(f"Language codes: {df['languageCode'].unique().to_list()}")