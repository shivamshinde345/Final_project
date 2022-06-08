from django.db import models

# Create your models here.
class devices(models.Model):
    dname=models.CharField(max_length=200)
    dversion=models.IntegerField()
    nameofcustomer=models.CharField(max_length=150)
    customermobileno=models.IntegerField()
    dateofselling=models.DateField()