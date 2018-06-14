gfrom django.db import models
from accounts.models import DriverProfile
from lotOwner.models import LotDetails
import datetime as dt
from django.contrib.auth.models import User
# Create your models here.
class Cardetails(models.Model):
    '''
    class for populating details of the car
    '''
    car_plate = models.CharField(max_length = 30,default = 'KCA101Z',null = True)
    car_make = models.CharField(max_length = 30, default ='RangeRover', null = True)
    driver = models.ForeignKey(DriverProfile, null = True,on_delete=models.CASCADE)

class Booking(models.Model):
    '''
    class for populating booking details
    '''
    
    driver = models.ForeignKey(DriverProfile, null = True,on_delete=models.CASCADE)
    lotdetails = models.ForeignKey(LotDetails, null = True,on_delete=models.CASCADE)
    time_in = models.TimeField(auto_now_add=True, blank=True)
    time_out = models.TimeField(auto_now_add=True, blank=True)