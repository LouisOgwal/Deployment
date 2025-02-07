from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from .database import db, init_db  # Import database initialization
from .models import bcrypt

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize database and migration
    init_db(app)  # Calls db.init_app(app) inside
    bcrypt.init_app(app)
    Migrate(app, db)

    # Enable CORS with credentials support
    CORS(app, supports_credentials=True)

    # Initialize Flask-RESTful API
    api = Api(app)

    # Register routes
    from .routes import register_routes
    register_routes(api)  

    return app

app = create_app()
