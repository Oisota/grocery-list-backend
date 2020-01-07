"""Flask Login Init"""
from flask_login import LoginManager

from grocerylist.util import jws
from grocerylist.api.services.user import UserService

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

    return UserService.get_by_id(int(data['id']))
