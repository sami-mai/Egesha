from django import forms
from .models import LotDetails,Location

#Create forms here
class LotDetails(forms.ModelForm):
    '''
    we create a lot details form to pick information about the lot
    '''
    class Meta:
        model=LotDetails
        fields=('Name_of_lot','Total_number_of_spaces')
class Location(forms.ModelForm):
    '''
    We create a location form to pick information about the lot
    '''
    class Meta:
        model=Location
        fields=('Name','latitude','longitude')
               
