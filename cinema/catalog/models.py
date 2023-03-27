from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(blank=False, max_length=20)
    sur_name = models.CharField(blank=False, max_length=20)
    second_name = models.CharField(blank=False, max_length=20)
    age = models.IntegerField(blank=False, max_length=4)
    gender = models.CharField(blank=False, max_length=20)
    

    

class Cinema(models.Model):
    name = models.CharField(blank=False, max_length=20)
    gender_rate = models.IntegerField(blank=False, max_length=4)
