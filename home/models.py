from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    contact = models.IntegerField()
    image = models.ImageField(null=True,blank=True)
    file = models.FileField(null=True,blank=True)

