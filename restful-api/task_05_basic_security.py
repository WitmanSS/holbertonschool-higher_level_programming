#!/usr/bin/python3
"""
A Flask API demonstrating Basic Authentication and JWT-based Token Authentication
with Role-Based Access Control (RBAC).
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt,
    JWTManager
)

# --- Initialization ---
app = Flask(__name__)
auth = HTTPBasicAuth()

# Configure JWT
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this in production!
jwt = JWTManager(app)

# --- In-Memory User Data Store ---
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# --- JWT Error Handlers (Ensuring 401 response for all auth errors) ---
@jwt.unauthorized_loader
@jwt.invalid_token_loader
@jwt.expired_token_loader
@jwt.revoked_token_loader
@jwt.needs_fresh_token_loader
def handle_auth_error(err):
    """Handle all JWT authentication errors with a 401 status."""
    return jsonify({"error": "Missing or invalid token"}), 401

# --- Basic Authentication Implementation ---
@auth.verify_password
def verify_password(username, password):
    """Callback function for verifying Basic Auth credentials."""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

# --- Basic Auth Protected Route ---
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"

# --- JWT Authentication: Login Route ---
@app.route('/login', methods=['POST'])
def login():
    """Authenticates user and returns a JWT access token."""
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data.get('username')
    password = data.get('password')

    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        # Create token, embedding the role in the 'additional_claims' payload
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)
    else:
        # Note: Flask-JWT-Extended handles the 401 for token issues,
        # but here we return 401 for failed login attempt.
        return jsonify({"error": "Invalid credentials"}), 401

# --- JWT Protected Route ---
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    # identity = get_jwt_identity() # Retrieves the identity (username) from the token
    return "JWT Auth: Access Granted"

# --- Role-Based Access Control (RBAC) Protected Route ---
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """Route protected by JWT Authentication with an Admin role check."""
    # Retrieve the custom claims (which includes the role)
    claims = get_jwt()
    
    if claims.get("role") == "admin":
        return "Admin Access: Granted"
    else:
        # 403 Forbidden response for unauthorized role
        return jsonify({"error": "Admin access required"}), 403

# --- Running the Server ---
if __name__ == '__main__':
    # Initialize the users dictionary with hashed passwords
    # Ensure this runs when starting the script directly
    users = {
        "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
        "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
    }
    app.run(debug=True)
