from grocerylist.exts.sqla import db

class GroceryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    checked = db.Column(db.Boolean, nullable=False)
    dollars = db.Column(db.Integer, nullable=False)
    cents = db.Column(db.Integer, nullable=False)
