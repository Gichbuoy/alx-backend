#!/usr/bin/env python3
"""
Force locale with URL parameter
"""
from flask import Flask, request, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configuration class for Flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('4-app.Config')


@babel.localeselector
def get_locale():
    """Determine the best-matching language for the user.

    Returns:
        str: The best-matching language code.
    """
    locale = request.args.get('locale', None)
    if locale is not None and locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Render the index page.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('4-index.html')
