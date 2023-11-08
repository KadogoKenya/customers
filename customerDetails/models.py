from django.db import models
# from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime,timedelta,date, timezone
# Create your models here.

class LocationDetails(models.Model):
    County=models.CharField(max_length=40)
    SubCounty = models.CharField(max_length=40)
    Ward = models.CharField(max_length=40)
    Building_name = models.CharField(max_length=40)
    floor=models.IntegerField(max_length=200,default=0)
    
    def __str__(self):
        return self.County

    def __str__(self):
        return self.SubCounty

class Business(models.Model):
    catchoice= [
        ('fintech', 'Fintech'),
        ('learning institution', 'Learning Institution'),
        ('transpotation', 'Transportation'),
        ]
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=30)
    date_of_birth=models.DateField(max_length=30)
    nationality=models.CharField(max_length=30)
    business_name=models.CharField(max_length=30)
    Business_category=models.CharField(max_length=30,choices=catchoice,default='fintech')
    business_registration_date=models.DateField(max_length=30)
    businessAge=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    location=models.ForeignKey(LocationDetails,on_delete=models.CASCADE,blank=True,null=True)

    def calculated_age(self):
        td = timezone.now() - self.business_registration_date
        return str(td)

    def __str__(self):
        return str(self.name)+"["+str(self.phone)+']'