from django import forms
from .models import LotDetails,Location

#Create forms here
class LotDetailsForm(forms.ModelForm):
    '''
    we create a lot details form to pick information about the lot
    '''
    class Meta:
        model=LotDetails
        fields=('Name_of_lot','Image_of_Lot','Total_number_of_spaces')
class LocationForm(forms.ModelForm):
    '''
    We create a location form to pick information about the lot
    '''
    class Meta:
        model=Location
        fields=('name_of_location','latitude','longitude')
