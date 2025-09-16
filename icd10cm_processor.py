import pandas as pd 
import re
from datetime import date
from pathlib import Path

# Define the file path
file_path= 'input/icd10cm_order_2025.txt'

# This initializes a blank list to hold the parsed codes (e.g., individual rows from the text file)
codes = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:

        # Remove whitespace and check line length
        line = line.rstrip('\n\r')
        if len(line) < 15:  # Skip lines that are too short
            continue

        # Parse the fixed-length format based on pdf instructions
        order_num = line[0:5].strip()  # Order number, first 6 characters
        code = line[6:13].strip()  # ICD-10-CM codAe, characters 7-13
        level = line[14:15].strip()  # Level indicator (0 or 1), character 15

        # Parse description and description_detailed that follows
        remaining_text = line[16:]  # Text after position 16
        
        # Split by 4+ consecutive spaces to separate description from description_detailed
        parts = re.split(r'\s{4,}', remaining_text, 1)

        # Extract description and description_detailed
        description = parts[0].strip() if len(parts) > 0 else ""
        description_detailed = parts[1].strip() if len(parts) > 1 else ""

        # Append the parsed data to the codes list
        codes.append({
            'order_num': order_num,
            'code': code,
            'level': level,
            'description': description,
            'description_detailed': description_detailed,
            'date_added': '2025-09-14'
        
        })

df = pd.DataFrame(codes)
for c in df.select_dtypes(include=['object']).columns:
    df[c] = df[c].str.strip()   
if {"order_num", "code"}.issubset(df.columns): 
    df = df.dropna(subset=["order_num", "code"])


## Create a DataFrame from the parsed codes
icdcodes = pd.DataFrame(codes)

## Save the DataFrame to a CSV file
icdcodes.to_csv("output/icd10cm_output.csv", index=False)




