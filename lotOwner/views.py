from django.shortcuts import render,redirect
from accounts.models import OwnerProfile
from .models import LotDetails
from .forms import LotDetailsForm,LocationForm,OwnerProfileForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    current_user = request.user.id
    title='Welcome lot owner'
    lots = 'none'
    current_profile = 'none'
    current_user_name=OwnerProfile.objects.filter(id=request.user.id)
    if current_user_name.exists():
        current_profile=OwnerProfile.objects.get(id=current_user)
        lots=LotDetails.objects.filter(owner=current_profile)
    if request.method == 'POST':
        form=LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect (home,current_profile.id)
    else:
        form=LocationForm()
    context = {
        "title":title,
        "lots":lots,
        "current_profile":current_profile,
        "form":form,
        "current_user": current_user
    }
    return render (request,'Lot/home.html', context)
def Lotdetail(request,profile_id):
    current_profile=OwnerProfile.objects.get(id=profile_id)
    current_user=request.user
    if request.method == 'POST':
        form=LotDetailsForm(request.POST,request.FILES)
        if form.is_valid():
            details=form.save(commit=False)
            details.owner=current_profile
            details.save()
            return redirect (home,current_profile.id)
    else:
        form=LotDetailsForm()

    return render(request,'Lot/details.html',{"form":form,"current_profile":current_profile,"current_user":current_user})
