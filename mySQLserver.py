import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",         # Your MySQL server
            user="yourusername",      # Replace with your MySQL username
            password="yourpassword"   # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Try to create the database
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()  # Close cursor
            connection.close()  # Close connection
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()

