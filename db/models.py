#coding=utf-8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save


#constant
GENDER_CHOICES = (
    ('0','Unknown'),
    ('1','Male'),
    ('2','Female'),
    ('9','not applicatable'))   
    
'''      see if is qualified
TIME_CHOICES = (
     ('0', 'Monday_morning'),
     ('1', 'Monday_afternoon'),
     ('2', 'Monday_evening'),
     ('3', 'Tuesday_morning'),
     ........
     ('20', 'Sunday_evening'),     
                )
'''

# Create your models here.

class TutorRequest(models.Model):
    applicant_name = models.CharField(max_length = 20)
    mobile_number = models.CharField(max_length = 20)
    address = models.CharField(max_length = 150)
    additional_info = models.TextField()
    

class Subject(models.Model):
    name = models.CharField(max_length=50)

class TimePeriod(models.Model):
    description = models.CharField(max_length = 20)
    def __unicode__(self):
            return self.description
    

class District(models.Model):
    name = models.CharField(max_length=40,blank = True, null = True)
    

class School(models.Model):
    name = models.CharField(max_length=40,blank = True, null = True)

def file_name(instance):
    return '/'.join['potrait',str(instance.userprofile.id)]
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name = 'profile')
    name = models.CharField(max_length=30, blank=True, null = True)
    GENDER_CHOICE = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    gender = models.CharField(max_length=2,choices = GENDER_CHOICE)
    email = models.EmailField(null=True,blank=True)
    school = models.CharField(max_length=40,blank = True, null = True)
    subject = models.ForeignKey(Subject, blank = True, null = True)
    cellphone = models.CharField(max_length=40,blank = True, null = True)
    honour = models.CharField(max_length=200,blank = True, null = True)
    speciality = models.CharField(max_length=200,blank = True, null = True)
    additional_info =  models.CharField(max_length=500,blank = True, null = True)
    course = models.CharField(max_length=200,blank = True)
    time_period = models.ManyToManyField(TimePeriod, null = True, related_name = 'user')
    area = models.ManyToManyField(District, blank = True, related_name = 'user')
    taobao_link = models.URLField(blank = True,null = True)
    confirmed = models.BooleanField(default = False)
    potrait = models.ImageField(upload_to = file_name,blank = True, null = True)
    salary_per_hour = models.PositiveIntegerField(default = 0)
    def __unicode__(self):
            return self.user.username
  
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create user profile for new users at save user time, if it doesn't already exist
    """
    if created:
        p = UserProfile(user=instance)
        p.save()

post_save.connect(create_user_profile, sender=User)
 

