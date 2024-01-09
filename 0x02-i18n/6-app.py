#!/usr/bin/env python3
"""
User locale
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
    """configururation class for FLask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('6-app.Config')


@babel.localeselector
def get_locale():
    """Determine the best-matching language for the user.

    Returns:
        str: The best-matching language code.
    """
    locale = request.args.get('locale', None)
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    login_as = request.args.get("login_as", None)
    if login_as is not None:
        local_lang = users[int(login_as)]['locale']
    if login_as is not None and local_lang in app.config["LANGUAGES"]:
        return local_lang
    if request.headers.get('locale') in app.config['LANGUAGES']:
        return request.headers.get('locale')
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
    return render_template('6-index.html')
