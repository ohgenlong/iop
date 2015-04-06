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








