from flask import Flask

app = Flask(__name__)

from . import config
app.config.from_object(config)

from .api import api_blueprint

app.register_blueprint(api_blueprint)
