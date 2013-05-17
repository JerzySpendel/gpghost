__author__ = 'jurek'
from django import forms
from main.models import User,Key
from Tools.FileTools import listFiles
class NewFileForm(forms.Form):
    file = forms.FileField()

    def addForm(self,user):
        choices = []
        keys = Key.objects.filter(ext_id=user)
        for key in keys:
            choices.append([key.key_email,key.key_email])
        self.fields['opcje'] = forms.ChoiceField(choices=choices)
class ManageForm(forms.Form):
    def __init__(self,user):
        forms.Form.__init__(self)
        self.user = user
    def addForm(self):
        files = listFiles(self.user.login)

