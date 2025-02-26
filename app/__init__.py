from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from app.config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    swagger = Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "API Documentation",
            "description": "API documentation for Flask app",
            "version": "1.0.0"
        }
    })

    from app.routes import blueprint
    app.register_blueprint(blueprint)

    return app

from app.models import Transaction  # Thêm dòng này

