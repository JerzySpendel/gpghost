__author__ = 'jurek'
from django import forms
from main import models
from django.forms.widgets import RadioSelect
class GPGFormNew(forms.ModelForm):
    class Meta:
        model = models.Key
        exclude = ('ext_id','key_type','key_length','key_fingerprint','key_id')
class GPGManage(forms.Form):
    def create(self,user):
        choices = []
        keys = models.Key.objects.filter(ext_id=user)
        for key in keys:
            choices.append([None,key.key_email])
        counter = 1
        for choice in choices:
            choice[0] = counter
            counter = counter + 1
        self.fields['opcje'] = forms.ChoiceField(widget=RadioSelect(),choices=choices)

