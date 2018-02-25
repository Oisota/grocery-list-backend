from flask import Blueprint, jsonify, request, abort
from flask.views import MethodView
from flask_login import login_required
from flask_cors import CORS, cross_origin

from ..database import query_db, get_db, db_commit
from ..user import User
from .. import jws
from .decorators import jsonified

api_blueprint = Blueprint('grocerylist', __name__, url_prefix='/api')
CORS(api_blueprint)

@api_blueprint.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
@jsonified
def login():
    data = request.get_json()
    email = data['email']
    pwd = data['password']

    user = User.validate(email, pwd)
    if user is None:
        abort(404)

    token = jws.dumps({'id': user.id_})
    return dict(token=token.decode())

@api_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    pwd = data['password']
    User.register(email, pwd)
    return '', 201


class GroceryList(MethodView):

    decorators = [login_required, jsonified]

    def get(self):
        items = query_db('SELECT * FROM item;')
        return items

    def post(self):
        data = request.get_json()
        q = """
        INSERT INTO item (name, dollars, cents, checked)
        VALUES (:name, :dollars, :cents, :checked);
        """
        with db_commit() as cur:
            cur.execute(q, data)
            last_row_id = cur.lastrowid
        item = query_db('SELECT * FROM item WHERE rowid = ?;', (last_row_id,), True)
        return item


class GroceryListItem(MethodView):

    decorators = [login_required, jsonified]

    def get(self, item_id):
        item = query_db('SELECT * FROM item WHERE id = ?;', (item_id,), True)
        if item is None:
            return jsonify({'message': 'Not Found'}), 404
        return item

    def put(self, item_id):
        data = request.get_json()
        q = """
        UPDATE item
        SET name = :name, checked = :checked, dollars = :dollars, cents = :cents
        WHERE id = :id;
        """
        with db_commit() as cur:
            cur.execute(q, data)
        item = query_db('select * from item where id = ?;', (item_id,), True)
        return item

    def delete(self, item_id):
        with db_commit() as cur:
            cur.execute('DELETE FROM item WHERE id = ?;', (item_id,))
        return '', 200

api_blueprint.add_url_rule('/grocery-list/', view_func=GroceryList.as_view('grocerylist'))
api_blueprint.add_url_rule('/grocery-list/<item_id>', view_func=GroceryListItem.as_view('grocerylistitem'))
