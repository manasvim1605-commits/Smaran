from flask import Flask, render_template, jsonify, session, redirect, url_for

from routes.caregiver import caregiver_bp
from routes.player import player_bp

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

app.secret_key = "smaran-development-secret-change-before-deployment"

# Register API routes
app.register_blueprint(caregiver_bp)
app.register_blueprint(player_bp)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# LOGIN PAGES
@app.route("/caregiver-login")
def caregiver_login_page():
    return render_template("caregiver_login.html")


@app.route("/player-login")
def player_login_page():
    return render_template("player_login.html")


# REGISTRATION PAGES
@app.route("/caregiver-register")
def caregiver_register_page():
    return render_template("caregiver_register.html")


@app.route("/player-register")
def player_register_page():
    return render_template("player_register.html")


# DASHBOARDS
@app.route("/caregiver-dashboard")
def caregiver_dashboard():

    if session.get("role") != "caregiver":
        return redirect(url_for("caregiver_login_page"))

    return render_template("caregiver_dashboard.html")


@app.route("/player-home")
def player_home():

    if session.get("role") != "player":
        return redirect(url_for("player_login_page"))

    return render_template("player_home.html")


# LOGOUT
@app.route("/api/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({
        "message": "You have logged out!"
    }), 200


if __name__ == "__main__":
    app.run(debug=True)
