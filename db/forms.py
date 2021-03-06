from django import forms
from django.forms import ModelForm
import re
from django.contrib.auth.models import User
from db.models import *


'''
class ProfileChangeForm(forms.Form):
    name = forms.CharField(label='Name',max_length=30, required = False)
    school = forms.CharField(label='School',max_length=40,required = False)
    subject = forms.CharField(label='Subject',required = False)
    cellphone = forms.CharField(label='Cellphone',max_length=40,required = False)
    honour = forms.CharField(label='Honour',max_length=200,required = False)
    speciality = forms.CharField(label='Speciality',max_length=200,required = False)
    additional_info =  forms.CharField(label='Additional_info',max_length=500,required = False)
    course = forms.CharField(label='Course',max_length=200,required = False)
    area = forms.CharField(label='Area',max_length=200,required = False)
    time_period = forms.CharField(label='TimePeriod')
    potrait = forms.ImageField(required = False)
'''

class ProfileChangeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfileChangeForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = UserProfile
        exclude =['user','taobao_link','confirmed','potrait']
        widgets = {
            'area': forms.CheckboxSelectMultiple(),
            'time_period': forms.CheckboxSelectMultiple(),
        }
        
class UploadImageForm(forms.Form):
    image  = forms.ImageField()         
