import mysql.connector

def connect_db():
    """Connect to MySQL database."""
    try:
        conn = mysql.connector.connect(
            host="sql12.freesqldatabase.com",
            user="sql12765842",
            password="eVmqvnqEm3",
            database="sql12765842",
            port=3306
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def insert_order(item_name, price):
    """Insert an order into the database."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO orders (item_name, price) VALUES (%s, %s)"
            cursor.execute(query, (item_name, price))
            conn.commit()
            cursor.close()
            conn.close()
            print(f"✅ Order inserted: {item_name} - ${price}")
        except mysql.connector.Error as err:
            print(f"Error inserting order: {err}")
