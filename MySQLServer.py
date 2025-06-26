import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="yusuftest",
        password="testtest"
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error:
    print("Error: did not connect ",)


