'''
Created on Oct 31, 2018

@author: A. Ayeva
'''
import os

TITLE = "TWILIO SERVICE API"
ACCOUNT = os.getenv('TW_ACCOUNT_SID', None)
TOKEN = os.getenv('TW_AUTH_TOKEN', None)
PHONE = os.getenv('TW_PHONE_NR', None)