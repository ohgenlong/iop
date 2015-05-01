# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Supplier url
    url(r'^supplier/$',
       'inv.views.supplier_manage', name='supplier_list'),
                       
    url(r'^supplier/(?P<supplier_id>\d+)/$',
        'inv.views.supplier_manage', name='supplier_manage'),
   
    # Server url                  
    url(r'^server_part/$', 
        'inv.views.server_part_manage',name='server_part_list'),
                        
    url(r'^server_part/(?P<part_name>\w+)/$',
        'inv.views.server_part_manage', name='server_part_type_list'),
                        
    url(r'^server_part/(?P<part_name>\w+)/(?P<type_id>\d+)/$',
        'inv.views.server_part_manage', name='server_part_manage'),
    
    # Template url                                    
    url(r'^template/$',
        'inv.views.template_manage', name='template_list'),
                        
    url(r'^template/(?P<template_type>\w+)/$',
        'inv.views.template_manage', name='template_type_list'),
                        
    url(r'^template/(?P<template_type>\w+)/(?P<template_id>\d+)/$',
        'inv.views.template_manage', name='template_manage'),
                        
    url(r'^template/(?P<template_type>\w+)/(?P<template_id>\d+)/io/(?P<io_type>\w+)/$',
        'inv.views.template_io_manage', name='template_io_manage'),
#    
#    # Asset url
#    url(r'^asset/$',
#        'inv.views.asset_manage', name='asset_list'),
#                        
#    url(r'^asset/(?P<asset_type>\w+)/$',
#        'inv.views.asset_manage', name='asset_type_list'),
#                        
#    url(r'^asset/(?P<asset_type>\w+)/(?P<asset_id>\d+)/$',
#        'inv.views.asset_manage', name='asset_manage'),
)








