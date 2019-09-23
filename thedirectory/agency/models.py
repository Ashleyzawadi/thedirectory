from django.db import models

# Create your models here.

class Agency(models.Model):
    agencyname = models.CharField(max_length = 200)
    registration_no = models.IntegerField(max_length=200)
    agency_logo = models.ImageField(default='default.jpg')

   

class Agent(models.Model):
    name = models.CharField(max_length = 100)
    agency = models.ForeignKey(Agency, on_delete=models.Cascade, blank =True)
    registration_no = models.IntegerField(max_length=100)
    email = models.EmailField()
    phone_no = models.IntegerField(max_length=10)


