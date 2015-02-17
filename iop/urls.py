from django.conf.urls import patterns, include, url
from django.contrib import admin
#from website.views import *
from iop.views1 import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('website.views',
    url(r'^login/$','login_func'),
    url(r'^logout/$','logout_func'),
    url(r'^index/$','index'),
    url(r'^taskresult/$','task_result'),
    url(r'^taskconfig/$','task_config'),
    url(r'^registerpage/$','register_page'),
    url(r'^login_auth/$','login_auth'),                  
                        
)
#urlpatterns += patterns('iop.views',
    #url(r'^time/$','current_datetime'),
    #url(r'^time/plus/(\d{1,2})','hours_ahead'),
    #url(r'^meta/$','display_meta'),
#)



