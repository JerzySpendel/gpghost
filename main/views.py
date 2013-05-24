# Create your views here.
from django.http import HttpResponse
from forms.register import RegisterForm
from forms.login import LoginForm
from django.shortcuts import render,redirect
from main.models import User,Key
import hashlib, os
from django.template import RequestContext
from forms.GPGForm import GPGFormNew, GPGManage
from Tools.KeyTools import GenerateKey
from forms.FileForm import NewFileForm,ManageForm
from Tools.FileTools import handle_file,listFiles
from Tools import Tools
def managef(request):
    if request.method == "POST":
        form = NewFileForm(request.POST,request.FILES)
        if form.is_valid():
            handle_file(request.FILES['file'],request.session['user'])
            return HttpResponse("hehehhehehe")
    else:
        form = NewFileForm()
        form.addForm(request.session['user'])
        return render(request,'managef.html',{'file_form':form})
def manage(request):
    if request.method == 'POST' and 'key_password' in request.POST:
        form = GPGFormNew(request.POST)
        key_to_save = form.save(commit=False)
        key_to_save.ext_id = request.session['user']
        key_to_save.key_type = "RSA"
        key_to_save.key_length = 2048
        print(request.POST.keys())
        if not key_to_save.isAlready():
            gpg = RequestContext(request)['gpg']
            GenerateKey(key_to_save,gpg).start() #Send gpg and key_to_save objects to another thread to be processed, now we will just send HttpResponse to make them happy
            return render(request,'base.html',{'message_m':'Generating keys will take up to 10 minutes. We will send you notification via email if its done'})
        else:
            return render(request,'base.html',{'message_m':'There is already key with that email'})
    elif request.method == 'POST' and 'delete' in request.POST:
        form_manage = GPGManage(post=request.POST)
        print(form_manage.data['delete'])
        form_manage.deleteKey(form_manage.data['delete'],RequestContext(request)['gpg'],request.session['user'])
        return render(request,'base.html',{'messagem_m':'Key deleted'})
    else:
        a = Key(key_email=request.session['user'].email,ext_id=request.session['user'],key_length=2048,key_real="Name and surname",key_comment="Additional description for this key",key_password="password")
        form = GPGFormNew(instance=a)
        form_manage = GPGManage(user=request.session['user'])
        print(request.POST.keys())
        return render(request,'manage.html',{'form':form,'form_manage':form_manage})
def logout(request):
    if request.session.get('logged',False):
        request.session['logged'] = False
        request.session['user'] = None
        return render(request,'base.html',{'message_m':'Have a nice day'})
    else:
        return render(request,'base.html',{'message_m':"You're not logged in"})
def index(request):
    return render(request,"index.html",{})
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            password = hashlib.md5()
            password.update(form.cleaned_data['password'].encode('utf-8'))
            password = str(password.hexdigest())
            login = form.cleaned_data['login']
            users = User.objects.filter(login=login)
            if users.count() > 1 or users.count() == 0:
                return HttpResponse("Error, more than one or 0 users with such a username")
            user = User.objects.get(login=login)
            if user:
                if password == user.password:
                    request.session.set_expiry(60*60*60)
                    request.session['logged'] = True
                    request.session['user'] = user
                    return redirect('/main')
                else:
                    return HttpResponse("Bad password or login")
            else:
                return HttpResponse("There's no such a user")
        else:
            return HttpResponse("Bad password")
    else:
        return render(request,"login.html",{'form':LoginForm})
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = hashlib.md5()
            password.update(form.cleaned_data['password'].encode('utf-8'))
            password = str(password.hexdigest())
            login = form.cleaned_data['login']
            email = form.cleaned_data['email']
            if not User.objects.filter(login=login).count():
                user = User.objects.create(login=login,password=password,email=email)
                user.save()
                if not os.path.exists('/home/jurek/PycharmProjects/gpghosting/files/'+login):
                    os.mkdir('/home/jurek/PycharmProjects/gpghosting/files/'+login)
                return render(request,'gratz.html',{'login':login,'gratulowac':True})
            else:
                return render(request,'gratz.html',{'gratulowac':False})
    else:
        return render(request,'register.html',{'form':RegisterForm})
def main(request):
    if request.method == "POST":
        form = ManageForm(post=request.POST,user=request.session['user'])
        Tools.deleteGivenFiles(form.data,request)
        return render(request,'base.html',{'message_m':'Files deleted'})
    else:
        form = ManageForm()
        form.addForm(request.session['user'])
    return render(request,"main.html",{'forms':form})