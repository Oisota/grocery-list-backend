from flask import jsonify, request, abort
from flask.views import MethodView
from flask_login import login_required
from werkzeug.exceptions import NotFound

from .. import database as db
from ..user import User
from ..util import jws
from .decorators import jsonified

@jsonified
def login():
    data = request.get_json()
    email = data['email']
    pwd = data['password']

    user = User.validate(email, pwd)
    if user is None:
        raise NotFound('Invalid Credentials')

    token = jws.dumps({'id': user.id_})
    return dict(token=token.decode())

def register():
    data = request.get_json()
    email = data['email']
    pwd = data['password']
    User.register(email, pwd)
    return '', 201


class Groceries(MethodView):

    decorators = [login_required, jsonified]

    def get(self):
        q = """
        SELECT
            id,
            name,
            dollars,
            cents,
            checked
        FROM item;
        """
        items = db.query(q)
        return items

    def post(self):
        data = request.get_json()
        q = """
        INSERT INTO item (name, dollars, cents, checked)
        VALUES (:name, :dollars, :cents, :checked);
        """
        with db.commit() as cur:
            cur.execute(q, data)
            last_row_id = cur.lastrowid
        item = db.query('SELECT * FROM item WHERE rowid = ?;', (last_row_id,), True)
        return item


class GroceryItem(MethodView):

    decorators = [login_required, jsonified]

    def put(self, item_id):
        data = request.get_json()
        q = """
        UPDATE item
        SET name = :name, checked = :checked, dollars = :dollars, cents = :cents
        WHERE id = :id;
        """
        data['id'] = item_id
        with db.commit() as cur:
            cur.execute(q, data)
        item = db.query('SELECT * FROM item WHERE id = ?;', (item_id,), True)
        return item

    def delete(self, item_id):
        with db.commit() as cur:
            cur.execute('DELETE FROM item WHERE id = ?;', (item_id,))
        return '', 200
