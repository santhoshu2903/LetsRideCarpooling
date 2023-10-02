from twilio.rest import Client

account_sid = 'ACd607e2f86a57f692c81867be2f0b351f'
auth_token = '28000cefd2c2ff8f4c7ebb8b73d500ea'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18449584452',
  to='+19803224017',
  body="working"
)

print(message.sid)