from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.timezone import now, timedelta
from django.contrib import auth
from django.shortcuts import render_to_response
from django.db import connection
from library.models import *
from django.core.mail import send_mail
from library.form import ContactForm

def search(request):
    errors = []
    if 'q' in request.GET:
            q = request.GET['q']
            if not q:
                errors.append('Enter a search term.')
            elif len(q) > 20:
                errors.append('Please enter at most 20 characters.')
            else:
                books = Book.objects.filter(title__icontains=q)
                return render_to_response('search_form.html',{'books': books, 'query': q})
            
    return render_to_response('search_form.html',{'errors': errors})


def contact(request):
    #errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                      cd['subject'],
                      cd['message'],
                      cd.get('email', ''),
                      ['ohgenlong@126.com'],
                      )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
        
    return render_to_response('search_form.html',{'form': form})