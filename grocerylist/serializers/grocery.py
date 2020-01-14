from grocerylist.exts.marshmallow import ma

class GroceryItemSerializer(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'dolars', 'cents', 'checked')

grocery_item_serializer = GroceryItemSerializer()
grocery_items_serializer = GroceryItemSerializer(many=True)
