from flask_login import UserMixin
from passlib.hash import bcrypt

from . import database as db

class User(UserMixin):

    def __init__(self, *args, **kwargs):
        self.email = kwargs['email']
        self.id_ = kwargs['id']
        
    @classmethod
    def get(cls, user_id):
        q = '''
        SELECT *
        FROM user
        WHERE id = ?;
        '''
        user = db.query(q, (user_id,), True)
        if user is None:
            return None
        return cls(**user)

    @classmethod
    def validate(cls, email, pwd):
        q = '''
        SELECT *
        FROM user
        WHERE email = ?;
        '''
        user = db.query(q, (email,), True)
        if user is None:
            return None

        if bcrypt.verify(pwd, user['hash']):
            return cls(**user)

        return None

    @classmethod
    def register(cls, email, pwd):
        hash_ = bcrypt.hash(pwd)
        q = '''
        INSERT INTO user (email, hash)
        VALUES (?, ?);
        '''
        with db.commit() as cur:
            cur.execute(q, (email, hash_))
