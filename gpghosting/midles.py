__author__ = 'jurek'
import re, gnupg
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.conf import settings
class Sesja(object):
    def process_request(self,request):
        path = request.get_full_path()
        pat = re.compile(r'^/main.*')
        if not request.session.get('logged',False) and pat.match(path):
            return HttpResponseForbidden(content="You're not allowed to be here")
        if request.session.get('logged',False) and not pat.match(path):
            return redirect('/main')
def gpgobject(request):
    gpg = gnupg.GPG(gnupghome=settings.GNUPGHOME)
    gpg.encoding = 'utf-8'
    return {'gpg':gpg}