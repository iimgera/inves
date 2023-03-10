from django.db import models
from django.contrib.auth.models import User

class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to='investors', null=True, blank=True)
    about = models.TextField()
    active = models.BooleanField(default=True)



class BusinessOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)    
    photo = models.ImageField(upload_to='business_owners', null=True, blank=True)
    sphere = models.CharField(max_length=100, null=True, blank=True)
    business_name = models.CharField(max_length=100, null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)



class Business(models.Model):
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE)
    budget = models.models.DecimalField(max_digits=10, decimal_places=2)
    conditions = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)



class BlockedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
