# MySQL CRUD Operations with Python

This project demonstrates how to perform basic CRUD (Create, Read, Update, Delete) operations using Python and MySQL. The code connects to a MySQL database and provides methods to manage customers, orders, products, and the relationships between orders and products.

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` library

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required Python packages:**

    ```bash
    pip install mysql-connector-python
    ```

3. **Set up your MySQL database:**

    Create a database named `PythonAutomation` and the necessary tables:

    ```sql
    CREATE DATABASE PythonAutomation;
    USE PythonAutomation;

    CREATE TABLE customer (
        customer_id INT AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(255),
        last_name VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(255),
        address VARCHAR(255),
        city VARCHAR(255),
        country VARCHAR(255),
        zip_code VARCHAR(255)
    );

    CREATE TABLE orders (
        order_id INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        order_date DATE,
        status VARCHAR(255),
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
    );

    CREATE TABLE product (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        description TEXT,
        price DECIMAL(10, 2),
        stock_quantity INT,
        category VARCHAR(255)
    );

    CREATE TABLE order_product (
        order_id INT,
        product_id INT,
        quantity INT,
        PRIMARY KEY (order_id, product_id),
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES product(product_id)
    );
    ```

## Usage

1. **Update the database configuration:**

    Edit the `db_config` parameters in the `Database` class initialization to match your MySQL server settings:

    ```python
    db = Database(host='localhost', database='PythonAutomation', user_name='root', password='rootpassword')
    ```

2. **Run the script:**

    ```bash
    python <script_name>.py
    ```

    The script will perform the following operations:

    - Create a customer
    - Read a customer's details
    - Update a customer's details
    - Delete a customer
    - Create an order
    - Read an order's details
    - Update an order's details
    - Delete an order
    - Create a product
    - Read a product's details
    - Update a product's details
    - Delete a product
    - Create a relationship between an order and a product
    - Read a relationship between an order and a product
    - Update a relationship between an order and a product
    - Delete a relationship between an order and a product

3. **Example output:**

    ```bash
    Connected to MySQL database
    Customer created successfully
    (1, 'John', 'Doe', 'john@example.com', '1234567890', '123 Main St', 'New York', 'USA', '10001')
    Customer updated successfully
    Customer deleted successfully
    Order created successfully
    (1, 1, datetime.date(2024, 7, 18), 'Prepared')
    Order updated successfully
    Order deleted successfully
    Product created successfully
    (1, 'Laptop', 'High performance laptop', Decimal('999.99'), 100, 'Electronics')
    Product updated successfully
    Product deleted successfully
    Order product created successfully
    (1, 1, 2)
    Order product updated successfully
    Order product deleted successfully
    MySQL connection is closed
    ```
