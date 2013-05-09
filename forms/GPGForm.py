__author__ = 'jurek'
from django import forms
from main import models
class GPGFormNew(forms.ModelForm):
    class Meta:
        model = models.Key
        exclude = ('ext_id','key_type','key_length','key_fingerprint','key_id')
