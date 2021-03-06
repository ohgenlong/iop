#from django.utils.timezone import now, timedelta
#from django.db import connection
#from django.contrib.auth.views import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.template.context import RequestContext
from website.form_sets import LoginForm, TaskForm

# Login Auth ...................................................................
def login_func(request):
    return render_to_response('login.html')

def register_page(request):
    return render_to_response('register.html')

def logout_func(request):
    auth.logout(request)
    return HttpResponseRedirect("/login/")

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
        
            if user is not None: 
                if user.is_active:
                    request.session['username'] = username
                    auth.login(request, user)
                    return HttpResponseRedirect("/")
                    
                else:
                    return render_to_response("login.html",RequestContext(request,{'form': form,'fail_reason':'Password is invalid!'}))
            else:
                return render_to_response("login.html",RequestContext(request,{'form': form,'fail_reason':'Username and Password is invalid!'}))
                
        else:
            return render_to_response("login.html",RequestContext(request,{'form': form,}))
        





@login_required()
def dashboard(request):
    return render_to_response('dashboard.html',RequestContext(request))

@login_required()
def task_result(request):
    return render_to_response('task_result.html',RequestContext(request))

@login_required()
def task_config(request):
    if request.method == 'GET': 
        form = TaskForm()
        return render_to_response('task_config.html', RequestContext(request, {'form': form,}))
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        return render_to_response('task_config.html', RequestContext(request, {'form': form,}))

def registeruser(request):
    pass



























