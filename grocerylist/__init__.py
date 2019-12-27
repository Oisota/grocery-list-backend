from flask import Flask, request
from itsdangerous import BadSignature

from .ext import init_extensions
from .api import api_blueprint
from .util import CustomSessionInterface
from .errors import register_error_handlers

def create_app(config):
    app = Flask(__name__)

    app.config.from_mapping(config)

    init_extensions(app)

    # disable cookie sessions
    app.session_interface = CustomSessionInterface()

    register_error_handlers(app)

    app.register_blueprint(api_blueprint)

    return app
