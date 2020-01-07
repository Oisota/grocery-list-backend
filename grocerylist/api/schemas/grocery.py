from grocerylist.exts.marshmallow import ma

class GroceryItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'dolars', 'cents', 'checked')


grocery_item_schema = GroceryItemSchema()
grocery_items_schema = GroceryItemSchema(many=True)
