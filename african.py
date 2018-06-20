import africastalking


import random
my_randoms=[random.randrange(1,101,1) for _ in range (10)]
rad=map(str,my_randoms)
rad1="".join(rad)
# print(rad1)
some_key="afdba9fece25e56e1e9aaf7d9ba09363f7e80c859298a7c4064e53be32175a3a"
africastalking.initialize(username='sandbox', api_key='afdba9fece25e56e1e9aaf7d9ba09363f7e80c859298a7c4064e53be32175a3a')
sms = africastalking.SMS
def on_finish(error, response):
 if error is not None:
     raise error
 print(response)

number=['+254722163292']



sms.send("Space is Booked!{}" .format(rad1),['+254722163292'] , callback=on_finish)
