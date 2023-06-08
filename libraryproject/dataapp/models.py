from django.db import models

from datetime import date, timedelta

# Create your models here.
def get_default_start_date():
    return date.today()

class catdb(models.Model):

    CategoryName = models.CharField(max_length=100)
    Description = models.CharField(max_length=100)
    Image = models.ImageField()

class prodb(models.Model):

    CategoryName = models.CharField(max_length=100)
    BookName=models.CharField(max_length=100)
    AutherName = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Price=models.IntegerField()
    qty=models.IntegerField()


    Image = models.ImageField()

class req(models.Model):
    Username=models.CharField(max_length=100,null=True)
    Email=models.EmailField(null=True)
    BookName=models.CharField(max_length=100)
    AutherName = models.CharField(max_length=100)
    Language = models.CharField(max_length=100,null=True)
    Price=models.IntegerField()
    qty=models.IntegerField()

class acceptdb(models.Model):
    Username=models.CharField(max_length=100,null=True)
    Email=models.EmailField(null=True)
    BookName=models.CharField(max_length=100)
    AutherName = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Price=models.IntegerField(null=True)
    qty=models.IntegerField()
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.end_date = self.start_date + timedelta(days=5)
        print("Save method executed")
        super().save(*args, **kwargs)

class returnbook(models.Model):
    Username=models.CharField(max_length=100,null=True)
    Email=models.EmailField(null=True)
    BookName=models.CharField(max_length=100)
    AutherName = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)

    Price=models.IntegerField()
    qty=models.IntegerField()
    Due = models.CharField(max_length=100,null=True)
    DuePrice = models.CharField(max_length=100,null=True)
    TotalPrice = models.IntegerField(null=True)
    start_date = models.CharField(max_length=100,null=True)
    end_date = models.CharField(max_length=100,null=True)

class cancel(models.Model):
    Username=models.CharField(max_length=100,null=True)
    Email=models.EmailField(null=True)
    BookName=models.CharField(max_length=100)
    AutherName = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Price=models.IntegerField()
    qty=models.IntegerField()

class Payment(models.Model):

    BookName=models.CharField(max_length=100)
    AutherName = models.CharField(max_length=100)
    Due=models.CharField(max_length=100)
    BookPrice=models.IntegerField(null=True)
    DuePrice = models.CharField(max_length=100,null=True)
    TotalPrice = models.IntegerField(null=True)


class payments(models.Model):
    Username = models.CharField(max_length=100, null=True)

    BookName=models.CharField(max_length=100)
    Due=models.CharField(max_length=100)
    BookPrice=models.IntegerField(null=True)
    DuePrice = models.CharField(max_length=100,null=True)
    TotalPrice = models.IntegerField(null=True)


class complect(models.Model):
    Username = models.CharField(max_length=100, null=True)

    BookName=models.CharField(max_length=100)
    Due=models.CharField(max_length=100)
    BookPrice=models.IntegerField(null=True)
    DuePrice = models.CharField(max_length=100,null=True)
    TotalPrice = models.IntegerField(null=True)

