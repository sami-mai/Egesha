from django import forms
from accounts.models import User, DriverProfile, ManagerProfile, OwnerProfile


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class EditDriver(forms.ModelForm):
    class Meta:
        model = DriverProfile
        fields = ['license', 'phone_number', 'avatar', 'bio']
        exclude = ['user', 'join_date']


class EditManager(forms.ModelForm):
    class Meta:
        model = ManagerProfile
        fields = ['national_id', 'phone_number', 'avatar', 'bio']
        exclude = ['user', 'join_date']


class EditOwner(forms.ModelForm):
    class Meta:
        model = OwnerProfile
        fields = ['national_id', 'phone_number', 'avatar', 'bio']
        exclude = ['user', 'join_date']
