from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)#este es el objeto osbre el cual configuramos la lave secreta

    return app
