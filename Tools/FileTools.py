__author__ = 'jurek'
from django.conf import settings
import os
def handle_file(f,user):
    DIR = '/home/jurek/PycharmProjects/gpghosting/files/'+user.login+'/'
    with open(DIR+f.name,'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)
def listFiles(user):
    path_to_files = settings.PATH
    user_path = path_to_files + 'files/'+user.login
    return os.listdir(user_path)
