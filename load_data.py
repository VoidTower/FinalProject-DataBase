import os
import pandas as pd
import uuid
from cassandra.query import BatchStatement
from cassandra.query import ConsistencyLevel
from connect_database import session

# Set keyspace
session.set_keyspace("netflix_keyspace")

# Load the Stack Overflow dataset
base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, "survey_results_public.csv"), low_memory=False)

# Select relevant columns
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
df.columns = [col.lower() for col in df.columns]  # lowercase column names
df.fillna("NA", inplace=True)

print("Loaded StackOverflow Data:", df.shape)

# Create table if it doesn't exist
session.execute("""
    CREATE TABLE IF NOT EXISTS developer_survey (
        id UUID PRIMARY KEY,
        hobby TEXT,
        opensource TEXT,
        country TEXT,
        student TEXT,
        employment TEXT,
        formaleducation TEXT,
        undergradmajor TEXT,
        companysize TEXT
    )
""")

# Prepare insert statement
insert_query = session.prepare("""
    INSERT INTO developer_survey (
        id, hobby, opensource, country, student, employment,
        formaleducation, undergradmajor, companysize
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""")

# Batch insert
batch = BatchStatement(consistency_level=ConsistencyLevel.QUORUM)
batch_size = 50  # Tune this size depending on performance testing
count = 0

for _, row in df.iterrows():
    batch.add(insert_query, (
        uuid.uuid4(),
        row['hobby'],
        row['opensource'],
        row['country'],
        row['student'],
        row['employment'],
        row['formaleducation'],
        row['undergradmajor'],
        row['companysize']
    ))

    count += 1

    # Execute batch every `batch_size` rows
    if count % batch_size == 0:
        session.execute(batch)
        batch.clear()

# Insert remaining records
if len(batch) > 0:
    session.execute(batch)

print(f" All {count} records inserted into 'developer_survey' using batch insert!")