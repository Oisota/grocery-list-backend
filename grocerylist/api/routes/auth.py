from flask import g
from werkzeug.exceptions import NotFound

from grocerylist.api.decorators import jsonified, schema
from grocerylist.util import jws
from grocerylist.services.user import UserService
from grocerylist.api import validators

@schema(validators.UserCreds())
@jsonified
def login():
    data = g.request_data
    email = data['email']
    pwd = data['password']

    user = UserService.validate(email, pwd)
    if user is None:
        raise NotFound('Invalid Credentials')

    token = jws.dumps({'id': user.id})
    return dict(token=token.decode())

@schema(validators.UserCreds())
def register():
    data = g.request_data
    email = data['email']
    pwd = data['password']
    UserService.register(email, pwd)
    return '', 201
