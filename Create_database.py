import mysql.connector
connection = mysql.connector.connect(
    host="localhost",      # Replace with your MySQL server host
    user="root",   # Replace with your MySQL username
    password="Ramailo2."   # Replace with your MySQL password
)

if connection.is_connected():
    print("Connected to MySQL server")

    # Create a cursor object
    cursor = connection.cursor()

    # Drop the menagerie database if it exists
    cursor.execute("CREATE DATABASE menagerie")

    # Close the cursor and the connection
    cursor.close()
    connection.close()
    print("Disconnected from MySQL server")