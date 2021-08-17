from django.db import models
from django.db.models.base import Model

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    msg = models.TextField()

    def __str__(self):
        return self.fname + " " +self.lname
    
    
    