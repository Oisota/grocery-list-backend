from flask import jsonify, request
from flask.views import MethodView

from . import app

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Grocery List API'})

@app.route('/grocery-list/', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] )
def grocery_list():
    if request.method == 'GET':
        return jsonify(['this', 'is', 'a', 'test'])
#    elif request.method == 'POST':
#        pass
#    elif request.method == 'PUT':
#        pass
#    elif request.method == 'PATCH':
#        pass
#    elif request.method == 'DELETE':
#        pass

@app.route('/grocery-list/<item_id>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'] )
def grocery_list_item(item_id):
    if request.method == 'GET':
        return jsonify({'item': 'turkey'})
