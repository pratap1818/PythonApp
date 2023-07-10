import os
import psycopg2

# Read the environment variables
project_id = os.environ['PROJECT_ID']
postgres_host = os.environ['POSTGRES_HOST']
postgres_port = os.environ['POSTGRES_PORT']
postgres_database = os.environ['POSTGRES_DATABASE']
postgres_user = os.environ['POSTGRES_USER']
postgres_password = os.environ['POSTGRES_PASSWORD']
sql_file_path = os.environ['SQL_FILE_PATH']

# Read the SQL file contents
with open(sql_file_path, 'r') as file:
    sql_script = file.read()

# Connect to the PostgreSQL server
conn = psycopg2.connect(
    host=postgres_host,
    port=postgres_port,
    database=postgres_database,
    user=postgres_user,
    password=postgres_password
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute the SQL script
cursor.execute(sql_script)

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
