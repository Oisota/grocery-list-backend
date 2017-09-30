from flask import Blueprint, jsonify, request, abort
from flask.views import MethodView

from ..database import query_db, get_db

api_blueprint = Blueprint('grocerylist', __name__, url_prefix='/grocery-list')

class GroceryList(MethodView):

    def get(self):
        items = query_db('SELECT * FROM item')
        return jsonify(items)

    def post(self):
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


class GroceryListItem(MethodView):

    def get(self, item_id):
        item = query_db('SELECT * FROM item WHERE id = ?;', (item_id,), True)
        if item is None:
            return jsonify({'message': 'Not Found'}), 404
        return jsonify(item)

    def put(self, item_id):
        data = {
                'id': request.json['id'],
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

    def delete(self, item_id):
        con = get_db()
        cur = con.cursor()
        cur.execute('DELETE FROM item WHERE id = ?', (item_id,))
        con.commit()
        return '', 200

api_blueprint.add_url_rule('/', view_func=GroceryList.as_view('grocerylist'))
api_blueprint.add_url_rule('/<item_id>', view_func=GroceryListItem.as_view('grocerylistitem'))
