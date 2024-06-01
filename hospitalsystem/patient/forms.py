from django import forms
from django.contrib.auth.models import User
from . import models


class PatientUserForm_(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class PatientForm_(forms.ModelForm):
    
    class Meta:
        model=models.Patientt
        fields=['age','bloodgroup','disease','address','doctorname','mobile','profile_pic']
