from functools import wraps

from flask import jsonify, request, g

def jsonified(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data = f(*args, **kwargs)
        if not (isinstance(data, dict) or isinstance(data, list)):
            return data
        return jsonify(data)
    return decorated

def schema(s):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
           g.request_data = s.load(request.json)
           return f(*args, **kwargs)
        return decorated
    return decorator
