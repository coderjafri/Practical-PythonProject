from django.db import models

# Create your models here.

class contarct(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    msg=models.CharField(max_length=250)
    
