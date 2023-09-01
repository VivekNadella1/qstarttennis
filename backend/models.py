from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class PrivateLesson(models.Model):
    childs_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone_number = PhoneNumberField() 
    
    COACH_CHOICES = [
        ('Brandon', 'Brandon'),
        ('Vishal', 'Vishal'),
        ('Ansh', 'Ansh'),
         ('Ishan', 'Ishan'),
         ('Shravan', 'Shravan'),
         ('Yajat', 'Yajat'),

    ]
    preferred_coach = models.CharField(max_length=20, choices=COACH_CHOICES, blank=True)
    

class GroupLesson(models.Model):
    childs_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone_number = PhoneNumberField() 

class Volunteer(models.Model):
    full_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone_number = PhoneNumberField()  
    skills = models.CharField(max_length=500, default='')

class EventSignup(models.Model):
    full_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_phone_number = PhoneNumberField()  
    TOURNAMENT_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    participating_in_tournament = models.CharField(max_length=5, choices=TOURNAMENT_CHOICES, default='No')