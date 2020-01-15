from flask import Blueprint

from .groceries import Groceries, GroceryItem

bp = Blueprint('grocerylist', __name__, url_prefix='/api')

bp.add_url_rule('/groceries', view_func=Groceries.as_view('grocerylist'))
bp.add_url_rule('/groceries/<item_id>', view_func=GroceryItem.as_view('grocerylistitem'))
