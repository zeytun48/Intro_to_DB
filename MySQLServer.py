import mysql.connector
from mysql.connector import Error

def create_database():
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
    
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()

