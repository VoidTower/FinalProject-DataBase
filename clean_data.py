# clean_data.py

import os
import pandas as pd

# Use project root as base_dir
base_dir = os.path.dirname(os.path.abspath(__file__))

# Load raw data from root folder
csv_path = os.path.join(base_dir, "survey_results_public.csv")
df = pd.read_csv(csv_path, low_memory=False)

# Select subset of relevant columns
columns = [
    "Hobby",
    "OpenSource",
    "Country",
    "Student",
    "Employment",
    "FormalEducation",
    "UndergradMajor",
    "CompanySize"
]
df = df[columns]

# Clean: lowercase headers, fill missing values, normalize text
df.columns = [col.lower() for col in df.columns]
df = df.fillna("NA")
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].str.strip().str.lower()

# Save cleaned file to root
df.to_csv(os.path.join(base_dir, "cleaned_stackoverflow.csv"), index=False)

print(" Cleaned data saved as cleaned_stackoverflow.csv")
print(" Preview:")
print(df.head(10))