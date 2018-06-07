from django.db import models
from django.contrib.auth.models import User
#import security profile
#import lot details

# Create your models here.

class Guard(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot,on_delete=models.CASCADE)

    #method to edit stuff..lot details