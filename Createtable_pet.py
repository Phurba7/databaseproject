import mysql.connector
connection = mysql.connector.connect(
    host="localhost",      # Replace with your MySQL server host
    user="root",   # Replace with your MySQL username
    password="Ramailo2.",
    db="menagerie"# Replace with your MySQL password
)

if connection.is_connected():
    print("Connected to MySQL server")

    # Create a cursor object
    cursor = connection.cursor()

    # Drop the menagerie database if it exists
    cursor.execute("CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);")

    # Close the cursor and the connection
    cursor.close()
    connection.close()
    print("Disconnected from MySQL server")