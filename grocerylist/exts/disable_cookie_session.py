from flask.sessions import SecureCookieSessionInterface

class CustomSessionInterface(SecureCookieSessionInterface):
    """Prevent creating session from API requests."""
    def save_session(self, *args, **kwargs):
        return

class DisabledCookieSession:
    """Flask extensions for disabling cookie sessions"""
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.session_interface = CustomSessionInterface()

no_cookie_sessions = DisabledCookieSession()
