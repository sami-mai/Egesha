from django.db import models
from accounts.models import OwnerProfile

# Create your models here.
class LotDetails(models.Model):
    '''
    We create a lot details model to store information about the lot details
    '''
    Name_of_lot=models.CharField(max_length=40)
    Image_of_Lot=models.ImageField(upload_to='images/',null=True)
    Total_number_of_spaces=models.IntegerField()
    owner=models.ForeignKey(OwnerProfile,null=True)
    def __str__(self):
        return self.Name_of_lot
class Location(models.Model):
    '''
    We create a location model to store information about the location of the lot
    '''
    '''
    we add a lotdetails  foreignkey to filter the location depending on the lot
    '''
    name_of_location=models.CharField(max_length=40)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    Lot=models.ForeignKey(LotDetails,null=True)
