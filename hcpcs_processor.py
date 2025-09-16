from datetime import date
import pandas as pd
from pathlib import Path

file_path = "input/HCPC2025_OCT_ANWEB_v3.txt"

colspecs = [(0, 11), (11, 90), (90, 180), (180, 250)]  
column_names = [
    "Code", "Description1", "Description2", "Last Updated"
]
df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names, )

df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
df = df.dropna(subset=["Code"])
df = df[df["Code"].str.strip() != ""]


df["last_updated"] = date.today().isoformat()

print(df.head())

## save as csv to Module1_MedicalCodexes/hcpcs/output
output_path = "output/hcpc2025_output.csv"
df.to_csv(output_path, index=False)


