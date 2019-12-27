from flask.sessions import SecureCookieSessionInterface
from itsdangerous import JSONWebSignatureSerializer

from .settings import config

jws = JSONWebSignatureSerializer(config['SECRET_KEY'])

class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""
    def save_session(self, *args, **kwargs):
        return
