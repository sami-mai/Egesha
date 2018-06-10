from django.shortcuts import render

# Create your views here.

def home(request):
    title='Welcome lot owner'
    return render (request,'Lot/home.html',{"title":title})
