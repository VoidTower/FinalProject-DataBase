from connect_database import session

# Set the correct keyspace
session.set_keyspace('netflix_keyspace')

# Create the survey_results table
session.execute("""
    CREATE TABLE IF NOT EXISTS survey_results (
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

print("Table 'survey_results' created.")