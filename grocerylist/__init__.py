from flask import Flask, request
from itsdangerous import BadSignature

from .ext import login_manager
from .api import api_blueprint
from .user import User
from .util import jws, CustomSessionInterface
from .errors import register_error_handlers

def create_app(config):
    app = Flask(__name__)

    app.config.from_mapping(config)

    # Configure flask login
    login_manager.init_app(app)

    # disable cookie sessions
    app.session_interface = CustomSessionInterface()

    @app.before_request
    def test():
        print(request.url)

    @login_manager.request_loader
    def load_user_from_request(request):
        """Load user by parsing bearer token"""
        header = request.headers.get('Authorization')
        if header is None:
            return None

        try:
            type_, token = header.split(' ')
        except ValueError:
            return None

        if type_.lower() != 'bearer' or not token:
            return None

        try:
            data = jws.loads(token)
        except BadSignature as e:
            return None

        return User.get(int(data['id']))

    register_error_handlers(app)

    app.register_blueprint(api_blueprint)

    return app
