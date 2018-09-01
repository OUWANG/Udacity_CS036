#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 21:12:38 2018

@author: Austin
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2791dbbc8c6ad63d61661e42a18eb869"
# Your Auth Token from twilio.com/console
auth_token  = "0aae24079cdde91a94a222215bc48f42"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17184500858", 
    from_="+19735471377",
    body="Hello from Python!")

print(message.sid)

##Test