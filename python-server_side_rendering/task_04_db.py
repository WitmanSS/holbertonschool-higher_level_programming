#!/usr/bin/python3
"""
A Flask application that reads product data from JSON, CSV, or SQLite database,
filters it based on URL query parameters, and renders it dynamically.
"""
from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

# Instantiate the Flask application
app = Flask(__name__)

# --- Database Setup and Management ---

def create_database():
    """Creates the SQLite database and populates the Products table."""
    conn = None
    try:
        # Connects to the database (creates it if it doesn't exist)
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Create Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        
        # Insert Example Data (using REPLACE INTO to handle multiple runs gracefully)
        cursor.execute('''
            REPLACE INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error during setup: {e}")
    finally:
        if conn:
            conn.close()

# --- Helper Functions for Data Reading ---

def read_json_data(filepath):
    """Reads and parses data from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    except Exception as e:
        print(f"An error occurred while reading JSON: {e}")
        return None

def read_csv_data(filepath):
    """Reads and parses data from a CSV file."""
    data = []
    try:
        with open(filepath, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
                except ValueError:
                    continue
        return data
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred while reading CSV: {e}")
        return None

def read_sql_data(product_id=None):
    """Reads data from the SQLite database, optionally filtered by ID."""
    conn = None
    data = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row  # Allows accessing columns by name
        cursor = conn.cursor()
        
        # Build query
        query = "SELECT id, name, category, price FROM Products"
        params = ()
        
        if product_id is not None:
            query += " WHERE id = ?"
            params = (product_id,)
        
        cursor.execute(query, params)
        
        # Convert sqlite3.Row objects to standard dictionaries
        rows = cursor.fetchall()
        data = [dict(row) for row in rows]
        
        return data
    except sqlite3.Error as e:
        # Return an error message to be displayed in the template
        return f"Database Error: {e}"
    finally:
        if conn:
            conn.close()

# --- Flask Route ---

@app.route('/products', methods=['GET'])
def products():
    """
    Handles product display logic based on 'source' and 'id' query parameters.
    """
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    data = []
    error_message = None
    product_id = None
    
    # 1. Parse and Validate optional ID
    if product_id_str is not None:
        try:
            product_id = int(product_id_str)
        except ValueError:
            error_message = "Invalid product ID format."
    
    # 2. Determine Source and Load Data (only if no ID parsing error)
    if not error_message:
        base_dir = os.path.dirname(__file__)
        
        if source == 'json':
            filepath = os.path.join(base_dir, 'products.json')
            data = read_json_data(filepath)
        elif source == 'csv':
            filepath = os.path.join(base_dir, 'products.csv')
            data = read_csv_data(filepath)
        elif source == 'sql':
            # SQLite function handles both filtered and full lists
            data = read_sql_data(product_id)
            if isinstance(data, str):
                error_message = data
                data = []
        else:
            # Handle wrong source
            error_message = "Wrong source. Please specify 'json', 'csv', or 'sql'."
            
        # Handle File Not Found errors for JSON/CSV (read_*_data returns None)
        if data is None:
             error_message = f"Error: The specified data file for source '{source}' was not found."
             data = []
        
        # 3. Apply ID Filter (for JSON/CSV sources only, SQL is filtered in the function)
        if source in ['json', 'csv'] and product_id is not None and not error_message:
            filtered_data = [product for product in data if product.get('id') == product_id]
            
            if not filtered_data:
                error_message = "Product not found"
                data = []
            else:
                data = filtered_data

    # 4. Render Template
    return render_template(
        'product_display.html',
        products=data,
        error=error_message
    )

# --- Run Server ---

if __name__ == '__main__':
    # 0. Setup Database before starting the application
    create_database()
    
    # Run the application on the default host and port
    app.run(debug=True, port=5000)
