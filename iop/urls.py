from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$','iop.views.dashboard', name='dashboard'),                    
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^dash_search/$', 'iop.views.search', name='dash_search'),
    url(r'^login_auth/$','iop.views.login_auth',name='login_auth'), 
    url(r'^login/$','iop.views.login_func',name='login'),
    url(r'^logout/$','iop.views.logout_func',name='logout'),
    url(r'^taskresult/$','iop.views.task_result'),
    url(r'^taskconfig/$','iop.views.task_config'),
    url(r'^registerpage/$','iop.views.register_page'),
    url(r'^bus/',include('bus.urls', namespace='business')),
    url(r'^inv/',include('inv.urls', namespace='inventory')),
    url(r'^api/',include('api.urls', namespace='api')),
    url(r'^idc/',include('idc.urls', namespace='idc')),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






