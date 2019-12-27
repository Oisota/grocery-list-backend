"""setup flask extensions"""

from flask_login import LoginManager

from .util import jws
from .user import User

login_manager = LoginManager()

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

def init_extensions(app):
    """initialize extensions on app"""
    login_manager.init_app(app)
