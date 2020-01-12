"""setup flask extensions"""
from grocerylist.exts.sqla import db
from grocerylist.exts.marshmallow import ma
from grocerylist.exts.login import login_manager
from grocerylist.exts.disable_cookie_session import no_cookie_sessions
from grocerylist.exts.admin import admin
from grocerylist.exts.migrate import migrate
from grocerylist.exts.limiter import limiter
from grocerylist.exts.cache import cache

def init_extensions(app):
    """initialize extensions on app"""
    login_manager.init_app(app)
    ma.init_app(app)
    db.init_app(app)
    no_cookie_sessions.init_app(app)
    admin.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)
    cache.init_app(app)
