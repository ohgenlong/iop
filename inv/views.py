# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Pagination
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

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


"""
Template Views
"""
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

def _get_templates(template_type, ret_format='list'):
    """
    Get templates list
    """
    all_template = {'list': [],
                     'dict': {},
                     }
    template_model = templates_map[template_type]['model']
    for template in template_model.objects.all():
        template_info = {
            "id": template.id,
            "name": template.name,
            "manufacturer": template.manufacturer,
            "height": template.height,
            "suppliers": ",".join([each.name for each in template.suppliers.all()]),
            "notes": template.notes,
        }
        if template_type == 'server':
            cpu_info = "%s %s * %s" % (
                template.cpu.get_manufacturer_display(), template.cpu.name, template.cpu_number)
            total_memory_size = template.memory.size * \
                template.memory_number / 1024
            memory_info = "%sG(%sM * %s)" % (total_memory_size,
                                             template.memory.size, template.memory_number)
            total_hds = {}
            total_hds_capacity = 0
            hds_info = []
            for each_hd in template.hds.all():
                total_hds[each_hd.capacity] = total_hds.get(
                    each_hd.capacity, 0) + 1
                total_hds_capacity += each_hd.capacity
            for each_hd_capacity in total_hds:
                hds_info.append(
                    "%sG * %s" % (each_hd_capacity, total_hds[each_hd_capacity]))
            hds_info = "%sG(%s)" % (total_hds_capacity, ", ".join(hds_info))
            total_nics = {}
            nics_info = []
            for each_nic in template.nics.all():
                total_nics[each_nic.speed] = total_nics.get(
                    each_nic.speed, 0) + 1
            for each_nic_speed in total_nics:
                nics_info.append(
                    "%sM * %s" %(each_nic_speed, total_nics[each_nic_speed])
                )
            nics_info = ", ".join(nics_info)
            template_info["cpu"] = cpu_info
            template_info["memory"] = memory_info
            template_info["hds"] = hds_info
            template_info["nics"] = nics_info

        all_template['list'].append(template_info)
        all_template['dict'][template.id] = template_info
        print all_template

    return all_template.get(ret_format)

@login_required
def template_manage(request, template_type=None, template_id=None):
    """
    Manage template
    """
    if not template_type:
        page_name = u'Template Management'
        template_order = ['server', 'switch']
        all_type = []
        for each_type in template_order:
            type_map = templates_map[each_type]
            all_type.append({
                'name': type_map['name'],
                'number': type_map['model'].objects.count(),
                'icon': type_map['icon'],
                'color': type_map['color'],
                'url': reverse('inventory:template_type_list', args=(each_type,)),
            })
        return render(request, 'inv/template_list.html', {
                      'page_name': page_name,
                      'all_type': all_type,
        })
    try:
        template_map = templates_map[template_type]
    except:
        raise Http404
    page_name = u'%s' % template_map['name']
    if template_id:
        template = get_object_or_404(template_map['model'], pk=template_id)
        page_name = u'Edit %s' % template_map['name']
        if request.method == 'POST':
            form = template_map['form'](request.POST, request.FILES, instance=template)
            operate = request.POST.get('operate')
            if form.is_valid():
                if operate == 'update':
                    template = form.save()
                    messages.success(request, u'%s (%s) Update Success!' %
                                     (template_map['name'], template))
                    return HttpResponseRedirect(reverse('inventory:template_type_list', args=(template_type,)))
                elif operate == 'delete':
                    template.delete()
                    messages.success(request, u'%s (%s) Delete Success!' %
                                     (template_map['name'], template))
                    return HttpResponseRedirect(reverse('inventory:template_type_list', args=(template_type,)))
                else:
                    messages.warning(request, u'Dont support %s operation type!' % operate)
        else:
            form = template_map['form'](instance=template)
        return render(request, 'inv/template.html', {
                  "form": form,
                  "page_name": page_name,
                  "template_type": template_type,
                  "template_id": template_id,
                  "template_io_map": template_map.get('io_map'),
                  })
    else:
        template = template_map['model']()
        if request.method == 'POST':
            form = template_map['form'](request.POST, request.FILES, instance=template)
            operate = request.POST.get('operate')
            if form.is_valid():
                if operate == 'add':
                    template = form.save()
                    messages.success(request, u'%s (%s) Add Success!' %
                                     (template_map['name'], template))
                    return HttpResponseRedirect(reverse('inventory:template_type_list', args=(template_type,)))
                elif operate == 'add_and_manage_io':
                    template = form.save()
                    messages.success(request, u'%s (%s) Add Success!' %
                                     (template_map['name'], template))
                    return HttpResponseRedirect(reverse('inventory:template_manage',
                                                        args=(template_type, template.id)))
        else:
            form = template_map['form'](instance=template)
        all_template = _get_templates(template_type)
        return render(request, 'inv/template_type_list.html', {
                      "form": form,
                      "page_name": page_name,
                      "all_template": all_template,
                      "template_type": template_type,
                      })



@login_required
def template_io_manage(request, template_type, template_id, io_type):
    """
    Manage Template I/O device
    """
    try:
        template_map = templates_map[template_type]
    except:
        raise Http404
    template = get_object_or_404(template_map['model'], pk=template_id)
    template_io_map = template_map.get('io_map')
    if not template_io_map:
        raise Http404
    template_io = template_io_map.get(io_type)
    if not template_io:
        raise Http404
    page_name = template_io['name']
    io_model = template_io['model']()
    if request.method == 'POST':
        operate = request.POST.get('operate')
        if operate == 'add':
            form = template_io['form'](request.POST, instance=io_model)
            if form.is_valid():
                io_dev = form.save(commit=False)
                io_dev.server = template
                io_dev.save()
                messages.success(request, u"%s Template (%s) IO_device (%s) Add Success!" %
                                 (template_map['name'], template, template_io['name']))
                return HttpResponseRedirect(reverse('inventory:template_manage',
                                                    args=(template_type, template_id)))
        elif operate == 'delete':
            io_id = request.POST.get('io_id')
            if io_id:
                io_dev = get_object_or_404(template_io['model'], pk=io_id)
                io_dev.delete()
                messages.success(request, u"%s Template (%s) IO_device (%s) Delete Success!" %
                                 (template_map['name'], template, io_dev)
                                 )
            return HttpResponseRedirect(reverse('inventory:template_manage',
                                                args=(template_type, template_id)))
        else:
            messages.warning(request, u'Dont support %s operation type!' % operate)
    else:
        form = template_io['form'](instance=io_model)
    all_io = template_io['model'].objects.filter(server=template).order_by('id')
    
    return render(request, 'inv/template_io.html', {
                  "form": form,
                  "template_type": template_type,
                  "template_id": template_id,
                  "io_type": io_type,
                  "all_io": all_io,
                  "page_name": page_name,
                  })




