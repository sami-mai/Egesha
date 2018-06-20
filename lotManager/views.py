from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from driver.models import Cardetails

def dashboard(request):
    cardetails = Cardetails.objects.all()

    return render(request,'lotManager/index.html',{"cardetails":cardetails})
