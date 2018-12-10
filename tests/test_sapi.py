'''
Created on Dec 10, 2018

@author: loup
'''
import pytest

from twilio_service_api.sms import *


def test_send():
    dest = "+4901704499765"
    phone = PHONE
    msg = "Testing send function"
    res = send(dest, phone, msg)
    assert len(res) != 0


def test_outbox_count():
    res = outbox_count()
    assert isinstance(res, int)
    