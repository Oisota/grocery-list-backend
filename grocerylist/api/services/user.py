from flask_login import UserMixin
from passlib.hash import bcrypt

from ... import database as db

class User(UserMixin):

    def __init__(self, *args, **kwargs):
        self.email = kwargs['email']
        self.id_ = kwargs['id']
        
    @classmethod
    def by_id(cls, user_id):
        """Load user by id"""
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
        """Validate email and password"""
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
        """rEgister a new user"""
        hash_ = bcrypt.hash(pwd)
        q = '''
        INSERT INTO user (email, hash)
        VALUES (?, ?);
        '''
        with db.commit() as cur:
            cur.execute(q, (email, hash_))
