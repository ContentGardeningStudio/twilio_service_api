'''
Created on Oct 31, 2018

@author: A. Ayeva
'''

#from app.core import core
from flask import flash, redirect, render_template, request, url_for, Markup, Blueprint
from flask_login import (current_user, login_required, login_user,
                         logout_user)
#from flask_rq import get_queue

from twlapi.flaskapp import db, TITLE
from twlapi.sms import *
from twlapi.flaskapp.models import User
from twlapi.flaskapp.forms import RegisterForm, LoginForm, CheckForm, SendForm,\
    ReplyForm
from twlapi.config import PHONE
from flask.helpers import flash 
from twlapi import sms
import json
import inspect
import markdown, markdown_code_blocks
twl = Blueprint('twl', __name__)

_to_register = None
_test_code = None


@twl.route('/')
def index():
        return render_template("index.html", app_title=TITLE, name='')


@twl.route('/home', methods=['GET', 'POST'])
def get_home():
    sform = SendForm()
    rform = ReplyForm()

    sid = None
    scode = Markup(markdown_code_blocks.highlight("```python\n" + inspect.getsource(sms_send) + "\n```"))
    rcode = Markup(markdown_code_blocks.highlight("```python\n" + inspect.getsource(reply) + "\n```"))
#     if sform.validate_on_submit():
#         to = sform.number.data
#         message = sform.message.data
#         sid = send(to=to, from_=PHONE, body=message)
#         
#         print(sid)
#         return render_template('home.html', app_title=TITLE, name='| Home', sform=sform, scode=scode, rcode=rcode, sid=sid) 

    
    
    return render_template('home.html', app_title=TITLE, name='| Home', sform=sform, rform=rform, scode=scode, rcode=rcode, sid=sid) 


@twl.route('/register', methods=['GET', 'POST'])
def register():
    """Register a new user, and send them a confirmation email.
    """
    form = RegisterForm()
    global _test_code, _to_register
    
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        phone = form.phone.data
        print (form.errors)
        
        user = User(username, email, phone, password)
        _to_register = user
       
        _test_code = '1234'
        
        send(to=phone, from_=PHONE, body= _test_code)
        flash('A verification SMS has been sent to {}.'.format(user.phone), 'warning')
        
        return redirect(url_for('twl.check'))
       
    return render_template('register.html', app_title=TITLE, name='| Registration', form=form)

    

@twl.route('/login', methods=['GET', 'POST'])
def login():
    """login
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()  # @UndefinedVariable
        if user is not None and user.password_hash is not None and \
                user.verify_password(form.password.data):
            login_user(user)
            flash('You are now logged in. Welcome back!', 'success')
            return redirect(request.args.get('next') or url_for('twl.get_home', user_id=current_user.username))  # @UndefinedVariable
        else:
            flash('Invalid email or password.', 'form-error')
    return render_template('login.html', app_title=TITLE, name='| Login', form=form)


@twl.route('/verification', methods=['GET', 'POST'])
def check():
    """ Verification
    """
    form = CheckForm()
    if form.validate_on_submit():
        code = form.code.data
        
        if str(code) == _test_code:
            try:
                db.session.add(_to_register)  # @UndefinedVariable
                db.session.commit()  # @UndefinedVariable
            except Exception as e:
                db.session.rollback()  # @UndefinedVariable

            flash('You have successfully registered! You may now login.')
            return redirect(url_for('twl.index'))
        
    return render_template('check.html', app_title=TITLE, name='| Registration', cform=form)


@twl.route('/sms/list', methods=['GET', 'POST'])
def get_message():
    
    
    messages = list_messages()
    for msg in messages:
        flash(msg)
   
    return render_template('home.html', app_title=TITLE, name='| Sent') 


@twl.route('/sms/', methods=['GET', ])
def last():
    msg = last_msg()
    flash(msg)
    return render_template('home.html', app_title=TITLE, name='| New')


@twl.route('/sms/reply', methods=['GET', 'POST'])
def reply():
    """ Reply to incoming SMS.
        @rtype: str
    """
    message = "Testing reply"
    rpl = sms.reply(message)
    
    return str(rpl[0])

@twl.route('/sms/count', methods=['GET',])
def sms_count():
    flash("TOTAL SENT: " + str(sent_msg_count()) + " SMS" )
    return render_template('home.html', app_title=TITLE, name='| Sent')


@twl.route('/sms/msg', methods=['POST','GET'])
def sms_send():
    #client = init()
    form = SendForm()
    if form.validate_on_submit():
        to = form.number.data
        message = form.message.data
        sid = send(to=to, from_=PHONE, body=message)
        print(sid)
        #return redirect('home')
        return render_template('home.html', app_title=TITLE, name='| Sent', sform=form, sid=sid)
    #msg = client.messages.create(to='+330615967734', from_=PHONE, body='Bjr Kémal, je fais un test, pourrais tu repondre au sms?')
    #flash(msg )
    return render_template('home.html', app_title=TITLE, name='| Sent', sform=form, sid=sid)


@twl.route('/sms/inbox', methods=['GET',])
def get_inbox():
    
    inbx = inbox()
    
    flash(inbx)
   
    return render_template('home.html', app_title=TITLE, name='| Inbox')

@twl.route('/sms/inbox/count', methods=['GET',])
def get_inbox_count():
    
    count = inbox_count()
    
    flash(count)
   
    return render_template('home.html', app_title=TITLE, name='| Inbox')


@twl.route('/sms/outbox', methods=['GET',])
def get_outbox():
    
    outbx = outbox()
    
    flash(outbx)
   
    return render_template('home.html', app_title=TITLE, name='| Outbox')

@twl.route('/sms/outbox/count', methods=['GET',])
def get_outbox_count():
    
    count = outbox_count()
    
    flash(count)
   
    return render_template('home.html', app_title=TITLE, name='| Outbox')