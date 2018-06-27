from django import forms
from .models import LotDetails, Location,PaymentDetails
from accounts.models import OwnerProfile


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
        fields=('Name_of_lot','Image_of_Lot','Total_number_of_spaces')
class PaymentForm(forms.ModelForm):
    '''
    we create a form to pick up lot owner's account details
    '''
    class Meta:
        model=PaymentDetails
        fields=('Bank_name','Account_number')
