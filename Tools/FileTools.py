__author__ = 'jurek'
from django.conf import settings
from django.template import RequestContext
from main.models import Key
import os
def handle_file(f,user,email,request,password):
    DIR = '/home/jurek/PycharmProjects/gpghosting/files/'+user.login+'/'
    with open(DIR+f.name,'wb+') as file: #"f" - file wrapper sent from request, "file" - new file
        for chunk in f.chunks():
            file.write(chunk)
    fileDir = DIR+f.name
    key = Key.objects.get(key_email=email)
    gpg = RequestContext(request)['gpg']
    data = gpg.encrypt_file(open(fileDir,'rb'),[key.key_email],armor=False,output=fileDir+'.pgp')
def listFiles(user):
    path_to_files = settings.PATH
    user_path = path_to_files + 'files/'+user.login
    return [file for file in os.listdir(user_path) if not file.startswith(".")]
def getUserFilePath(user):
    login = user.login
    return settings.PATH+'files/'+login+'/'
def prepareLinks(user,form):
    names = [name.label for name in form]
    login = user.login
    link = settings.LINK
    links = []
    for name in names:
        links.append(link+'download/?u='+login+'&f='+name)
    return links

