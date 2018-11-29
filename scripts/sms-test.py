import os
from twilio.rest import Client

account_sid = "AC48524fdca77f1118718e27341f70d1b9"

# THE API KEY AND SECRET WERE CREATED IN section 4.2
api_key = "SK8732db2a62834bb489054e9ed6b02fa7"
api_secret = "yvIHNkzetAhp8fISSIeaINW9BHfHtLj7"

client = Client(api_key, api_secret, account_sid)

message = client.messages.create(to='+14124784604', from_='+14125334733', body='Hello world. this is a test message')

print(message.sid)
