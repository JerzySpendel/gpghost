__author__ = 'jurek'
from django.conf import settings
import os
def toPairs(lista):
    i = iter(lista)
    return zip(i,i)
def deleteGivenFiles(data,request):
    login = request.session['user'].login
    path = settings.PATH+'files/'+login+'/'
    for file in data:
        if file != 'csrfmiddlewaretoken':
            os.remove(path+file)