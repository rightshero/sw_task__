import psycopg2
import time
import sys

def wait_for_db(host, port, user, password, max_retries=10):
    retries = 0
    while retries < max_retries:
        try:
            conn = psycopg2.connect(
                host=host,
                port=port,
                user=user,
                password=password,
            )
            conn.close()
            print("Database is available. Proceeding.............")
            return
        except psycopg2.OperationalError:
            print("Database is not yet available. Retrying...")
            retries += 1
            time.sleep(2)
    
    print("Failed to connect to the database after multiple retries. Exiting.")
    sys.exit(1)

if __name__ == "__main__":
    # Replace these with your database connection details
    db_host = "db"
    db_port = 5432
    db_user = "postgres"
    db_password = "abdelrhman"
    
    wait_for_db(db_host, db_port, db_user, db_password)
