'''
Created on Oct 31, 2018

@author: A. Ayeva
'''

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from .config import ACCOUNT, TOKEN, PHONE

import json
API_URL = 'https://api.twilio.com/2010-04-01/Accounts/'

def init():
    """ Returns a object from type Twilio Client
        @rtype: Client
    """
    return Client(ACCOUNT, TOKEN)


CLIENT = init()

def send(to, from_, body):
    """ Send a SMS from Twilio Number to destination number.
        @param to: Receiver
        @param from_: Sender
        @param body: Content of the message 
        @rtype: MessageSID
    """
    msg = CLIENT.messages.create(to=to, from_=from_, body=body)
    return (msg.sid)
    

def reply(message):
    """ Reply to SMS
    """
    
    resp = MessagingResponse()
    
    return (resp, str(resp.message(message)) )


def get_msg_sid_list():
    """ Give the list of all Messages SIDs
        @rtype: List
    """
    return [ msg.sid for msg in CLIENT.messages.list()]


def get_msg(sid):
    """ Retrieve a message with sid.
        @param sid: The Message SID.
        @return: A Message.
    """
    msg_url = API_URL + ACCOUNT + '/SMS/Messages/' + str(sid) + '.json'
        
    msg = CLIENT.request(method='GET', uri=str(msg_url))

    return msg


def list_messages():
    ''' Give the list of Messages
        @rtype: List
    '''
    msg_sid_list = get_msg_sid_list()
    l = []
    for sid in msg_sid_list:
        msg = get_msg(sid)
        data = json.loads(msg.content)
        l.append({"from": data['from'], "to": data['to'], "body": data['body'], "date": data['date_sent'], "status": data['status']})
    return l

def last_msg():
    """ Retrieve the last message.
        @rtype: dict
    """
    sid = get_msg_sid_list()[0]
    
    data = json.loads(get_msg(sid).content)
    
    return {"from": data['from'], "to": data['to'], "body": data['body'], "date": data['date_sent'], "status": data['status']}


def sent_msg_count():
    ''' Give the count of set messages.
        @rtype: int
    '''
    return len(get_msg_sid_list())

def inbox():
    msgs = CLIENT.messages.list()
    contents = [json.loads(get_msg(m.sid).content) for m in msgs]
    inbx = []
    for c in contents:
        if PHONE not in str(c['from']):
            msg = '{} | {} | {}'.format(c['from'], c['date_sent'], c['body'])
            inbx.append(msg)
    return inbx

def inbox_count():
    return len(inbox())


def outbox():
    msgs = CLIENT.messages.list()
    contents = [json.loads(get_msg(m.sid).content) for m in msgs]
    inbx = []
    for c in contents:
        if PHONE not in str(c['to']):
            msg = '{} | {} | {}'.format(c['from'], c['date_sent'], c['body'])
            inbx.append(msg)
    return inbx

def outbox_count():
    return len(outbox())