# Service prototype using Twilio API

TWILIO API offers the possibility to send and reply to SMS and to get access to your Twilio account from a program. This package shows some examples using python.

### Requirements

* twilio ~=6.0.0

### Features

* Send SMS
* Reply to incoming SMS
* Retrieve message from messageSID
* Get the outbox list
* Get the inbox list
* Get the last message sent
* Get the count of sent messages
* Get the count of outbox messages
* Get the count of inbox messages


## Getting Started


Register on [Twilio](https://twilio.com) to get your Twilio account identifier and authentication token.

### Sending SMS and replying programmatically


#### Create and activate a virtual environment

To create a virtualenv run the following command:

```shell
$ python3 -m venv env
```
Navigate to your virtualenv folder activate it with the following:

```shell
$ source bin/activate
```

#### Setting environment variables

To protect the credentials, we avoid their direct declaration by defining the following environment variables.

```
**TW_ACCOUNT_SID** - your Twilio account identifier
**TW_AUTH_TOKEN** - your Twilio authentication token
**TW_PHONE_NR** - your Twilio phone number
```


```shell    
$ export TW_ACCOUNT_SID=Your_Twilio_Account_Identifier
```

```shell
$ export TW_AUTH_TOKEN=Your_Twilio_Authentication_Token
```

You can optionally add your Twilio phone number. 

```shell
$ export TW_PHONE_NR=Your_Twilio_Phone_Number
```

### Sending a SMS programmatically

To test the _send_ function, run inside the projet directory the following commands

```shell
$ python
...
>>> from twlapi.sms import send
>>> send('+33062333xx', PHONE, 'Hi there!')
```	    
### Replying to incoming SMS from Flask


See (link to twilio flask app)
	