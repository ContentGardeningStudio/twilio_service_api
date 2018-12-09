'''
Created on Oct 31, 2018

@author: A. Ayeva
'''
 
# -*- coding: utf-8 -*-
from twlapi.flaskapp import db, login_manager
#from app import UserMixin 
from flask_login import AnonymousUserMixin, UserMixin
#import login_manager, AnonymousUserMixin
from werkzeug.security import check_password_hash, generate_password_hash  # @UnresolvedImport
        

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, unique=True, primary_key=True) # @UndefinedVariable
    username = db.Column(db.String(32), unique=True)  # @UndefinedVariable
    email = db.Column(db.String(128), unique=True)  # @UndefinedVariable
    phone = db.Column(db.String(32), unique=True)  # @UndefinedVariable
    password_hash = db.Column(db.String(128), unique=True)  # @UndefinedVariable
    

    def __init__(self, username, email, phone, password):

        self.username = username
        self.email = email
        self.phone = phone
        self.password = password
        super(User, self).__init__()

    @property
    def password(self):
        raise AttributeError('`password` is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class AnonymousUser(AnonymousUserMixin):
    def can(self, _):
        return False

    def is_admin(self):
        return False


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
