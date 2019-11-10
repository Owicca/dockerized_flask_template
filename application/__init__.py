from flask import Flask

from .config import Config


def create_app():
    app = Flask(__name__,
                template_folder="templates",
                static_folder="static")
    app.config.from_object(Config())

    with app.app_context():
        from . import routes
        return app
