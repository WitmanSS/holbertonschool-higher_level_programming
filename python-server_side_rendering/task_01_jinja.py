#!/usr/bin/python3
"""
A basic Flask application that renders multiple HTML pages using Jinja2
templates and demonstrates the use of reusable components.
"""
from flask import Flask, render_template

# Instantiate the Flask application
app = Flask(__name__)

# --- Routes ---

@app.route('/')
def home():
    """Renders the index.html template (Home page)."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about.html template (About Us page)."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact.html template (Contact Us page)."""
    return render_template('contact.html')

# --- Run Server ---

if __name__ == '__main__':
    # Run the application on port 5000 as specified
    app.run(debug=True, port=5000)
