#!/usr/bin/env python3
"""
Mock logging In
"""
from flask import Flask, request, g, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('5-app.Config')


@babel.localeselector
def get_locale():
    """force locale with parameters"""
    locale = request.args.get('locale', None)
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Get user details based on user ID.

    Args:
        user_id (int): User ID.

    Returns:
        dict or None: User details if found, otherwise None.
    """
    login_as = request.args.get("login_as", None)
    if login_as is None:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """Execute before all other functions.

    Sets the user as a global variable on flask.g.
    """
    g.user = get_user()


@app.route('/', strict_slashes=False)
def index():
    """Render the index page.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('5-index.html')
