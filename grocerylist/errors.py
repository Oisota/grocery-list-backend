from flask import jsonify
from werkzeug import exceptions

from . import app, login_manager

class AppError(Exception):

    def __init__(self, status_code=500, message='An error occurred'):
        self.status_code = status_code
        self.message = message

    def to_response(self):
        res = {}
        res['message'] = self.message
        resp = jsonify(res)
        resp.status_code = self.status_code
        return resp


@app.errorhandler(AppError)
def handle_app_error(error):
    return error.to_response()

@login_manager.unauthorized_handler
def handle_unauthorized():
    res = {}
    res['message'] = 'You are not authorized'
    resp = jsonify(res)
    resp.status_code = 401
    return resp

@app.errorhandler(exceptions.HTTPException)
def handle_error(error):
    res = {}
    res['message'] = error.description
    resp = jsonify(res)
    resp.status_code = error.code
    return resp
