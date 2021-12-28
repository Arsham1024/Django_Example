from django.db import models

class Pet(models.Model):
    SEX_CHOICES = [('M', "Male") , ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=100 , blank=True)
    breed = models.CharField(max_length=30 , blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True) # instead of blank=True, because blank stores 0 and here it would be confused with age
    vaccination = models.ManyToManyField("Vaccine" , blank=True) # first argument is the class it is related to

class Vaccine(models.Model):
    name = models.CharField(max_length=100)


