from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    
    

    return render(request,'index.html')
