from django import forms
from .models import Parked

class Parkedcars(forms.ModelForm):
    class Meta:
        model = Parked
       