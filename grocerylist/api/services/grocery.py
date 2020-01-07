"""Grocery Service Module"""

from grocerylist.exts.sqla import db
from grocerylist.api.models.groceries import GroceryItem

class GroceryService:
    """Grocery list CRUD operations"""

    @staticmethod
    def all():
        """Return all items"""
        return GroceryItem.query.all()

    @staticmethod
    def create(data):
        """Create a new item"""
        item = GroceryItem(**data)
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def update(data):
        """Update existing item"""
        item = GroceryItem.query.get(data['id'])
        for k, v in data.items():
            setattr(item, k, v)
        db.session.commit()
        return item

    @staticmethod
    def delete(data):
        """Delete existing item"""
        item = GroceryItem(**data)
        db.session.delete(item)
        db.session.commit()
