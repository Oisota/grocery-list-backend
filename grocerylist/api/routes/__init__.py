from flask import Blueprint

from . import auth
from . import groceries

bp = Blueprint('grocerylist', __name__, url_prefix='/api')

bp.add_url_rule('/auth/login', view_func=auth.login, methods=['POST'])
bp.add_url_rule('/auth/register', view_func=auth.register, methods=['POST'])
bp.add_url_rule('/groceries', view_func=groceries.Groceries.as_view('grocerylist'))
bp.add_url_rule('/groceries/<item_id>', view_func=groceries.GroceryItem.as_view('grocerylistitem'))
