from django.contrib import admin
from accounts.models import DriverProfile, ManagerProfile, OwnerProfile


# Register your models here.
admin.site.register(DriverProfile)
admin.site.register(ManagerProfile)
admin.site.register(OwnerProfile)
