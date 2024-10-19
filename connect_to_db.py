import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",         # Your MySQL server, often localhost
    user="yourusername",       # Replace with your MySQL username
    password="yourpassword",   # Replace with your MySQL password
    database="alx_book_store"  # This is the database we created
)

if connection.is_connected():
    print("Connected to the MySQL database!")
    connection.close()

