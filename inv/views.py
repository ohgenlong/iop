# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from inv.models import *
from inv.forms import *


@login_required
def supplier_manage(request, supplier_id=None):
    """
    Manage supplier
    """
    
    page_name = u"Supplier"
    if supplier_id:
        supplier = get_object_or_404(Supplier, pk=supplier_id)
        page_name = u"Edit " + page_name
        
        if request.method == 'POST':
            form = SupplierForm(request.POST, instance=supplier)
            operate = request.POST.get('operate')
            if form.is_valid():
                if operate == 'update':
                    form.save()
                    messages.success(request, u'Supplier (%s) Update Success!' % supplier.name)
                    return HttpResponseRedirect(reverse('inventory:supplier_list'))
                elif operate == 'delete':
                    supplier.delete()
                    messages.success(request, u'Supplier (%s) Delete Success!' % supplier.name)
                    return HttpResponseRedirect(reverse('inventory:supplier_list'))
                else:
                    messages.warning(request, u'Dont support %s operation!' % operate)
        else:
            form = SupplierForm(instance=supplier)
        return render(request, 'inv/supplier.html', {
                      "page_name": page_name,
                      "form": form,
        })
    else:
        supplier = Supplier()
        if request.method == 'POST':
            operate = request.POST.get('operate')
            form = SupplierForm(request.POST, instance=supplier)
            if form.is_valid():
                if operate == 'add':
                    supplier = form.save()
                    messages.success(request, u'Supplier (%s) Add Success!' % supplier.name)
                    return HttpResponseRedirect(reverse('inventory:supplier_list'))
                else:
                    messages.warning(request, u'Dont support %s operation!' % operate)
        else:
            form = SupplierForm(instance=supplier)
        all_supplier = Supplier.objects.all()
        return render(request, 'inv/supplier_list.html', {
                      "form": form,
                      "page_name": page_name,
                      "all_supplier": all_supplier,
                      })

# Server Parts Map
server_parts_map = {
    'cpu': {
        'model': ServerCPU,
        'form': ServerCPUForm,
        'name': u'Server CPU',
        'color': 'bg-green',
        'icon': 'ion-jet',
    },
    'memory': {
        'model': ServerMemory,
        'form': ServerMemoryForm,
        'name': u'Server MEM',
        'color': 'bg-yellow',
        'icon': 'ion-android-send',
    },
    'hd': {
        'model': ServerHD,
        'form': ServerHDForm,
        'name': u'Server DISK',
        'color': 'bg-blue',
        'icon': 'ion-record',
    },
    'raidlevel': {
        'model': ServerRaidLevel,
        'form': ServerRaidLevelForm,
        'name': u'Server RAIDLEVEL',
        'color': 'bg-purple',
        'icon': 'ion-stats-bars',
    },
    'raidcard': {
        'model': ServerRaidCard,
        'form': ServerRaidCardForm,
        'name': u'Server RAIDCARD',
        'color': 'bg-teal',
        'icon': 'ion-umbrella',
    },
    'nic': {
        'model': ServerNIC,
        'form': ServerNICForm,
        'name': u'Server NIC',
        'color': 'bg-aqua',
        'icon': 'ion-wifi',
    },
}


templates_map = {
    'server': {
        'model': ServerAssetTemplate,
        'form': ServerAssetTemplateForm,
        'name': u'Server Template',
        'color': 'bg-green',
        'icon': 'ion-android-storage',
        'io_map': {
            'hds': {
                'name': u'Disk',
                'model': ServerTemplateHDS,
                'form': ServerTemplateHDSForm,
            },
            'nics': {
                'name': u'Nic',
                'model': ServerTemplateNICS,
                'form': ServerTemplateNICSForm,
            },
        },
    },
    'switch': {
        'model': SwitchAssetTemplate,
        'form': SwitchAssetTemplateForm,
        'name': u'Switch Template',
        'color': 'bg-aqua',
        'icon': 'ion-radio-waves',
    }
}

@login_required
def server_part_manage(request, part_name=None, type_id=None):
    """
    Manage part type for server
    """
    """
    1. Show All Type Server Parts 
    """
    if not part_name:
        page_name = u'Server Parts'
        part_order = ['cpu', 'memory', 'hd', 'nic', 'raidlevel', 'raidcard']
        all_part = []
        for each_part in part_order:
            all_part.append({
                'name': server_parts_map[each_part]['name'],
                'number': server_parts_map[each_part]['model'].objects.count(),
                'icon': server_parts_map[each_part]['icon'],
                'color': server_parts_map[each_part]['color'],
                'url': reverse('inventory:server_part_type_list', args=(each_part,)),
            })
        print all_part
        return render(request, 'inv/server_part_list.html', {
                      'page_name': page_name,
                      'all_part': all_part,
        })
    
    """
    2. Init Server Parts map: choice the part_name
    """
    try:
        server_part_map = server_parts_map[part_name]
    except:
        raise Http404
    
    page_name = u'%s' % server_part_map['name']
    
    """
    3. Get into the Edit page
    """
    if type_id:
        part_type = get_object_or_404(server_part_map['model'], pk=type_id)
        page_name = u'Edit %s' % server_part_map['name']
        if request.method == 'POST':
            form = server_part_map['form'](request.POST, instance=part_type)
            operate = request.POST.get('operate')
            if form.is_valid():
                if operate == 'update':
                    part_type = form.save()
                    messages.success(request, u'%s Type (%s) Update Success!' %
                                     (server_part_map['name'], part_type))
                    return HttpResponseRedirect(reverse('inventory:server_part_type_list', args=(part_name,)))
                elif operate == 'delete':
                    part_type.delete()
                    messages.success(request, u'%s Type (%s) Delete Success!' %
                                     (server_part_map['name'], part_type))
                    return HttpResponseRedirect(reverse('inventory:server_part_type_list', args=(part_name,)))
                else:
                    messages.warning(request, u'Dont support %s operation type!' % operate)
        else:
            form = server_part_map['form'](instance=part_type)
        return render(request, 'inv/server_part.html', {
                  "form": form,
                  "page_name": page_name,
                  "part_name": part_name,
                  "type_id": type_id,
                  })
    

    else:
        """
        4. Get into the NewAdd window
        """
        part_type = server_part_map['model']()
        if request.method == 'POST':
            form = server_part_map['form'](request.POST, instance=part_type)
            operate = request.POST.get('operate')
            if form.is_valid():
                if operate == 'add':
                    part_type = form.save()
                    messages.success(request, u'%s Type (%s) Add Success!' %
                                     (server_part_map['name'], part_type))
                    return HttpResponseRedirect(reverse('inventory:server_part_type_list', args=(part_name,)))
        else:
            form = server_part_map['form'](instance=part_type)
            
        all_type = server_part_map['model'].objects.all()
        return render(request, 'inv/server_part_type_list.html', {
                      "form": form,
                      "page_name": page_name,
                      "all_type": all_type,
                      "part_name": part_name,
                      })






