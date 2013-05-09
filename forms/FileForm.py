__author__ = 'jurek'
from django import forms
from main.models import User,Key
class NewFileForm(forms.Form):
    def addForm(self,user):
        choices = []
        keys = Key.objects.filter(ext_id=user)
        for key in keys:
            choices.append([None,key.key_email])
        counter = 1
        for choice in choices:
            choice[0] = counter
            counter = counter + 1
        self.fields['opcje'] = forms.ChoiceField(choices=choices)