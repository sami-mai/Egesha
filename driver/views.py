from .forms import CardetailsForm,TimeinForm,TimeoutForm
from django.shortcuts import render,redirect,get_object_or_404
from .models import Cardetails,Timein,Timeout
from django.http import Http404
from accounts.models import DriverProfile
from accounts.forms import EditDriver,EditUserForm
from lotOwner.models import Location
from django.core import serializers
from django.core.serializers import serialize
import json
from django.core.serializers.json import DjangoJSONEncoder
# Create your views here.
import africastalking

def homed(request):
    '''
    function to display driver and car details
    '''
    title="Egesha | Home "
    try:
        cardetails = Cardetails.objects.filter(id = request.user.id)
        profile = DriverProfile.objects.filter(id =request.user.id)
        user = request.user
    except ValueError:
        Http404

    return render(request,'user/indexed.html',{"cardetails":cardetails,"profile":profile,"user":user})

def car_details(request):
    '''
    function to populate the details of the car
    '''
    title="Egesha | Car Details "
    current_user = request.user
    cardetails = Cardetails.objects.filter(id = request.user.id)
    profile = DriverProfile.objects.filter(id =request.user.id)
    try:

        if request.method == 'POST':
            cardetails_form = CardetailsForm(request.POST, request.FILES)

            if cardetails_form.is_valid():
                cardetails = cardetails_form.save(commit=False)

                cardetails.user=current_user

                cardetails.save()

                return redirect('/driver/home/')

        else:
            cardetails_form = CardetailsForm

    except ValueError:
        Http404
    context = {
        "title": title,
        "cardetails_form": cardetails_form,
        "profile": profile,
        "cardetails": cardetails
        }
    return render(request, 'user/cardetails.html', context)


def edit_profile(request):
    '''
    function to populate the details of the profile
    '''
    title="Egesha | Profile Form "
    current_user = request.user
    try:
        if request.method == 'POST':

            driver_form  = EditDriver(request.POST,request.FILES)
            user_form = EditUserForm(request.POST, request.FILES)
            if driver_form.is_valid() and user_form.is_valid():

                driverdetails = driver_form.save(commit=False)
                userdetails = user_form.save(commit=False)

                driverdetails.user=current_user
                userdetails.user=current_user

                driverdetails.save()
                userdetails.save()
                return redirect('/driver/car-details')

        else:
            driver_form  = EditDriver()
            user_form = EditUserForm()

    except ValueError:
        Http404

    return render(request, 'user/profileform.html', {"title":title,"driver_form":driver_form,"user_form":user_form})

def update_profile(request,id):
    '''
    function to update profile
    '''
    title="Egesha | edit-profile "
    current_user = DriverProfile.objects.get(id = id)
    try:
        if request.method == 'POST':

            driver_form  = EditDriver(request.POST,request.FILES, instance = current_user)

            if driver_form.is_valid():
                driverdetails = driver_form.save(commit=False)
                driverdetails.user=current_user
                driverdetails.save()

                return redirect('/driver')

        else:
            driver_form  = EditDriver()
    except ValueError:
        Http404

    return render(request, 'user/editprofile.html', {"title":title,"driver_form":driver_form,"id":id,"current_user":current_user})

def home(request):
    '''
    function to display driver and car details
    '''
    title="Egesha | Home "
    try:
        cardetails = Cardetails.objects.filter(id = request.user.id)
        profile = DriverProfile.objects.filter(id =request.user.id)
        timein = Timein.objects.all()
        timeout = Timeout.objects.all()
        user = request.user
    except ValueError:
        Http404


    return render(request,'user/index.html',{"cardetails":cardetails,"profile":profile,"timeout":timeout,"timein":timein,"user":user})


def trigger_payment(request):
    africastalking.initialize(username='sandbox', api_key='4caafe95008a0a8ba2df43746a62238715dd1f3f3517be3a898402d40542c034')
    payment = africastalking.Payment
    res = payment.mobile_checkout(product_name='egesha',phone_number='+254720676920', currency_code='KES', amount=4000)
    return redirect('/driver/')

def search_location(request):
    current_user=request.user.id
    search_term=request.GET.get("location")
    spots=list(Location.search(search_term))



    print(spots)
    coords={"1":1,"2":2}
    coords_json=json.dumps(coords,cls=DjangoJSONEncoder)
    spots_json=serializers.serialize('json',spots,cls=DjangoJSONEncoder)
    searched_locations=Location.search(search_term)

    return render (request,'user/search.html',{"coords_json":coords_json,"spots_json":spots_json,"searched_locations":searched_locations})

def time(request):
    '''
    function to populate the time into the carlot
    '''
    title="Egesha | Time In "
    current_user = request.user
    try:
        if request.method == 'POST':
            timein_form = TimeinForm(request.POST, request.FILES)
            timeout_form = TimeoutForm(request.POST, request.FILES)
            if timein_form.is_valid() and timeout_form.is_valid():
                timein = timein_form.save(commit=False)
                timeout = timeout_form.save(commit=False)

                timein.user=current_user
                timeout.user=current_user

                timein.save()
                timeout.save()

                return redirect('/driver/')

        else:
            timein_form  = TimeinForm
            timeout_form  = TimeoutForm

    except ValueError:
        Http404

    return render(request, 'user/time.html', {"title":title,"timein_form": timein_form,"timeout_form": timeout_form})

def status_success(request):
    return render (request,'user/status_success.html')

def status_failed(request):
    return render (request,'user/status_failed.html')
