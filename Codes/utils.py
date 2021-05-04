import os
from twilio.rest import Client

account_sid = 'EXAMPLE' # PLACE YOUR ACCOUNT_SID
account_token = 'EXAMPLE' # ACCOUNT_TOKEN

client = Client(account_sid, account_token)

def send_sms(user_code, phone_number):
    message = client.messages.create(
        body=f"Hi! Your Verification code is {user_code}",
        from_ = "+13345106386",
        to = f"{phone_number}"
    )

    print(message.sid)