from django.contrib import admin
from .models import Parked,CheckedOut

# Register your models here.
admin.site.register(Parked)
admin.site.register(CheckedOut)