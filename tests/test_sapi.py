'''
Usage:
    $ pytest -q --number="<to>" --message="<message>"
'''

from twilio_service_api.sms import *


def test_send(number, message):

    res = send(number, PHONE, message)
    assert len(res) != 0


def test_outbox_count():
    res = outbox_count()
    assert isinstance(res, int)
    