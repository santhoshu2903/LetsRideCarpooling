import random

def generate_otp():
    return ''.join(random.choice('0123456789') for i in range(6))

from twilio.rest import Client

def send_sms(phone_number, message):
    # Your Twilio account SID and Auth Token
    account_sid = 'ACd607e2f86a57f692c81867be2f0b351f'
    auth_token = '8ee8f3b5ce7f516bfde81a6a166fd35b'
    client = Client(account_sid, auth_token)

    # Your Twilio phone number
    twilio_phone_number = '+18449584452'
    message = client.messages.create(
        to=phone_number,
        from_=twilio_phone_number,
        body=message
    )
    return message.sid

# Using the functions
otp = generate_otp()
send_sms('+19803224017', f"Your OTP is: {otp}")  # Replace with the actual phone number
