#!/usr/bin/python3
"""
A Flask application that loads data from a JSON file and renders it
dynamically using Jinja loops and conditional statements.
"""
from flask import Flask, render_template
import json
import os

# Instantiate the Flask application
app = Flask(__name__)

# --- Routes ---

@app.route('/')
def home():
    """Renders the index.html template (Home page)."""
    return render_template('index.html')

@app.route('/items')
def items():
    """
    Reads item data from items.json and renders items.html,
    passing the list of items to the template.
    """
    # Define the path to the items.json file
    json_file_path = os.path.join(os.path.dirname(__file__), 'items.json')
    items_list = []

    # Read data from items.json
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
            # Ensure 'items' key exists and is a list
            items_list = data.get('items', [])
            if not isinstance(items_list, list):
                items_list = []
    except FileNotFoundError:
        print(f"Error: {json_file_path} not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {json_file_path}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Render the template, passing the list of items
    return render_template('items.html', items=items_list)

# (Optional: Include other routes from Task 01 here if required for completeness)
# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')


# --- Run Server ---

if __name__ == '__main__':
    app.run(debug=True, port=5000)
