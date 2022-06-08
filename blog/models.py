from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class crudst(models.Model):
    stname=models.CharField(max_length=200)
    stemail=models.CharField(max_length=100)
    staddress=models.CharField(max_length=150)
    stmobile=models.IntegerField()
    stgender=models.CharField(max_length=1)

class crudst1(models.Model):
    dname=models.CharField(max_length=200)
    dversion=models.IntegerField()
    nameofcustomer=models.CharField(max_length=150)
    customermobileno=models.IntegerField()
    dateofselling=models.DateField()    

class Data(models.Model):
   
    name=models.CharField(max_length=50)
    # mem_id=models.CharField(max_length=5,blank=True)
    milktype=models.CharField(max_length=50,blank=True)
    fat=models.FloatField(max_length=10)
    snf=models.FloatField(max_length=10)
    clr=models.FloatField(max_length=10)
    water=models.FloatField(max_length=10)
    temp=models.FloatField(max_length=10)
    weight=models.FloatField(max_length=10)
    price=models.FloatField(max_length=10)
    time=models.TimeField()
    