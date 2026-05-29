import psycopg2
from psycopg2 import Error

def run_db_operations():
    # Database connection 
    connection_config = {
        "dbname": "postgres",
        "user": "postgres",
        "password": "75430",
        "host": "localhost",
        "port": "5432"
    }
    
    connection = None
    try:
        # connection to the local PostgreSQL database
        print("Connecting to the PostgreSQL database...")
        connection = psycopg2.connect(**connection_config)
        cursor = connection.cursor()
        
        # 1. Create Table
        print("Creating table 'students'...")
        cursor.execute("DROP TABLE IF EXISTS students;")
        create_table_query = """
        CREATE TABLE students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            grade CHAR(1)
        );
        """
        cursor.execute(create_table_query)
        
        # 2. Insert Data.
        print("Inserting sample records...")
        insert_query = "INSERT INTO students (name, grade) VALUES (%s, %s);"
        records_to_insert = [('Aman', 'A'), ('Ram', 'B'), ('Shyam', 'A')]
        cursor.executemany(insert_query, records_to_insert)
        
        # Commit changes to database
        connection.commit()
        print("Data successfully committed.")

        # 3. Select / Query Data
        print("\nFetching and displaying records:")
        cursor.execute("SELECT id, name, grade FROM students;")
        rows = cursor.fetchall()
        
        print(f"{'ID':<5} | {'Name':<12} | {'Grade':<5}")
        print("-" * 30)
        for row in rows:
            print(f"{row[0]:<5} | {row[1]:<12} | {row[2]:<5}")
            
    except (Exception, Error) as error:
        # Catch and print any SQL execution or connection errors
        print(f"\n[ERROR] Database operation failed: {error}")
        if connection:
            connection.rollback()
            
    finally:
        # Guarantee that the database connection closes safely
        if connection:
            cursor.close()
            connection.close()
            print("\nDatabase connection safely closed.")

if __name__ == "__main__":
    run_db_operations()