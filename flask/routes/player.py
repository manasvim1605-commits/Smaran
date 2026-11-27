
from flask import Blueprint, request, jsonify, session
from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash

player_bp = Blueprint("player", __name__)


# PLAYER REGISTRATION
@player_bp.route("/api/player/register", methods=["POST"])
def player_register():

    data = request.get_json() or {}

    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")
    password = data.get("password")
    caregiver_email = data.get("caregiver_email")

    if not all([name, email, password, caregiver_email]):
        return jsonify({"message": "Please fill all required fields"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Find caregiver
        cursor.execute(
            "SELECT caregiver_id FROM Caregiver WHERE email = %s",
            (caregiver_email,)
        )

        caregiver = cursor.fetchone()

        if not caregiver:
            return jsonify({
                "message": "Caregiver account not found"
            }), 404

        caregiver_id = caregiver[0]

        # Check whether email already exists
        cursor.execute(
            "SELECT user_id FROM Elderly_User WHERE email = %s",
            (email,)
        )

        if cursor.fetchone():
            return jsonify({
                "message": "Email already registered"
            }), 409

        hashed_password = generate_password_hash(password)

        query = """
        INSERT INTO Elderly_User
        (caregiver_id, full_name, phone, email, password)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query, (
            caregiver_id,
            name,
            phone or None,
            email,
            hashed_password
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


# PLAYER LOGIN
@player_bp.route("/api/player/login", methods=["POST"])
def player_login():

    data = request.get_json() or {}

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"message": "Enter email and password"}), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            "SELECT * FROM Elderly_User WHERE email = %s",
            (email,)
        )

        player = cursor.fetchone()

        if player and check_password_hash(
            player["password"], password
        ):
            session.clear()
            session["user_id"] = player["user_id"]
            session["role"] = "player"

            return jsonify({
                "message": "You have logged in!",
                "redirect": "/player-home"
            }), 200

        return jsonify({
            "message": "Invalid email or password"
        }), 401

    finally:
        cursor.close()
        connection.close()
