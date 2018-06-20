from django.db import models
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

class Timein(models.Model):
    '''
    class for populating timein details
    '''
    
    time_in = models.TimeField()
   
class Timeout(models.Model):
    '''
    class for populating timeout details
    '''
    
    time_out = models.TimeField()