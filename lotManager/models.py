from django.db import models
from django.contrib.auth.models import User
from accounts.models import ManagerProfile
from accounts.models import DriverProfile


# Create your models here.


class Parked(models.Model):
    '''
    class for populating details of the checked in car
    '''
    car_plate = models.CharField(max_length = 30,default = 'KCA101Z',null = True)

class CheckedOut(models.Model):
    '''
    class for populating details of the checked out car
    '''
    car_plate = models.CharField(max_length = 30,default = 'KCA101Z',null = True)
    