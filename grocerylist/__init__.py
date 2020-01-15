from flask import Flask

from grocerylist.exts import init_extensions
from grocerylist.api import register_blueprints
from grocerylist.errors import register_error_handlers

def create_app(config):
    app = Flask(__name__)

    app.config.from_mapping(config)

    init_extensions(app)

    register_error_handlers(app)

    register_blueprints(app)

    return app
