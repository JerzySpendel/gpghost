__author__ = 'jurek'
from django.conf import settings
import os
def toPairs(lista):
    i = iter(lista)
    return zip(i,i)
def toPairs(lista1,lista2):
    i1 = iter(lista1)
    i2 = iter(lista2)
    return zip(i1,i2)
def toTriples(l1,l2,l3):
    i1 = iter(l1)
    i2 = iter(l2)
    i3 = iter(l3)
    return zip(i1,i2,i3)
def deleteGivenFiles(data,request):
    login = request.session['user'].login
    path = settings.PATH+'files/'+login+'/'
    for file in data:
        if file != 'csrfmiddlewaretoken':
            os.remove(path+file)