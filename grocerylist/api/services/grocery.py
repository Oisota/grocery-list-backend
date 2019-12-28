"""Grocery Service Module"""

from ... import database as db

class GroceryService:
    """Grocery list CRUD operations"""

    @staticmethod
    def all():
        """Return all items"""
        q = """
        SELECT
            id,
            name,
            dollars,
            cents,
            checked
        FROM item;
        """
        items = db.query(q)
        return items

    @staticmethod
    def create(data):
        q = """
        INSERT INTO item (name, dollars, cents, checked)
        VALUES (:name, :dollars, :cents, :checked);
        """
        with db.commit() as cur:
            cur.execute(q, data)
            last_row_id = cur.lastrowid
        item = db.query('SELECT * FROM item WHERE rowid = ?;', (last_row_id,), True)
        return item

    @staticmethod
    def update(data):
        q = """
        UPDATE item
        SET name = :name, checked = :checked, dollars = :dollars, cents = :cents
        WHERE id = :item_id;
        """
        with db.commit() as cur:
            cur.execute(q, data)
        item = db.query('SELECT * FROM item WHERE id = :item_id;', data, True)
        return item

    @staticmethod
    def delete(data):
        with db.commit() as cur:
            cur.execute('DELETE FROM item WHERE id = :item_id;', data)
