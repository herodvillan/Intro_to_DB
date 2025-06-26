import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="yusuftest",
        password="testtest"
    )

    cursor = conn.cursor()
    print("connected succsfuly")
except mysql.connector.Error:
    print("Error: did not connect ",)


