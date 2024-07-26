import psycopg2
import pandas as pd
import os
df = None
conn = None
sql_file_path = os.path.join('sql', 'JobsFiltered.sql')

# Establish database connection
db_params = {
    'dbname': 'JOBdata',
    'user': 'postgres',
    'password': 'Mistyferret1313',
    'host': 'localhost',
    'port': '5432'
}

try:
    with open(sql_file_path, 'r') as file:
        sql_query = file.read()
    print("SQL file read successfully")
except Exception as e:
    print(f"Error reading SQL file: {e}")

# Connect to the database and execute the query
try:
    conn = psycopg2.connect(**db_params)
    df = pd.read_sql_query(sql_query, conn)
except Exception as e:
    print(f"Error: {e}")
finally:
    if conn:
        conn.close()

# Check if df is defined before attempting to save it
if df is not None:
    # Export the result to a CSV file
    df.to_csv('data/Jobsfiltered.csv', index=False)
    print("Query results have been exported to Jobsfiltered.csv")
else:
    print("No data to export")
