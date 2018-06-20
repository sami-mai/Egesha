from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from driver.models import Cardetails
from .models import Parked
from .forms import Parkedcars

def dashboard(request):
    cardetails = Cardetails.objects.all()

    if request.method == 'POST':
        form = Parkedcars(request.POST,request.FILES)
        if form.is_valid():
            parked = form.save(commit=False) 
            parked.save()
    else:
        form = Parkedcars()

    return render(request,'lotManager/index.html',{"cardetails":cardetails,"form":form})
