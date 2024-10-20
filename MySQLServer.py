import mysql.connector
from mysql.connector import Error

def create_database():
<<<<<<< HEAD
    # Database credentials
    host_name = 'localhost'
    user_name = 'root'
    password = '@zeytun29'  

    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=password
        )

        # Check if the connection is successful
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")
    
=======
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',    
            password='@zeytun29'     
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

>>>>>>> f473d62f031780257ccd781f1cebd1ec930cd7b1
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
<<<<<<< HEAD
        # Closing the connection
=======
>>>>>>> f473d62f031780257ccd781f1cebd1ec930cd7b1
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()

<<<<<<< HEAD
=======

>>>>>>> f473d62f031780257ccd781f1cebd1ec930cd7b1
