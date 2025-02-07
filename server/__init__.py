from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from .database import db, init_db
from .models import bcrypt
from .routes import register_routes  # Import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize database and migration
    init_db(app)
    bcrypt.init_app(app)
    Migrate(app, db)

    # Enable CORS
    CORS(app, supports_credentials=True)

    # Initialize Flask-RESTful API
    api = Api(app)

    # Register routes
    register_routes(api)

    # ✅ Define the root route separately
    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "Welcome to the Apple Store API!"}), 200

    return app

app = create_app()
