'''
Usage:
    $ pytest -q --number="<to>" --message="<message>"
    
    To test a single funtion.
    
    $ pytest -q -k <function-name> --number="<to>" --message="<message>"
    ex.
    $ pytest -q -k test_send --number="+15443323456" --message="Hello World"
'''

from twilio_service_api.sms import *


def test_send(number, message):

    res = send(number, PHONE, message)
    assert len(res) != 0


def test_outbox_count():
    res = outbox_count()
    assert isinstance(res, int)
    