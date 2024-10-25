import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        print("Attempting to connect to MySQL...")
        connection = mysql.connector.connect(
            host="localhost",      
            user="root",            
            password="HappinessA1@2020"
        )
        print("Connection successful!")

        cursor = connection.cursor()
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
        cursor.execute(create_db_query)
        connection.commit()

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username or password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection to MySQL server closed.")

if __name__ == "__main__":
    create_database()
