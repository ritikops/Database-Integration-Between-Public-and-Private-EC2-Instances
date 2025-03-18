import mysql.connector

# Database connection settings
db_host = "private-instance-private-ip"
db_user = "admin"
db_password = "StrongPassword"
db_name = "mydb"

try:
    # Connect to database
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = conn.cursor()

    # Create a sample table and insert data
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")
    cursor.execute("INSERT INTO users (name) VALUES ('Ritik'), ('Sonu')")
    conn.commit()

    # Retrieve data
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)

    # Close connection
    cursor.close()
    conn.close()
    print("Database connection successful!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
