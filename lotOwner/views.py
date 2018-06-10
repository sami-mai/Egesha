from django.shortcuts import render
from accounts.models import OwnerProfile
# Create your views here.

def home(request):
    title='Welcome lot owner'
    return render (request,'Lot/home.html',{"title":title})
def Lotdetail(request,profile_id):
    current_profile=
