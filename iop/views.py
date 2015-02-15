#from django.utils.timezone import now, timedelta
#from django.db import connection
#from django.contrib.auth.views import login, logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response

from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.template.context import RequestContext
from .iop_forms import LoginForm

@login_required()
def index(request):
    return render_to_response('index.html')

#### Page return ####
def login_func(request):
    return render_to_response('login.html')

def register_page(request):
    return render_to_response('register.html')

##### Auth #####
def login_auth(request):
    if request.method == 'GET': 
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            
            print user
            
            if user is not None: 
                if user.is_active:
                    #auth.login(request, user)
                    return render_to_response("index.html",RequestContext(request))
                else:
                    return render_to_response("login.html",RequestContext(request,{'form': form,'fail_reason':'Password is invalid!'}))
            else:
                return render_to_response("login.html",RequestContext(request,{'form': form,'fail_reason':'Username and Password is invalid!'}))
                
        else:
            return render_to_response("login.html",RequestContext(request,{'form': form,}))
        
        
        
        
def logout(request):
    #auth.logout(request)
    return HttpResponseRedirect("/account/loggedout/")

def registeruser(request):
    pass



























