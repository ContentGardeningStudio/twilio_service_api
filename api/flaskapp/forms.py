'''
Created on Oct 31, 2018

@author: A. Ayeva
'''

from flask import url_for
from flask_wtf import Form, FlaskForm
from wtforms import ValidationError
from wtforms.fields import (BooleanField, PasswordField, StringField,
                            SubmitField)
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email, EqualTo, InputRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from .models import User

from flask import Markup
from email.message import Message
from wtforms.fields.simple import TextField

class RegisterForm(FlaskForm):
    #first_name = StringField(
        #'First name', validators=[InputRequired(), Length(1, 64)])
    username = StringField(
        'username', validators=[InputRequired(), Length(1, 32)])
    email = EmailField(
        'email', validators=[InputRequired(), Length(1, 128), Email()])
    phone = StringField(
        'phone number', validators=[InputRequired(), Length(1, 32)])
    password = PasswordField(
        'password',
        validators=[
            InputRequired(), EqualTo('password2', 'Passwords must match')
        ])
    password2 = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first(): # @UndefinedVariable
            raise ValidationError(('Email already registered. (Did you mean to '
                                  + Markup('<a href="login">log in</a>') + ' instead?)').format(url_for('index')))



class LoginForm(FlaskForm):

    email = EmailField(
        'email', validators=[InputRequired(), Length(1, 128), Email()])
    password = PasswordField(
        'password',
        validators=[
            InputRequired()])
    submit = SubmitField('Sign In!')
    

class CheckForm(FlaskForm):

    code = StringField(
        'Verification Code', validators=[InputRequired(), Length(4)])
    
    submit = SubmitField('Submit')
    
class SendForm(FlaskForm):
    """
    """
    number = StringField('To:', validators=[InputRequired()])
    message = TextField('Message')
    submit = SubmitField('Send')
    
class ReplyForm(FlaskForm):
    """
    """
    message = TextField('Message')
    submit = SubmitField('Send')