from django.contrib import admin
from .models import LotDetails,Location,PaymentDetails
# Register your models here.
admin.site.register(Location)
admin.site.register(LotDetails)
admin.site.register(PaymentDetails)
