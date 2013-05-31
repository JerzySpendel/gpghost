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
        self.fields['password'] = forms.CharField(max_length=100)
class DeleteForm(forms.Form):
    def __init__(self,post=None,user=None):
        forms.Form.__init__(self,post)
        if user != None:
            self.addForm(user)
    def addForm(self,user):
        self.user = user
        files = listFiles(self.user)
        for file in files:
            self.fields[file] = forms.BooleanField(label=file)
    def __len__(self):
        i = iter(self)
        counter = 0
        for a in i:
            counter += 1
        return counter
class RenameForm(forms.Form):
    def __init__(self,post=None,user=None):
        forms.Form.__init__(self,post)
        if user != None:
            self.addForm(user)
    def addForm(self,user):
        self.user = user
        files = listFiles(user)
        for file in files:
            self.fields[file] = forms.BooleanField(label=file)
    def __len__(self):
        i = iter(self)
        counter = 0
        for a in i:
            counter += 1
        return counter