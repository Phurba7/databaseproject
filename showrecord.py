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
    cursor.execute( '''SELECT DISTINCT name, birth, MONTH(birth) 
                        FROM  pet 
                        ORDER BY MONTH(birth),birth''')
    table_structure = cursor.fetchall()
    # Print the structure of the pet table
    #print("Structure of the pet table:")
    for column_info in table_structure:
        print(column_info)

    # Close the cursor and the connection
    cursor.close()
    connection.close()
    print("Disconnected from MySQL server")