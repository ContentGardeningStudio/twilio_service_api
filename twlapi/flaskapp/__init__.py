'''
@author: A. Ayeva
'''
#!/usr/bin/env python3

import os
from flask import Flask

from flask import render_template

from flask_bootstrap import Bootstrap
from .config import app_config

from string import Template
from werkzeug.utils import redirect
from flask.helpers import url_for
from flask import Blueprint
 
#from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
from flask_migrate import Migrate
from twlapi.config import TITLE
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    Bootstrap(app)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "core.login"
    migrate = Migrate(app, db)
    
    from twlapi.flaskapp.views import twl as core_blueprint
    
    app.register_blueprint(core_blueprint, url_prefix='/')

    return app