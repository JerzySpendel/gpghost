__author__ = 'jurek'
from django import forms
class LoginForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=100)