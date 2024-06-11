from django.db import models

# Create your models here.
from django.db import models

class Customer(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=12)
    phone = models.CharField(max_length=10)
    accno = models.PositiveBigIntegerField()

