#!/usr/bin/python3
"""
A Flask application that reads product data from JSON or CSV files,
filters it based on URL query parameters, and renders it dynamically.
"""
from flask import Flask, render_template, request
import json
import csv
import os

# Instantiate the Flask application
app = Flask(__name__)

# --- Helper Functions for Data Reading ---

def read_json_data(filepath):
    """Reads and parses data from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {filepath}")
        return []
    except Exception as e:
        print(f"An error occurred while reading JSON: {e}")
        return []

def read_csv_data(filepath):
    """Reads and parses data from a CSV file."""
    data = []
    try:
        with open(filepath, 'r', newline='') as f:
            # Use DictReader to treat each row as a dictionary
            reader = csv.DictReader(f)
            for row in reader:
                # Convert 'id' and 'price' to appropriate types for filtering/display
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    data.append(row)
                except ValueError:
                    # Skip rows with invalid numeric data
                    continue
        return data
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"An error occurred while reading CSV: {e}")
        return []

# --- Flask Route ---

@app.route('/products', methods=['GET'])
def products():
    """
    Handles product display logic based on 'source' and 'id' query parameters.
    """
    # Get query parameters
    source = request.args.get('source')
    product_id_str = request.args.get('id')
    
    data = []
    error_message = None
    
    # 1. Determine Source and Load Data
    if source == 'json':
        filepath = os.path.join(os.path.dirname(__file__), 'products.json')
        data = read_json_data(filepath)
    elif source == 'csv':
        filepath = os.path.join(os.path.dirname(__file__), 'products.csv')
        data = read_csv_data(filepath)
    else:
        # Handle wrong source
        error_message = "Wrong source. Please specify 'json' or 'csv'."
        # If the data file itself wasn't found (e.g., read_*_data returned None)
    if data is None:
        error_message = f"Error: The specified data file for source '{source}' was not found."
        data = []
    
    # 2. Filter Data by ID (if provided and no initial error)
    if product_id_str is not None and not error_message:
        try:
            # Convert the ID parameter to an integer
            product_id = int(product_id_str)
            
            # Filter the loaded data
            filtered_data = [product for product in data if product.get('id') == product_id]
            
            if not filtered_data:
                # Handle product not found
                error_message = "Product not found"
                data = [] # Clear data list to prevent empty table rendering
            else:
                data = filtered_data # Replace full list with filtered list
                
        except ValueError:
            # Handle non-integer ID
            error_message = "Invalid product ID format."
            data = []

    # 3. Render Template
    # Pass the final list of data (filtered or full) and any error message
    return render_template(
        'product_display.html',
        products=data,
        error=error_message
    )

# --- Run Server ---

if __name__ == '__main__':
    app.run(debug=True, port=5000)
