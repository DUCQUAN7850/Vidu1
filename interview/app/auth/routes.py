from flask import Blueprint, request, jsonify, current_app, g
from werkzeug.security import generate_password_hash, check_password_hash
from app.database import db
from app.models import User
from app.schemas import UserSchema
from app.auth.utils import create_access_token
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from datetime import timedelta
import re

auth_bp = Blueprint("auth", __name__)
user_schema = UserSchema()


@auth_bp.route("/", methods=["GET"])
def ping():
    return jsonify({"message": "okela"}), 201


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    print("--11111111111")
    # Required fields check
    required_fields = ["username", "password", "email"]
    for field in required_fields:
        if field not in data or not data[field].strip():
            return jsonify({"message": f"{field.capitalize()} is required"}), 400

    username = data["username"]
    password = data["password"]
    email = data["email"]
    print("---2222222222222", email, username, password)
    # Username validation
    if not re.match("^[a-zA-Z0-9]+$", username):
        return jsonify({"message": "Username must consist of letters and numbers only"}), 400
    if not (5 <= len(username) <= 20):
        return jsonify({"message": "Username length must be between 5 and 20 characters"}), 400
    print("------3333333333")
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Username already exists"}), 400
    print("-----35555555")
    # Password validation
    if not (8 <= len(password) <= 20):
        return jsonify({"message": "Password length must be between 8 and 20 characters"}), 400
    if not re.search("[A-Z]", password):
        return jsonify({"message": "Password must contain at least one uppercase letter"}), 400
    if not re.search("[a-z]", password):
        return jsonify({"message": "Password must contain at least one lowercase letter"}), 400
    if not re.search("[0-9]", password):
        return jsonify({"message": "Password must contain at least one number"}), 400
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return jsonify({"message": "Password must contain at least one special character"}), 400
    print("-----44444444444444")
    # Email validation
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        return jsonify({"message": "Invalid email format"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 400
    print("----okela")
    return jsonify({"message": "okela"}), 201
    # Create new user
    # hashed_password = generate_password_hash(password)
    # new_user = User(username=username, hashed_password=hashed_password, email=email)
    # db.session.add(new_user)
    # db.session.commit()

    # return user_schema.dump(new_user), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    app = current_app
    session = g.get('session')
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    remember_me = data.get("remember_me", False)

    # Try to find user by username or email
    user = None
    if username:
        user = User.query.filter_by(username=username).first()
    elif email:
        user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.hashed_password, password):
        return jsonify({"message": "Invalid credentials"}), 401

    # Login successful, generate access token
    payload = {"user_id": user.id}
    serializer = Serializer(app.config['SECRET_KEY'], expires_delta=timedelta(days=30) if remember_me else None)
    token = serializer.dumps(payload)

    # Set user info in session for display
    session['username'] = user.username
    session['email'] = user.email

    return jsonify({"access_token": token}), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    return jsonify({"message": "Logged out successfully"}), 200
