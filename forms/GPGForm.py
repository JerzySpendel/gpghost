__author__ = 'jurek'
from django import forms
from main import models
from django.forms.widgets import RadioSelect
class GPGFormNew(forms.ModelForm):
    class Meta:
        model = models.Key
        exclude = ('ext_id','key_type','key_length','key_fingerprint','key_id')
class GPGManage(forms.Form):
    def __init__(self,user=None,post=None):
        forms.Form.__init__(self,post)
        if user != None:
            self.create(user)
    def create(self,user):
        choices = []
        keys = models.Key.objects.filter(ext_id=user)
        for key in keys:
            choices.append([None,key.key_email])
        counter = 1
        for choice in choices:
            choice[0] = counter
            counter = counter + 1
        self.fields['delete'] = forms.ChoiceField(widget=RadioSelect(),choices=choices)
    def deleteKey(self,number,gpg,user):
        self.keys = models.Key.objects.filter(ext_id=user)
        key = self.keys[int(number)-1]
        gpg.delete_keys(key.key_fingerprint)
        gpg.delete_keys(key.key_fingerprint,True)
        key.delete()
