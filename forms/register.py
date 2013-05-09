__author__ = 'jurek'
from django import forms
from main.models import User
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User