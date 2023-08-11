from flask import Flask
from app.main import bp as main_bp
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(main_bp)
    return app
