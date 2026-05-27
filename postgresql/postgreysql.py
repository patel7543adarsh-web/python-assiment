import psycopg2


def run_database_app():
    # 1. Define your database connection parameters
    # Change these values to match your local PostgreSQL setup
    connection_params = {
        "host": "localhost",
        "database": "postgres",  
        "user": "postgres",  
        "password": "75430",
        "port": "5432",
    }

    connection = None
    cursor = None

    try:
        # 2. Connect to the PostgreSQL database
        print("Connecting to the PostgreSQL database...")
        connection = psycopg2.connect(**connection_params)

        # Create a cursor object to execute SQL commands
        cursor = connection.cursor()

        # 3. Create a Table
        print("Creating table 'users' if it doesn't exist...")
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL
        );
        """
        cursor.execute(create_table_query)

        # 4. Insert Data (Safely using placeholders to prevent SQL Injection)
        print("Inserting a new user...")
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s) ON CONFLICT (email) DO NOTHING;"
        user_data = ("Alice Smith", "alice@example.com")
        cursor.execute(insert_query, user_data)

        # Commit changes to the database
        connection.commit()
        print("Data saved successfully!")

        # 5. Fetch and Query Data
        print("\nFetching all users from the database:")
        cursor.execute("SELECT id, name, email FROM users;")
        records = cursor.fetchall()

        for row in records:
            print(f"ID: {row[0]} | Name: {row[1]} | Email: {row[2]}")

    except Exception as error:
        print(f"An error occurred: {error}")
        # Rollback changes if something went wrong
        if connection:
            connection.rollback()

    finally:
        # 6. Always close the cursor and connection when done
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("\nPostgreSQL connection closed.")


if __name__ == "__main__":
    run_database_app()