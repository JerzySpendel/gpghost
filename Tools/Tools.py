__author__ = 'jurek'
from django.conf import settings
import os
class Display(object):  #class for displaying uniform set of rename for, delete form and links, in other words just wrapper for data to display in view :}
    def __init__(self,**kvars):
        if 'formR' in kvars:
            self.formR = kvars['formR']
            self.iR = iter(self.formR) # iterator for fields in rename form
        if 'formD' in kvars:
            self.formD = kvars['formD']
            self.iD = iter(self.formD) # iterator for fields in delete form
        if 'links' in kvars:
            self.links = kvars['links']
            self.iL = iter(self.links) # iterator for list with links to each file
        self._check()
    def reset(self):
        if self.formR:
            self.iR = iter(self.formR)
        if self.formD:
            self.iD = iter(self.formD)
        if self.links:
            self.iL = iter(self.links)
    def nextPlease(self): #Next portion of data to display as a list with rename form, delete form and link
        d = next(self.iD)
        r = next(self.iR)
        l = next(self.iL)
        if d.label.count('.pgp') >= 1:
            d.sec = True
        else:
            d.sec = False
        self.curID = d
        self.curIR = r
        self.curIL = l
        return (d,r,l)
    def nextR(self):  #next rename form got from self.iR iterator
        self.curIR = next(self.iR)
        return self.curIR
    def nextD(self):  #next delete form got from self.iD iterator
        n = next(self.iD)
        if n.label.count('.pgp') >= 1:
            n.sec = True
        else:
            n.sec = False
        self.curID = n
        return n
    def nextLink(self):  #next link got from self.iL iterator
        self.curIL = next(self.iL)
        return self.curIR
    def __iter__(self):
        return self
    def __next__(self):
        return self.nextPlease()
    def _check(self):
        if self.formR and self.formD and self.links:
            if len(self.formR) != len(self.formD) and (len(self.formR) != len(self.links)):
                raise Exception('Different sizes between formR,formD and links')
# "data" argument is data from form (form.data) containing
# information about selected pools
# request is request object which contain user info
def deleteGivenFiles(data,request):
    login = request.session['user'].login
    path = settings.PATH+'files/'+login+'/'
    for file in data:
        if file != 'csrfmiddlewaretoken':
            os.remove(path+file)
