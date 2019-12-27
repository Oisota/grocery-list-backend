from flask import jsonify
from werkzeug.exceptions import HTTPException
from marshmallow.exceptions import ValidationError

def handle_http_exception(error):
    res = {}
    res['error'] = error.description
    resp = jsonify(res)
    resp.status_code = error.code
    return resp

def handle_validation_error(error):
    res = {}
    res['error'] = error.messages
    resp = jsonify(res)
    resp.status_code = 400
    return resp

def register_error_handlers(app):
    """Register error handlers on the app"""
    app.register_error_handler(HTTPException, handle_http_exception)
    app.register_error_handler(ValidationError, handle_validation_error)
