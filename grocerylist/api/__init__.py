from .auth import bp as auth_bp
from .grocery import bp as grocery_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(grocery_bp)
