from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.timezone import now, timedelta
from django.contrib import auth
from django.shortcuts import render_to_response
from django.db import connection

def index(request):
    return render_to_response('index.html')

def report(request):
    return render_to_response('report.html')

def catch_package(request):
    return render_to_response('catch_package.html')


def package(request):
    
    
    
    return HttpResponse('F:\work\abc.zip')
# Create your views here.
