__author__ = 'jurek'
def handle_file(f,user):
    DIR = '/home/jurek/PycharmProjects/gpghosting/files/'+user.login+'/'
    with open(DIR+f.name,'wb+') as file:
        for chunk in f.chunks():
            file.write(chunk)
