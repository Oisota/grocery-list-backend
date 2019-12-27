from flask import g
from werkzeug.exceptions import NotFound

from ..decorators import jsonified, schema
from ...util import jws
from ...user import User
from .. import schemas

@schema(schemas.UserCreds())
@jsonified
def login():
    data = g.request_data
    email = data['email']
    pwd = data['password']

    user = User.validate(email, pwd)
    if user is None:
        raise NotFound('Invalid Credentials')

    token = jws.dumps({'id': user.id_})
    return dict(token=token.decode())

@schema(schemas.UserCreds())
def register():
    data = g.request_data
    email = data['email']
    pwd = data['password']
    User.register(email, pwd)
    return '', 201
