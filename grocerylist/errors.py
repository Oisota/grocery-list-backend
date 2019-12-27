from flask import jsonify
from werkzeug.exceptions import HTTPException

def handle_http_exception(error):
    res = {}
    res['error'] = error.description
    resp = jsonify(res)
    resp.status_code = error.code
    return resp

def register_error_handlers(app):
    """Register error handlers on the app"""
    app.register_error_handler(HTTPException, handle_http_exception)
