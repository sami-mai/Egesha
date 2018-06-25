from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
# import unirest  # unirest is a http library.
import json


def home(request):

    return render(request, 'pay/rave.html')


# data = {
#     "txref": "MC-1520443531487",  # this is the reference from the payment button response after customer paid.
#     "SECKEY": "FLWSECK-df3b77a5c3333b3339d27fae2803aba5-X"  # this is the secret key of the pay button generated
#     }
#
#
# # function called after your request gets a response from rave's server
# def callback_function(response):
#     # confirm that the response for the transaction is successful
#     if response.body['data']['status'] == 'success':
#         # confirm that the amount for that transaction is the amount you wanted to charge
#         if response.body['data']['chargecode'] == '00':
#
#             if response.body['data']['amount'] == 5:
#                 print("Payment successful then give value")
#
# # this is the url of the staging server. Please make sure to change to that of
# # production server when you are ready to go live.
#
#
# url = "https://ravesandboxapi.flutterwave.com/flwv3-pug/getpaidx/api/v2/verify"
#
# # make the http post request to our server with the parameters
# thread = unirest.post(
#     url, headers={"Content-Type": "application/json"},
#     params=data, callback=callback_function)
