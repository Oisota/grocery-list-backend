from flask import g
from flask.views import MethodView
from flask_login import login_required

from grocerylist.api import validators
from grocerylist.api.decorators import jsonified, schema
from grocerylist.services.grocery import GroceryService
from grocerylist.api.schemas.grocery import grocery_item_schema, grocery_items_schema

class Groceries(MethodView):

    decorators = [login_required, jsonified]

    def get(self):
        items = GroceryService.all()
        return grocery_items_schema.dump(items)

    @schema(validators.GroceryItem())
    def post(self):
        data = g.request_data
        item = GroceryService.create(data)
        return grocery_item_schema.dump(item)

class GroceryItem(MethodView):

    decorators = [login_required, jsonified]

    @schema(validators.GroceryItem())
    def put(self, item_id):
        data = g.request_data
        data['id'] = item_id
        item = GroceryService.update(data)
        return grocery_item_schema.dump(item)

    def delete(self, item_id):
        GroceryService.delete({'item_id': item_id})
        return '', 200
