from flask_login import UserMixin
from passlib.hash import bcrypt

from .database import query_db, get_db

class User(UserMixin):

    def __init__(self, *args, **kwargs):
        self.email = kwargs['email']
        self.id_ = kwargs['id']
        
    @classmethod
    def get(cls, user_id):
        user = query_db('SELECT * FROM user WHERE id = ?;', (user_id,), True)
        if user is None:
            return None
        return cls(**user)

    @classmethod
    def validate(cls, email, pwd):
        user = query_db('SELECT * FROM user WHERE email = ?;', (email,), True)
        if user is None:
            return None

        if bcrypt.verify(pwd, user['hash']):
            return cls(**user)

        return None

    @classmethod
    def register(cls, email, pwd):
        hash_ = bcrypt.hash(pwd)
        db = get_db()
        cur = db.cursor()
        cur.execute('INSERT INTO user (email, hash) VALUES (?, ?);', (email, hash_))
        db.commit()
