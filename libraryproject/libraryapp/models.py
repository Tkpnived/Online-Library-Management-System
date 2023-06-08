from django.db import models

# Create your models here.
class logindb(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    Phone = models.IntegerField(null=True)
    Mobile = models.IntegerField(null=True)
    Address=models.TextField(max_length=100,null=True)

    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)