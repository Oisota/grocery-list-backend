from flask import jsonify, request, abort
from flask.views import MethodView

from . import app
from .database import query_db, get_db

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the Grocery List API'})

@app.route('/grocery-list/', methods=['GET', 'POST'] )
def grocery_list():
    if request.method == 'GET':
        items = query_db('SELECT * FROM item')
        return jsonify(items)
    elif request.method == 'POST':
        data = {
                'name': request.json['name'],
                'checked': request.json['checked'],
                'dollars': request.json['dollars'],
                'cents': request.json['cents']
                }
        con = get_db()
        cur = con.cursor()
        cur.execute('INSERT INTO item (name, dollars, cents, checked) VALUES (:name, :dollars, :cents, :checked)', data)
        con.commit()
        item = query_db('SELECT * FROM item WHERE rowid = ?', (cur.lastrowid,), True)
        return jsonify(item)

@app.route('/grocery-list/<item_id>', methods=['GET', 'PUT', 'DELETE'] )
def grocery_list_item(item_id):
    if request.method == 'GET':
        item = query_db('SELECT * FROM item WHERE id = ?;', (item_id,), True)
        if item is None:
            return jsonify({'message': 'Not Found'}), 404
        return jsonify(item)
    elif request.method == 'PUT':
        data = {
                'name': request.json['name'],
                'checked': request.json['checked'],
                'dollars': request.json['dollars'],
                'cents': request.json['cents']
                }
        
        con = get_db()
        cur = con.cursor()
        cur.execute("""
                UPDATE item 
                SET name = :name, checked = :checked, dollars = :dollars, cents = :cents 
                WHERE id = :id;""", data)
        con.commit()
        item = query_db('select * from item where id = ?;', (item_id,), True)
        return jsonify(item)
    elif request.method == 'DELETE':
        con = get_db()
        cur = con.cursor()
        cur.execute('DELETE FROM item WHERE id = ?', (item_id,))
        con.commit()
        return '', 200
