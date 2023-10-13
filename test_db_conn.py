import psycopg2

# Define your database connection parameters
db_params = {
    'dbname': 'categories_task',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': '5432',       
}

try:
    # Attempt to connect to the database
    connection = psycopg2.connect(**db_params)
    print("Database connection successful.")
    connection.close()
except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
