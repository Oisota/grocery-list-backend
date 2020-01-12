from flask_login import UserMixin
from passlib.hash import bcrypt

from grocerylist.exts.sqla import db
from grocerylist.models.user import User

class UserService():
        
    @staticmethod
    def get_by_id(user_id):
        """Load user by id"""
        user = User.query.get(user_id)
        return user

    @staticmethod
    def validate(email, pwd):
        """Validate email and password"""
        user = User.query.filter_by(email=email).first()
        if user is None:
            return None

        if bcrypt.verify(pwd, user.hash):
            return user

        return None

    @staticmethod
    def register(email, pwd):
        """Register a new user"""
        hash_ = bcrypt.hash(pwd)
        user = User(email=email, hash=hash_)
        db.session.add(user)
        db.session.commit()
