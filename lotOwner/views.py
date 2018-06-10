from django.shortcuts import render,redirect
from accounts.models import OwnerProfile
from .models import LotDetails
from .forms import LotDetailsForm,LocationForm
# Create your views here.

def home(request,profile_id):
    current_profile=OwnerProfile.objects.get(id=profile_id)
    title='Welcome lot owner'
    lots=LotDetails.objects.filter(owner=current_profile)
    return render (request,'Lot/home.html',{"title":title,"lots":lots,"current_profile":current_profile})
def Lotdetail(request,profile_id):
    current_profile=OwnerProfile.objects.get(id=profile_id)

    if request.method == 'POST':
        form=LotDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            details=form.save(commit=False)
            details.owner=current_profile
            details.save()
            return redirect (home,current_profile.id)
    else:
        form=LotDetailsForm()
    return render(request,'Lot/details.html',{"form":form,"current_profile":current_profile})
