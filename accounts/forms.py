from django import forms
from accounts.models import User, DriverProfile, ManagerProfile, OwnerProfile


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class EditDriver(forms.ModelForm):
    class Meta:
        model = DriverProfile
        fields = ['avatar', 'bio', 'license', 'phone_number']
        exclude = ['user', 'join_date']


class EditManager(forms.ModelForm):
    class Meta:
        model = ManagerProfile
        fields = ['avatar', 'bio', 'national_id', 'phone_number']
        exclude = ['user', 'join_date']


class EditOwner(forms.ModelForm):
    class Meta:
        model = OwnerProfile
        fields = ['avatar', 'bio', 'national_id', 'phone_number']
        exclude = ['user', 'join_date']
