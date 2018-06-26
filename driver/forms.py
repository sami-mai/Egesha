from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cardetails,Timein,Timeout
# from datetimewidget.widgets import DateTimeWidget

# cardetails form
class CardetailsForm(forms.ModelForm):
    class Meta:
        model = Cardetails
        fields = ['car_plate','car_make']

#timein form
class TimeinForm(forms.ModelForm):
    class Meta:
        model = Timein
        fields = ['time_in']
        dateTimeOptions = {
        'format': 'HH:ii P',
        'autoclose': True,
        'showMeridian' : True
        }
        widgets = {
         #NOT Use localization and set a default format
        # 'datetime': DateTimeWidget(options = dateTimeOptions)
        }
#timeout form
class TimeoutForm(forms.ModelForm):
    class Meta:
        model = Timeout
        fields = ['time_out']

        dateTimeOptions = {
        'format': 'HH:ii P',
        'autoclose': True,
        'showMeridian' : True
        }
        widgets = {
        #NOT Use localization and set a default format
        # 'datetime': DateTimeWidget(options = dateTimeOptions)
        }
