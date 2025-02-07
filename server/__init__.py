from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from .database import db, init_db 
from .models import bcrypt

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")


    init_db(app) 
    bcrypt.init_app(app)
    Migrate(app, db)

    CORS(app, supports_credentials=True)

    api = Api(app)

    
    from .routes import register_routes
    register_routes(api)  

    return app

app = create_app()
