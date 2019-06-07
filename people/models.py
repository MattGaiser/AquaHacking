from django.db import models
import localflavor.ca.ca_provinces as flavor
import datetime
from django.utils import timezone

class Skill(models.Model):
    description = models.CharField(max_length=300)
    def __str__(self):
        return self.description

class Person(models.Model):
    name = models.CharField(max_length=50)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(default=0)
    occupation = models.CharField(max_length=50)
    skills = models.ManyToManyField(Skill)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=70)
    address = models.CharField(max_length=50)
    address_city = models.CharField(max_length=50)
    address_province = models.CharField(max_length=2, choices=flavor.PROVINCE_CHOICES)
    address_country = models.CharField(max_length=50, default="Canada")

    def __str__(self):
        return self.name

class Emergency(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        long_position = models.DecimalField(max_digits=8, decimal_places=3)
        lat_position = models.DecimalField(max_digits=8, decimal_places=3)
        RATING_CHOICES = (
            ('One', 'One : Anomaly'),
            ('Two', 'Two : Incident '),
            ('Three', 'Disaster with Local Consequences'),
            ('Four', 'State of Local Emergency'),
            ('Five', 'State of Emergency'),
        )
        rating = models.CharField(max_length=30,choices=RATING_CHOICES)

        def __str__(self):
            return self.title

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    time_assigned = models.DateTimeField(auto_now_add=True, blank=True)
    date_assigned = models.DateTimeField(auto_now_add=True, blank=True)
    person_assigned = models.ManyToManyField(Person)
    emergency = models.ForeignKey(Emergency, on_delete=models.CASCADE)
    skill_needed = models.ForeignKey(Skill, on_delete=models.CASCADE)
    long_position = models.DecimalField(max_digits=8, decimal_places=3)
    lat_position = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return self.title
