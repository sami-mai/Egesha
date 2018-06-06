from django import forms
from accounts.models import User


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


# class EditProfile(forms.ModelForm):
#     class Meta:
#         model = Profile
        # fields = ['avatar', 'bio', 'birthdate', 'veg_status']
        # exclude = ['user', 'location', 'listing', 'recipe', 'review']
