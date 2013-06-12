__author__ = 'jurek'
from django.conf import settings
import os
from collections import OrderedDict
class Display(object):  #class for displaying uniform set of rename for, delete form and links, in other words just wrapper for data to display in view :}
    def __init__(self,kvars):
        print('kvars: ',kvars)
        self.forms = OrderedDict()  #set for forms
        self.iters = OrderedDict()  #set for iterators got from self.forms
        for i in kvars.keys():
            self.forms[i] = kvars[i]
            self.iters[i] = iter(self.forms[i])
    def reset(self):
        for key in self.forms.keys():
            self.iters[key] = iter(self.forms[key])
    def nextPlease(self): #Next portion of data to display as a list with rename form, delete form and link
        please = []
        for iterator in self.iters.values():
            please.append(next(iterator))
        return please
    def __iter__(self):
        return self
    def __next__(self):
        return self.nextPlease()
# "data" argument is data from form (form.data) containing
# information about selected pools
# request is request object which contain user info
def deleteGivenFiles(data,request):
    login = request.session['user'].login
    path = settings.PATH+'files/'+login+'/'
    for file in data:
        if file != 'csrfmiddlewaretoken':
            os.remove(path+file)
