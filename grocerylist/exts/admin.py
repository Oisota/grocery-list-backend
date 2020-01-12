from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from grocerylist.exts.sqla import db
from grocerylist.models.user import User
from grocerylist.models.groceries import GroceryItem

admin = Admin(name='Grocery List', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(GroceryItem, db.session))
