from flask import g
from flask.views import MethodView
from flask_login import login_required

from .. import schemas
from ... import database as db
from ..decorators import jsonified, schema
from ..services.grocery import GroceryService

class Groceries(MethodView):

    decorators = [login_required, jsonified]

    def get(self):
        return GroceryService.all()

    @schema(schemas.GroceryItem())
    def post(self):
        data = g.request_data
        item = GroceryService.create(data)
        return item

class GroceryItem(MethodView):

    decorators = [login_required, jsonified]

    @schema(schemas.GroceryItem())
    def put(self, item_id):
        data = g.request_data
        data['item_id'] = item_id
        item = GroceryService.update(data)
        return item

    def delete(self, item_id):
        GroceryService.delete({'item_id': item_id})
        return '', 200
