PostgreSQL Python Operations Script

What This Program Does:
This Python script connects to a local PostgreSQL instance to demonstrate 
fundamental database interactions using the 'psycopg2' library. 

When executed, the program:
1. Connects to the database server using specified credentials.
2. Clears out any existing older versions of the 'students' table.
3. Creates a fresh 'students' table with tracking columns (ID, Name, Grade).
4. Inserts a batch of mock records safely using parameterized queries.
5. Queries the table to pull all active records and prints them cleanly 
   to the terminal.
6. Safely disconnects from the database server, handling any unexpected 
   errors gracefully via rollbacks.

How to Run:

1. Open your terminal.
2. Navigate to the directory containing 'student.py'.
3. Run the script using the following command:
   python student.py

Expected Output:
----------------
Connecting to the PostgreSQL database...
Creating table 'students'...
Inserting sample records...
Data successfully committed.

Fetching and displaying records:
ID    | Name         | Grade
------------------------------
1     | Aman      | A    
2     | Ram       | B    
3     | Shyam     | A    

Database connection safely closed.
