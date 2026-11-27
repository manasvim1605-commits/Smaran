from flask import Blueprint, request, jsonify, session
from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

caregiver_bp = Blueprint("caregiver", __name__)


# CAREGIVER REGISTRATION
@caregiver_bp.route("/api/caregiver/register", methods=["POST"])
def caregiver_register():

    data = request.get_json() or {}

    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")
    password = data.get("password")

    if not all([name, phone, email, password]):
        return jsonify({"message": "Please fill all fields"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT caregiver_id FROM Caregiver WHERE email = %s",
            (email,)
        )

        if cursor.fetchone():
            return jsonify({"message": "Email already registered"}), 409

        hashed_password = generate_password_hash(password)

        query = """
        INSERT INTO Caregiver (name, phone, email, password)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (
            name, phone, email, hashed_password
        ))

        connection.commit()

        return jsonify({
            "message": "Registration successful!"
        }), 201

    except Exception:
        connection.rollback()
        return jsonify({"message": "Registration failed. Please try again."}), 500

    finally:
        cursor.close()
        connection.close()


# CAREGIVER LOGIN
@caregiver_bp.route("/api/caregiver/login", methods=["POST"])
def caregiver_login():

    data = request.get_json() or {}

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Enter email and password"}), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM Caregiver WHERE email = %s",
            (email,)
        )

        caregiver = cursor.fetchone()

        if caregiver and check_password_hash(
            caregiver["password"], password
        ):
            session.clear()
            session["caregiver_id"] = caregiver["caregiver_id"]
            session["role"] = "caregiver"

            return jsonify({
                "message": "You have logged in!",
                "redirect": "/caregiver-dashboard"
            }), 200

        return jsonify({
            "message": "Invalid email or password"
        }), 401

    finally:
        cursor.close()
        connection.close() 