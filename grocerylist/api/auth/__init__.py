from flask import Blueprint

from .auth import login, register

bp = Blueprint('auth', __name__, url_prefix='/api')

bp.add_url_rule('/auth/login', view_func=login, methods=['POST'])
bp.add_url_rule('/auth/register', view_func=register, methods=['POST'])
