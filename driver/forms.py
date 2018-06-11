from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cardetails,Booking

# cardetaisls form
class CardetailsForm(forms.ModelForm):
    class Meta:
        model = Cardetails
        fields = ['car_plate','car_make']
