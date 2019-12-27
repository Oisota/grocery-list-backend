from functools import wraps

from flask import jsonify

def jsonified(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data = f(*args, **kwargs)
        if not (isinstance(data, dict) or isinstance(data, list)):
            return data
        return jsonify(data)
    return decorated
