from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from driver.models import Cardetails
from .models import Parked,CheckedOut
from .forms import Parkedcars,Checkedoutcars

def operator(request):
    cardetails = Cardetails.objects.all()

  

    return render(request,'lotManager/index.html',{"cardetails":cardetails})

def checkin(request):
    if request.method == 'POST':
        form = Parkedcars(request.POST,request.FILES)
        if form.is_valid():
            parked = form.save() 
            parked.save()
    else:
        form = Parkedcars()

    carsparked = Parked.objects.all()

    return render(request,'lotManager/in.html',{"form":form,"carsparked":carsparked})

def checkout(request):
    if request.method == 'POST':
        form = Checkedoutcars(request.POST,request.FILES)
        if form.is_valid():
            checkedout = form.save() 
            checkedout.save()
    else:
        form = Checkedoutcars()

    carscheckedout = Parked.objects.all()

    return render(request,'lotManager/out.html',{"form":form,"carscheckedout":carscheckedout})
