from django.contrib import admin
from .models import Cardetails,Timein,Timeout

# Register your models here.
admin.site.register(Cardetails)
admin.site.register(Timein)
admin.site.register(Timeout)