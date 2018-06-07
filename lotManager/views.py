from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Guard
from django.contrib.auth.models import User

# Create your views here.
def landing(request):
    
    

    return render(request,'index.html')
