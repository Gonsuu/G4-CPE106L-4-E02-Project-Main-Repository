import mysql.connector
import random

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
        print(f"Database Connection Error: {err}")
        return None


def insert_order(customer_name, item_name, price):
    """Ensure customer exists, then insert a new order."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()

            # Check if the customer already exists
            cursor.execute("SELECT id FROM customers WHERE name = %s", (customer_name,))
            result = cursor.fetchone()

            if result:
                customer_id = result[0]  # Use existing customer ID
            else:
                # Create a new customer if not found
                customer_id = create_customer(customer_name)
                if not customer_id:
                    print("❌ Error: Unable to create customer.")
                    return

            # Insert order with the retrieved or new customer_id
            query = "INSERT INTO orders (customer_id, item_name, price, status) VALUES (%s, %s, %s, 'Pending')"
            cursor.execute(query, (customer_id, item_name, float(price)))
            conn.commit()
            print("✅ Order saved successfully!")

        except mysql.connector.Error as err:
            print(f"❌ Query Error: {err}")

        finally:
            cursor.close()
            conn.close()

def fetch_orders():
    """Retrieve all orders with customer details."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            query = """
            SELECT orders.id AS order_id, 
                   customers.name AS customer_name,  -- Get the customer name
                   orders.item_name, 
                   orders.price, 
                   COALESCE(orders.status, 'Pending') AS status 
            FROM orders
            JOIN customers ON orders.customer_id = customers.id  -- Join with customers table
            """
            cursor.execute(query)
            orders = cursor.fetchall()
            return orders  # This now includes 'customer_name'
        except mysql.connector.Error as err:
            print(f"❌ Query Error: {err}")
            return []
        finally:
            cursor.close()
            conn.close()

def update_order_status(order_id, status):
    """Update the status of an order."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "UPDATE orders SET status = %s WHERE id = %s"
            cursor.execute(query, (status, order_id))
            conn.commit()
            print("✅ Order status updated successfully!")
        except mysql.connector.Error as err:
            print(f"❌ Query Error: {err}")
        finally:
            cursor.close()
            conn.close()

def delete_order(order_id):
    """Delete an order from the database."""
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM orders WHERE id = %s"
            cursor.execute(query, (order_id,))
            conn.commit()
            print("✅ Order deleted successfully!")
        except mysql.connector.Error as err:
            print(f"❌ Query Error: {err}")
        finally:
            cursor.close()
            conn.close()


def generate_customer_id():
    """Generate a unique random customer ID."""
    conn = connect_db()
    if not conn:
        return None

    try:
        cursor = conn.cursor()
        while True:
            customer_id = random.randint(100000, 999999)  # Generate a 6-digit ID

            # Check if the ID already exists
            cursor.execute("SELECT id FROM customers WHERE id = %s", (customer_id,))
            if not cursor.fetchone():
                return customer_id  # Return only if it's unique
    finally:
        cursor.close()
        conn.close()


def create_customer(name):
    """Create a new customer with a unique ID."""
    customer_id = generate_customer_id()
    if not customer_id:
        print("❌ Error generating customer ID")
        return None

    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO customers (id, name) VALUES (%s, %s)"
            cursor.execute(query, (customer_id, name))
            conn.commit()
            print(f"✅ Customer {name} registered with ID: {customer_id}")
            return customer_id
        except mysql.connector.Error as err:
            print(f"❌ Query Error: {err}")
        finally:
            cursor.close()
            conn.close()
    return None
