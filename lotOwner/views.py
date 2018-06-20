from django.shortcuts import render, redirect
from accounts.models import OwnerProfile
from .models import LotDetails,Location
from .forms import LotDetailsForm,OwnerProfileForm,PaymentForm
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
    # title='Welcome lot owner'
    lots=''
    current_profile=''

    current_user_name=OwnerProfile.objects.filter(id=request.user.id)
    current_profile=OwnerProfile.objects.filter(user=current_user)
    location=''
    if current_user_name.exists():
        current_profile=OwnerProfile.objects.filter(user=current_user)
        lots=LotDetails.objects.filter(owner=current_profile)
        location=Location.objects.all()

    else:
        print('no profile')

    if request.method == 'POST':
        form1=OwnerProfileForm(request.POST, request.FILES,instance=current_profile)
        if form1.is_valid():
            user_profile=form1.save(commit=False)
            user_profile.user=request.user
            user_profile.save( )
            return redirect('/lot/owner/')
    else:
        form1=OwnerProfileForm()
    spots=list(Location.objects.all())


    print(spots)
    coords={"1":1,"2":2}
    coords_json=json.dumps(coords,cls=DjangoJSONEncoder)
    spots_json=serializers.serialize('json',spots,cls=DjangoJSONEncoder)

    return render (request,'Lot/home.html',{"lots":lots,"current_profile":current_profile,"form1":form1,"location":location,"coords_json":coords_json,"spots_json":spots_json})


def Lotdetail(request,profile_id):
    current_profile=''
    current_user=request.user
    current_profile=OwnerProfile.objects.get(id=profile_id)



    if request.method == 'POST':
        form = LotDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            details = form.save(commit=False)
            details.owner = current_profile
            details.save()

            return redirect('/lot/owner/')

    else:
        form=LotDetailsForm()

    return render(request,'Lot/details.html',{"form":form,"current_profile":current_profile,"current_user":current_user})


def map(request,lot_id):

    lot_owner=OwnerProfile.objects.get(id=request.user.id)
    lot=LotDetails.objects.get(id=lot_id)
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
        location.lot=lot
        location.save()
        return redirect ('/lot/owner/')

    else:
        print('Not working')
    return redirect('/lot/owner/')


def location(request,lot_id):
    current_user=request.user.id
    lot=LotDetails.objects.get(id=lot_id)

    spots=''
    current_user_name=OwnerProfile.objects.filter(id=request.user.id)

    if current_user_name.exists():
        current_profile=OwnerProfile.objects.get(id=current_user)
        lots=LotDetails.objects.all()
        spots=list(Location.objects.filter(lot=lot))

        print(spots)
    coords={"1":1,"2":2}
    coords_json=json.dumps(coords,cls=DjangoJSONEncoder)
    spots_json=serializers.serialize('json',spots,cls=DjangoJSONEncoder)
    return render (request,'Lot/location.html',{"coords_json":coords_json,"spots_json":spots_json,"lot":lot})
def edit_profile(request,profile_id):
    current_profile=OwnerProfile.objects.get(id=profile_id)
    if request.method == 'POST':
        form=OwnerProfileForm(request.POST, request.FILES,instance=current_profile)
        if form.is_valid():
            user_profile=form.save(commit=False)
            user_profile.user=request.user
            user_profile.save( )
            return redirect('/lot/owner/')
    else:
        form=OwnerProfileForm()
    return render (request,'Lot/edit_profile.html',{"form":form,"current_profile":current_profile})
def edit_lot(request,lot_id):
    lot=LotDetails.objects.get(id=lot_id)
    if request.method == 'POST':
        form = LotDetailsForm(request.POST,request.FILES,instance=lot)
        if form.is_valid():
            details = form.save(commit=False)
            details.save()

            return redirect('/lot/owner/')

    else:
        form=LotDetailsForm()
    return render (request,'Lot/edit_lot.html',{"form":form,"lot":lot})
def payment(request,profile_id):
    current_profile=OwnerProfile.objects.get(id=profile_id)
    if request.method == 'POST':
        form=PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile=form.save(commit=False)
            user_profile.owner=current_profile
            user_profile.save()
            return redirect('/lot/owner/')
    else:
        form=PaymentForm()
    return render(request,'Lot/payment.html',{"form":form,"current_profile":current_profile})
