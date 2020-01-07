from flask import Flask

from grocerylist.exts import init_extensions
from grocerylist.api import api_blueprint
from grocerylist.errors import register_error_handlers

def create_app(config):
    app = Flask(__name__)

    app.config.from_mapping(config)

    init_extensions(app)

    register_error_handlers(app)

    app.register_blueprint(api_blueprint)

    return app
