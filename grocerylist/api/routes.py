from flask import Blueprint

from . import views

bp = Blueprint('grocerylist', __name__, url_prefix='/api')

bp.add_url_rule('/auth/login', view_func=views.login, methods=['POST'])
bp.add_url_rule('/auth/register', view_func=views.register, methods=['POST'])
bp.add_url_rule('/groceries', view_func=views.Groceries.as_view('grocerylist'))
bp.add_url_rule('/groceries/<item_id>', view_func=views.GroceryItem.as_view('grocerylistitem'))
