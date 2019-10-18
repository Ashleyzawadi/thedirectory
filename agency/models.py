from django.db import models

# Create your models here.

class Agency(models.Model):
    agencyname = models.CharField(max_length = 200)
    registration_no = models.IntegerField()
    agency_logo = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.agencyname

    class Meta:
        ordering = ['agencyname']

    @classmethod
    def search_by_name(cls,search_term):
        agency = cls.objects.filter(agenncyname__icontains=search_term)
        return agency

class Agent(models.Model):
    name = models.CharField(max_length = 100)
    agency = models.ForeignKey(Agency,on_delete=models.CASCADE,blank =True)
    registration_no = models.IntegerField()
    email = models.EmailField()
    phone_no = models.IntegerField()


