from django.shortcuts import render_to_response
from django.template import RequestContext



def custom_proc(request):
    "A context processor that provides 'app', 'user' and 'ip_address'."
    return {
        'APP': 'My app',
        'USER': request.user,
        'IP_ADDRESS': request.META['REMOTE_ADDR'],
        'meta_data': request.META.items(),
        'username': request.session.get('username','nobody'),
    }