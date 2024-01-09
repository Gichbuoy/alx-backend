#!/usr/bin/env python3
"""
Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """configuration class for FLask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('1-app.Config')


@app.route('/', strict_slashes=False)
def index():
    """Render the index page.

    Returns:
        str: Rendered HTML page.
    """
    return render_template('1-index.html')
