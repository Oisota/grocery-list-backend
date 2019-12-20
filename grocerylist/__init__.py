from flask import Flask
from flask_login import LoginManager
from itsdangerous import JSONWebSignatureSerializer, BadSignature


app = Flask(__name__)

from . import config
app.config.from_object(config)

from .user import User

jws = JSONWebSignatureSerializer(app.config['SECRET_KEY'])

# Configure flask login
login_manager = LoginManager()
login_manager.init_app(app)

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

from .api import api_blueprint
from . import errors

app.register_blueprint(api_blueprint)
