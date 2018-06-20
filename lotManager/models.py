from django.db import models
from django.contrib.auth.models import User
from accounts.models import ManagerProfile
from accounts.models import DriverProfile


# Create your models here.


class Parked(models.Model):
    '''
    class for populating details of the car
    '''
    car_plate = models.CharField(max_length = 30,default = 'KCA101Z',null = True)
    car_make = models.CharField(max_length = 30, default ='RangeRover', null = True)
    driver = models.ForeignKey(DriverProfile, null = True,on_delete=models.CASCADE)
