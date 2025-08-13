# advanced_script.py
import mysql.connector

# Replace with your actual database credentials
config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'test_db',
    'raise_on_warnings': True
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    print("Connected to MySQL database successfully!")

    # Sample query
    cursor.execute("SELECT 'Hello from MySQL via Python!' AS message;")

    for (message,) in cursor:
        print(message)

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
