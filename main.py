from twilio.rest import Client
import random

n = random.randint(1000,9999)

account_sid = 'AC8855bd4f6b2892***********2'
auth_token = '54643209f5917a97***********'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+1256290***',
  body='Your OTP For Login is :' + str(n),
  to='+9199715*****'
)

while(True):
   OTP = input("ENTER OTP :")

   if OTP == str(n):
        print("SUCCESS")
        break
   else:
        print("FAILURE")
