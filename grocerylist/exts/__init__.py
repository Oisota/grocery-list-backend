"""setup flask extensions"""
from grocerylist.exts.sqla import db
from grocerylist.exts.marshmallow import ma
from grocerylist.exts.login import login_manager
from grocerylist.exts.disable_cookie_session import no_cookie_sessions

def init_extensions(app):
    """initialize extensions on app"""
    login_manager.init_app(app)
    ma.init_app(app)
    db.init_app(app)
    no_cookie_sessions.init_app(app)
