import pandas as pd
from collections import Counter
from connect_database import session

session.set_keyspace("netflix_keyspace")



# Create Gold Layer tables if not exist
session.execute("""
    CREATE TABLE IF NOT EXISTS top_countries (
        country TEXT PRIMARY KEY,
        count INT
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS education_distribution (
        education TEXT PRIMARY KEY,
        count INT
    )
""")

session.execute("""
    CREATE TABLE IF NOT EXISTS opensource_by_company (
        companysize TEXT PRIMARY KEY,
        count INT
    )
""")


# Load raw data again
df = pd.read_csv("survey_results_public.csv", low_memory=False)
df.fillna("NA", inplace=True)

# 1. Top 10 countries
top_countries = df['Country'].value_counts().head(10)
session.execute("TRUNCATE top_countries")
for country, count in top_countries.items():
    session.execute("INSERT INTO top_countries (country, count) VALUES (%s, %s)", (country, int(count)))

# 2. Education distribution
edu_dist = df['FormalEducation'].value_counts()
session.execute("TRUNCATE education_distribution")
for edu, count in edu_dist.items():
    session.execute("INSERT INTO education_distribution (education, count) VALUES (%s, %s)", (edu, int(count)))

# 3. Open source by company size
opensource_df = df[df['OpenSource'] == 'Yes']
company_dist = opensource_df['CompanySize'].value_counts()
session.execute("TRUNCATE opensource_by_company")
for size, count in company_dist.items():
    session.execute("INSERT INTO opensource_by_company (companysize, count) VALUES (%s, %s)", (size, int(count)))

print("Aggregated data inserted into Gold Layer tables.")