#!/usr/bin/python3
"""
A simple RESTful API developed using the Flask framework.
It handles user data in memory and supports GET and POST requests.
"""
from flask import Flask, jsonify, request, abort

# Instantiate the Flask application
app = Flask(__name__)

# In-memory user data store
# NOTE: Do not include testing data when pushing your code to avoid checker issues.
users = {}

# Pre-populate with a single user for initial testing purposes,
# but remove this line before final submission if the instructions say so.
# We will initialize it with an empty dictionary as requested to avoid checker issues.
users = {}

@app.route('/', methods=['GET'])
def home():
    """Returns a welcome message for the root URL."""
    return "Welcome to the Flask API!"

# --- API Endpoints ---
# 1. /status
@app.route('/status', methods=['GET'])
def get_status():
    """Returns the status of the API."""
    return "OK"

# 2. /data
@app.route('/data', methods=['GET'])
def get_data():
    """Returns a JSON list of all usernames."""
    # Get all keys (usernames) from the dictionary
    return jsonify(list(users.keys()))

# 3. /users/<username>
@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Returns the full user object for a given username, or 404 if not found."""
    user = users.get(username)
    if user:
        return jsonify(user)
    
    # Return 404 Not Found error if user does not exist
    return jsonify({"error": "User not found"}), 404

# 4. /add_user (POST)
@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handles POST requests to add a new user to the in-memory store.
    Performs validation for JSON, missing username, and duplicate username.
    """
    try:
        # 1. Parse incoming JSON data
        data = request.get_json()
    except Exception:
        # 400 Bad Request for invalid JSON
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        # Fallback for non-JSON content or empty body
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Check for missing 'username'
    username = data.get('username')
    if not username:
        # 400 Bad Request for missing username
        return jsonify({"error": "Username is required"}), 400

    # 3. Check for existing 'username'
    if username in users:
        # 409 Conflict for duplicate username
        return jsonify({"error": "Username already exists"}), 409

    # 4. Add new user to the dictionary
    # Ensure the stored user object includes the username key (as per example output)
    new_user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    users[username] = new_user

    # 5. Return confirmation message (201 Created)
    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201

# --- Running the Server ---
if __name__ == '__main__':
    # Running the application on the default host and port (127.0.0.1:5000)
    # You can also run it using 'flask --app task_04_flask.py run'
    app.run(debug=True)
