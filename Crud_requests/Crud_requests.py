import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(self, host, database, user_name, password):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                database=database,
                user=user_name,
                password=password
            )
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print('Connected to MySQL database')
        except Error as e:
            print(f"Error: {e}")

    def create_customer(self, first_name, last_name, email, phone, address, city, country, zip_code):
        query = """INSERT INTO customer (first_name, last_name, email, phone, address, city, country, zip_code) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (first_name, last_name, email, phone, address, city, country, zip_code)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Customer created successfully")

    def read_customer(self, customer_id):
        query = "SELECT * FROM customer WHERE customer_id = %s"
        self.cursor.execute(query, (customer_id,))
        return self.cursor.fetchone()

    def update_customer(self, customer_id, first_name, last_name, email, phone, address, city, country, zip_code):
        query = """UPDATE customer SET first_name = %s, last_name = %s, email = %s, phone = %s, 
                   address = %s, city = %s, country = %s, zip_code = %s WHERE customer_id = %s"""
        values = (first_name, last_name, email, phone, address, city, country, zip_code, customer_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Customer updated successfully")

    def delete_customer(self, customer_id):
        query = "DELETE FROM customer WHERE customer_id = %s"
        self.cursor.execute(query, (customer_id,))
        self.conn.commit()
        print("Customer deleted successfully")

    def create_order(self, customer_id, order_date, status):
        query = """INSERT INTO orders (customer_id, order_date, status) 
                   VALUES (%s, %s, %s)"""
        values = (customer_id, order_date, status)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Order created successfully")

    def read_order(self, order_id):
        query = "SELECT * FROM orders WHERE order_id = %s"
        self.cursor.execute(query, (order_id,))
        return self.cursor.fetchone()

    def update_order(self, order_id, customer_id, order_date, status):
        query = """UPDATE orders SET customer_id = %s, order_date = %s, status = %s 
                   WHERE order_id = %s"""
        values = (customer_id, order_date, status, order_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Order updated successfully")

    def delete_order(self, order_id):
        query = "DELETE FROM orders WHERE order_id = %s"
        self.cursor.execute(query, (order_id,))
        self.conn.commit()
        print("Order deleted successfully")

    def create_product(self, name, description, price, stock_quantity, category):
        query = """INSERT INTO product (name, description, price, stock_quantity, category) 
                   VALUES (%s, %s, %s, %s, %s)"""
        values = (name, description, price, stock_quantity, category)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Product created successfully")

    def read_product(self, product_id):
        query = "SELECT * FROM product WHERE product_id = %s"
        self.cursor.execute(query, (product_id,))
        return self.cursor.fetchone()

    def update_product(self, product_id, name, description, price, stock_quantity, category):
        query = """UPDATE product SET name = %s, description = %s, price = %s, 
                   stock_quantity = %s, category = %s WHERE product_id = %s"""
        values = (name, description, price, stock_quantity, category, product_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Product updated successfully")

    def delete_product(self, product_id):
        query = "DELETE FROM product WHERE product_id = %s"
        self.cursor.execute(query, (product_id,))
        self.conn.commit()
        print("Product deleted successfully")

    def create_order_product(self, order_id, product_id, quantity):
        query = """INSERT INTO order_product (order_id, product_id, quantity) 
                   VALUES (%s, %s, %s)"""
        values = (order_id, product_id, quantity)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Order product created successfully")

    def read_order_product(self, order_id, product_id):
        query = "SELECT * FROM order_product WHERE order_id = %s AND product_id = %s"
        self.cursor.execute(query, (order_id, product_id))
        return self.cursor.fetchone()

    def update_order_product(self, order_id, product_id, quantity):
        query = """UPDATE order_product SET quantity = %s 
                   WHERE order_id = %s AND product_id = %s"""
        values = (quantity, order_id, product_id)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Order product updated successfully")

    def delete_order_product(self, order_id, product_id):
        query = "DELETE FROM order_product WHERE order_id = %s AND product_id = %s"
        self.cursor.execute(query, (order_id, product_id))
        self.conn.commit()
        print("Order product deleted successfully")

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
        print('MySQL connection is closed')


if __name__ == "__main__":
    db = Database(host='localhost', database='PythonAutomation', user_name='root', password='password')

    db.create_customer("John", "Doe", "john@example.com", "1234567890", "123 Main St", "New York", "USA", "10001")
    print(db.read_customer(1))
    db.update_customer(1, "John", "Smith", "john.smith@example.com", "0987654321", "456 Elm St", "Los Angeles", "USA", "90001")
    db.delete_customer(2)

    db.create_order(1, "2024-07-18", "Prepared")
    print(db.read_order(1))
    db.update_order(1, 1, "2024-07-19", "Shipped")
    db.delete_order(2)

    db.create_product("Laptop", "High performance laptop", 999.99, 100, "Electronics")
    print(db.read_product(1))
    db.update_product(1, "Gaming Laptop", "High performance gaming laptop", 1299.99, 50, "Electronics")
    db.delete_product(2)

    db.create_order_product(1, 1, 2)
    print(db.read_order_product(1, 1))
    db.update_order_product(1, 1, 3)
    db.delete_order_product(1, 1)

    db.close_connection()
