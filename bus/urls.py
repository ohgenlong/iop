# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('',
   url(r'^asset/$',
       'inventory.views.asset_manage', name='asset_list'),
   url(r'^asset/(?P<asset_type>\w+)/$',
       'inventory.views.asset_manage', name='asset_type_list'),
   url(r'^asset/(?P<asset_type>\w+)/(?P<asset_id>\d+)/$',
       'inventory.views.asset_manage', name='asset_manage'),
)




