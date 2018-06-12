from django.shortcuts import render, redirect
from accounts.models import OwnerProfile
from .models import LotDetails,Location
from .forms import LotDetailsForm,OwnerProfileForm
from django.contrib.auth.models import User
import googlemaps
#we import the serializers to convert the data from python to json
from django.core import serializers
from django.core.serializers import serialize
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.

def home(request):
    current_user=request.user.id
    title='Welcome lot owner'
    lots=''
    current_profile=''
    current_user_name=OwnerProfile.objects.filter(id=request.user.id)
    if current_user_name.exists():
        current_profile=OwnerProfile.objects.get(id=current_user)
        lots=LotDetails.objects.filter(owner=current_profile)
    if request.method == 'POST':
        form1=OwnerProfileForm(request.POST)
        if form1.is_valid():
            user_profile=form1.save(commit=False)
            user_profile.user=request.user
            return redirect (home)
    else:
        form1=OwnerProfileForm()
    spots=list(Location.objects.filter(owner=current_profile))
    print(spots)
    coords={"1":1,"2":2}
    coords_json=json.dumps(coords,cls=DjangoJSONEncoder)
    spots_json=serializers.serialize('json',spots,cls=DjangoJSONEncoder)
    return render (request,'Lot/home.html',{"title":title,"lots":lots,"current_profile":current_profile,"form1":form1,"coords_json":coords_json,"spots_json":spots_json,})
def Lotdetail(request,profile_id):
    current_profile=OwnerProfile.objects.get(id=profile_id)
    current_user=request.user
    if request.method == 'POST':
        form = LotDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            details = form.save(commit=False)
            details.owner = current_profile
            details.save()
<<<<<<< HEAD
            return redirect(home, current_profile.id)
=======
            return redirect (home)
>>>>>>> daafda9bc01eff8999394265505c218be242e265
    else:
        form=LotDetailsForm()

    return render(request,'Lot/details.html',{"form":form,"current_profile":current_profile,"current_user":current_user})
def map(request):
    lot_owner=OwnerProfile.objects.get(id=request.user.id)
    gmaps=googlemaps.Client(key='AIzaSyBmrKc7FjQwLm9vEtseo5LK7Z6M_1aPm5k')
    title='hello'
    results=gmaps.geocode('nairobi')

    print('I am here 1')

    if 'address' in request.GET and request.GET['address']:
        address1=request.GET.get("address")
        geo=gmaps.geocode(address1)
        print('I am here')

        latitude=geo[0]['geometry']['location'].get('lat')
        longitude=geo[0]['geometry']['location'].get('lng')
        location=Location()
        print(latitude)
        print(longitude)
        location.name_of_location=address1
        location.latitude=latitude
        location.longitude=longitude
        location.owner=lot_owner
        location.save()

        return redirect (home)

    else:
        print('Not working')
    return redirect(home)
