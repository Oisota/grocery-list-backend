from itsdangerous import JSONWebSignatureSerializer

from .settings import config

jws = JSONWebSignatureSerializer(config['SECRET_KEY'])
