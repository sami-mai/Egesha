from django import forms
from .models import Parked,CheckedOut

class Parkedcars(forms.ModelForm):
    class Meta:
        model = Parked
        fields = ['car_plate']

class Checkedoutcars(forms.ModelForm):
    class Meta:
        model = Parked
        fields = ['car_plate']