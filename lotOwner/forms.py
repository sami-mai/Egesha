from django import forms
from .models import LotDetails,Location
from accounts.models import OwnerProfile

#Create forms here
class OwnerProfileForm(forms.ModelForm):
    '''
    We create an owner profile form to save the owner's information
    '''
    class Meta:
        model=OwnerProfile
        fields=('avatar','bio','national_id','phone_number')
class LotDetailsForm(forms.ModelForm):
    '''
    we create a lot details form to pick information about the lot
    '''
    class Meta:
        model=LotDetails
        fields=('Name_of_lot','Image_of_Lot','Total_number_of_spaces','location')
