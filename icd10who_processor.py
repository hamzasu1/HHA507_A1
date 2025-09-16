## import Module1_MedicalCodexes/icd/who/icd102019syst_codes.txt file as pandas df

import pandas as pd
from pathlib import Path
from datetime import date

file_path = 'input/icd102019syst_codes.txt'

columns = ['code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4','last_updated']





df = pd.read_csv(file_path, sep=';', header=None, names=columns)
df["custom_date"] = "2025-09-14"

for c in df.columns:
    if df[c].dtype== 'object':
        df[c] = df[c].str.strip()  

if 'code' in df.columns:
    df = df.dropna(subset=['code'])




output_path = 'output/icd102019_output.csv'
df.to_csv(output_path, index=False)

print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"Saved to {output_path}")
print(f"\nFirst 5 rows:")
print(df.head())


