from twilio.rest import Client
import random

n = random.randint(1000,9999)

account_sid = 'AC8855bd4f6b28926dbf05736df367ba12'
auth_token = '54643209f5917a9763d9b8f6af4e0e3a'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+12562900939',
  body='Your OTP For Login is :' + str(n),
  to='+919971514995'
)

while(True):
   OTP = input("ENTER OTP :")

   if OTP == str(n):
        print("SUCCESS")
        break
   else:
        print("FAILURE")