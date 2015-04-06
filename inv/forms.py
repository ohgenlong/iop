# -*- coding: utf-8 -*-
from django.forms import *

from inv.models import *
#from wolf.utils.dell import sn2esc

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'seller', 'address', 'phone', 'email', 'notes']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'seller': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

class ServerCPUForm(ModelForm):
    class Meta:
        model = ServerCPU
        fields = ['name', 'manufacturer', 'cores', 'speed', 'l3cache', 'notes']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'manufacturer': Select(attrs={'class': 'form-control'}),
            'cores': NumberInput(attrs={'class': 'form-control'}),
            'speed': NumberInput(attrs={'class': 'form-control'}),
            'l3cache': NumberInput(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

class ServerMemoryForm(ModelForm):
    class Meta:
        model = ServerMemory
        fields = ['memory_type', 'speed', 'size', 'notes']
        widgets = {
            'memory_type': Select(attrs={'class': 'form-control'}),
            'speed': NumberInput(attrs={'class': 'form-control'}),
            'size': NumberInput(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

class ServerHDForm(ModelForm):
    class Meta:
        model = ServerHD
        fields = ['name', 'manufacturer', 'hd_type', 'speed', 'size', 'capacity', 'notes']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'manufacturer': TextInput(attrs={'class': 'form-control'}),
            'hd_type': Select(attrs={'class': 'form-control'}),
            'speed': NumberInput(attrs={'class': 'form-control'}),
            'size': Select(attrs={'class': 'form-control'}),
            'capacity': NumberInput(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

class ServerRaidLevelForm(ModelForm):
    class Meta:
        model = ServerRaidLevel
        fields = ['name', 'min_hds', 'max_hds', 'notes']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'min_hds': NumberInput(attrs={'class': 'form-control'}),
            'max_hds': NumberInput(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }


class ServerRaidCardForm(ModelForm):
    class Meta:
        model = ServerRaidCard
        fields = ['name', 'manufacturer', 'cache', 'battery', 'support_raids', 'notes']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'manufacturer': TextInput(attrs={'class': 'form-control'}),
            'cache': NumberInput(attrs={'class': 'form-control'}),
            'battery': CheckboxInput(attrs={'class': 'form-control'}),
            'support_raids': CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

class ServerNICForm(ModelForm):
    class Meta:
        model = ServerNIC
        fields = ['name', 'manufacturer', 'speed', 'eom', 'notes']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'manufacturer': TextInput(attrs={'class': 'form-control'}),
            'speed': NumberInput(attrs={'class': 'form-control'}),
            'eom': CheckboxInput(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

class ServerAssetTemplateForm(ModelForm):
    class Meta:
        model = ServerAssetTemplate
        fields = ['name', 'manufacturer', 'height', 'exterior', 'suppliers',
                  'cpu', 'cpu_number', 'max_cpu_number',
                  'memory', 'memory_number', 'max_memory_number',
                  'notes',
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'manufacturer': TextInput(attrs={'class': 'form-control'}),
            'height': NumberInput(attrs={'class': 'form-control'}),
            'exterior': ClearableFileInput(attrs={'class': 'form-control'}),
            'suppliers': CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'cpu': Select(attrs={'class': 'form-control'}),
            'cpu_number': NumberInput(attrs={'class': 'form-control'}),
            'max_cpu_number': NumberInput(attrs={'class': 'form-control'}),
            'memory': Select(attrs={'class': 'form-control'}),
            'memory_number': NumberInput(attrs={'class': 'form-control'}),
            'max_memory_number': NumberInput(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

    def clean_cpu_number(self):
        cpu_number = int(self.data.get('cpu_number'))
        max_cpu_number = int(self.data.get('max_cpu_number'))
        if cpu_number > max_cpu_number:
            self._errors['cpu_number'] = self.error_class([u'CPU鏁扮洰瓒呰繃鏈�澶ф敮鎸佺殑CPU鏁�'])
        return cpu_number

    def clean_memory_number(self):
        memory_number = int(self.data.get('memory_number'))
        max_memory_number = int(self.data.get('max_memory_number'))
        if memory_number > max_memory_number:
            self._errors['memory_number'] = self.error_class([u'鍐呭瓨鏁扮洰瓒呰繃鏈�澶ф敮鎸佺殑鍐呭瓨鏁�'])
        return memory_number


class SwitchAssetTemplateForm(ModelForm):
    class Meta:
        model = SwitchAssetTemplate
        fields = ['name', 'manufacturer', 'height', 'exterior', 'suppliers',
                  'notes',
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'manufacturer': TextInput(attrs={'class': 'form-control'}),
            'height': NumberInput(attrs={'class': 'form-control'}),
            'exterior': FileInput(attrs={'class': 'form-control'}),
            'suppliers': CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

class ServerTemplateHDSForm(ModelForm):
    class Meta:
        model = ServerTemplateHDS
        exclude = ['server']
        widgets = {
            'hd_type': Select(attrs={'class': 'form-control'}),
        }

class ServerTemplateNICSForm(ModelForm):
    class Meta:
        model = ServerTemplateNICS
        exclude = ['server']
        widgets = {
            'nic_type': Select(attrs={'class': 'form-control'}),
        }

class ServerAssetForm(ModelForm):
    class Meta:
        model = ServerAsset
        fields = ['template', 'supplier', 'sn', 'esc', 'purchase_date', 'notes']
        widgets = {
            'template': Select(attrs={'class': 'form-control'}),
            'supplier': Select(attrs={'class': 'form-control'}),
            'sn': TextInput(attrs={'class': 'form-control'}),
            'esc': TextInput(attrs={'class': 'form-control', 'placeholder': u'鑷姩鐢熸垚(浠呴檺DELL璁惧)', 'disabled': ''}),
            'purchase_date': DateInput(attrs={'class': 'form-control', 'type': 'Date'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }

    def clean_esc(self):
        sn = self.cleaned_data.get('sn')
        #ecs = sn2esc(sn)
        return sn
        #return ecs


class SwitchAssetForm(ModelForm):
    class Meta:
        model = SwitchAsset
        fields = ['template', 'supplier', 'sn', 'purchase_date', 'notes']
        widgets = {
            'template': Select(attrs={'class': 'form-control'}),
            'supplier': Select(attrs={'class': 'form-control'}),
            'sn': TextInput(attrs={'class': 'form-control'}),
            'purchase_date': DateInput(attrs={'class': 'form-control', 'type': 'Date'}),
            'notes': Textarea(attrs={'class': 'form-control'}),
        }
        
        
        