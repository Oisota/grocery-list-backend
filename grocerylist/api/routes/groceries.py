from flask import g
from flask.views import MethodView
from flask_login import login_required

from grocerylist.api import validators
from grocerylist.api.decorators import jsonified, schema
from grocerylist.services.grocery import GroceryService
from grocerylist.serializers.grocery import grocery_item_serializer, grocery_items_serializer

class Groceries(MethodView):

    decorators = [login_required, jsonified]

    def get(self):
        items = GroceryService.all()
        return grocery_items_serializer.dump(items)

    @schema(validators.GroceryItem())
    def post(self):
        data = g.request_data
        item = GroceryService.create(data)
        return grocery_item_serializer.dump(item)

class GroceryItem(MethodView):

    decorators = [login_required, jsonified]

    @schema(validators.GroceryItem())
    def put(self, item_id):
        data = g.request_data
        data['id'] = item_id
        item = GroceryService.update(data)
        return grocery_item_serializer.dump(item)

    def delete(self, item_id):
        GroceryService.delete({'item_id': item_id})
        return '', 200
