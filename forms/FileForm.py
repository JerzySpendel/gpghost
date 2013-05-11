__author__ = 'jurek'
from django import forms
from main.models import User,Key
class NewFileForm(forms.Form):
    file = forms.FileField()

    def addForm(self,user):
        choices = []
        keys = Key.objects.filter(ext_id=user)
        for key in keys:
            choices.append([key.key_email,key.key_email])
        self.fields['opcje'] = forms.ChoiceField(choices=choices)