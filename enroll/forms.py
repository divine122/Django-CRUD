from django.core import validators
from .models import User
from django import forms

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']