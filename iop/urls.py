from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('app01.views',
    # Examples:
    # url(r'^$', 'iop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'index'),
    url(r'^report/','report'),
    url(r'^cpk/','catch_package'),
    url(r'^pkg/','package'),

)

urlpatterns += patterns('library.views',
    url(r'^search/$','search'),
    url(r'^contact/$','contact'),
                       
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^debuginfo/$','library.views.contact')
    
    
    
    )