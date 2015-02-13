# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8:ts=4:sw=4

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default
from django.contrib.auth.decorators import login_required
from django.conf import settings


class Asset(models.Model):  
    device_type_choices = (
        ('server', u'������'),
        ('switch', u'������'),
        ('router', u'·����'),
        ('firewall', u'����ǽ'),
        ('storage', u'�洢�豸'),
        ('acc_cpu', u'CPU'),
        ('acc_memory', u'�ڴ���'),
        ('acc_disk', u'Ӳ��'),
        ('acc_network_adapter', u'����'),
        ('acc_monitor', u'��ʾ��'),
        ('acc_others', u'�������'),
    )
    device_type = models.CharField(choices=device_type_choices,max_length=64, default='server')
    name = models.CharField(max_length=30)
    hostname= models.CharField(max_length=32, blank=True, unique=True)
    #sn = models.CharField(u'�ʲ�SN��',max_length=64, unique=True,null=True, blank=True)
    #manufactory = models.ForeignKey('Manufactory',verbose_name=u'������',null=True, blank=True)
    #model = models.ForeignKey('ProductVersion', verbose_name=u'�ͺ�')
    asset_op = models.CharField(max_length=32,blank=True,null=True)
    contract = models.ForeignKey('Contract', verbose_name=u'��ͬ',null=True, blank=True)
    trade_time = models.DateTimeField(u'����ʱ��',null=True, blank=True)
    warranty = models.SmallIntegerField(u'������',null=True, blank=True)
    price = models.IntegerField(u'�۸�',null=True, blank=True) 
    business_unit = models.ForeignKey('BusinessUnit', verbose_name=u'���ڵ�ҵ����',null=True, blank=True)
    business_unit_level2 = models.ForeignKey('BusinessUnitLevel2', verbose_name=u'2��ҵ����',null=True, blank=True)
    function = models.CharField(max_length=32,blank=True,null=True)
    admin = models.ForeignKey('UserProfile', verbose_name=u'�豸����Ա',related_name='+',null=True, blank=True)
    #client = models.ForeignKey('UserProfile', verbose_name=u'ҵ��ʹ�÷�',null=True, blank=True)
    idc = models.ForeignKey('IDC', verbose_name=u'IDC����',null=True, blank=True)
    cabinet_num = models.CharField(u'�����',max_length=30,null=True, blank=True)
    cabinet_order = models.SmallIntegerField(u'���������',null=True, blank=True)

    status = models.ForeignKey('Status', verbose_name = u'�豸״̬',default=1)
    #Configuration = models.OneToOneField('Configuration',verbose_name='���ù���',blank=True,null=True)
    
    memo = models.TextField(u'��ע', null=True, blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
     
    #maintain_record = models.ManyToManyField('Maintainence', verbose_name='ά�������¼')
    class Meta:
        verbose_name = '�ʲ��ܱ�'
        verbose_name_plural = "�ʲ��ܱ�"
    def __unicode__(self):
        return 'id:%s h:%s'  %(self.id,self.hostname)        
class Status(models.Model):
    status_choice = (
        (1, 'Init'),
        (2, 'Standby'),
        (3, 'Online'),
        (4, 'Offline'),
        (5, 'Unreachable'),
        (6, 'Deprecated'),
        (7, 'Maintenance'),
    )
    status = models.SmallIntegerField(u'�豸״̬', choices=status_choice,unique=True)    
    os_installed = models.BooleanField(default=False)
    puppet_installed = models.BooleanField(default=False)
    zabbix_configured = models.BooleanField(default=False)
    auditing_configured = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)    
    
    def __unicode__(self):
 
        return '%s' %self.get_status_display()
    
class Configuration(models.Model):
    '''store all the configurations of this asset'''
    asset = models.OneToOneField('Asset',default=None)
    definded_raid_type = models.CharField(verbose_name=u'Ԥ����raid����',max_length=32,blank=True,null=True)
    nic = models.ManyToManyField('NICConfig', verbose_name=u'�����б�',blank=True )
    management_ip = models.CharField(u'����IP',max_length=64,blank=True,null=True)
    os = models.ForeignKey('Software', verbose_name='OS', blank=True,null=True)
    
    os_installed = models.BooleanField(default=False)
    puppet_installed = models.BooleanField(default=False)
    zabbix_configured = models.BooleanField(default=False)
    auditing_configured = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    
    def __unicode__(self):
        return '%s ' % self.id
class NICConfig(models.Model):
    name = models.CharField(u'���',max_length=128,blank=True)
    ipaddr = models.IPAddressField(u'ip��ַ',blank=True)
    mac = models.CharField(u'����mac��ַ', max_length=64)
    netmask = models.CharField(max_length=64,blank=True)
    gateway = models.IPAddressField(u'����')
    bonding = models.BooleanField(default=False)
    memo = models.TextField(u'��ע', blank=True)
    class Meta:
        unique_together = ("name", "mac")
        verbose_name = '���ñ�_����'
        verbose_name_plural = "���ñ�_����"   
    def __unicode__(self):
        return '%s:%s' %(self.name,self.ipaddr)    
    
        
class Server(models.Model):
    asset = models.OneToOneField('Asset')  
    created_by = models.CharField(max_length=32,default='auto') #auto: auto created,   manual:created manually 
    sn = models.CharField(u'SN��',max_length=64)
    management_ip = models.CharField(u'����IP',max_length=64,blank=True,null=True)
    manufactory = models.CharField(verbose_name=u'������',max_length=128,null=True, blank=True)
    model = models.CharField(u'�ͺ�',max_length=128,null=True, blank=True )
    # ���ж��CPU���ͺ�Ӧ�ö���һ�µģ���û��ForeignKey
    cpu_count = models.SmallIntegerField(u'cpu����',blank=True)
    cpu_core_count = models.SmallIntegerField(u'cpu����',blank=True)
    cpu_model = models.ForeignKey('CPU')    
    
    nic = models.ManyToManyField('NIC', verbose_name=u'�����б�')
    #disk
    raid_type = models.TextField(u'raid����', blank=True)
    physical_disk_driver = models.ManyToManyField('Disk', verbose_name=u'Ӳ��',blank=True) 
    raid_adaptor = models.ManyToManyField('RaidAdaptor', verbose_name=u'Raid��',blank=True) 
    #memory
    ram_size = models.IntegerField(u'�ڴ��ܴ�СGB',blank=True)
    ram = models.ManyToManyField('Memory', verbose_name=u'�ڴ�����',blank=True)
    
    os_type  = models.CharField(u'����ϵͳ����',max_length=64, blank=True,null=True)
    os_distribution =models.CharField(u'���Ͱ汾',max_length=64, blank=True,null=True)
    os_version  = models.CharField(u'����ϵͳ�汾',max_length=64, blank=True,null=True)
    
    #software
    #software = models.ManyToManyField('Software', verbose_name=u'���',null=True, blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True)  
    class Meta:
        verbose_name = '������'
        verbose_name_plural = "������"   
        index_together = ["sn", "asset"]
        
    def __unicode__(self):
        return '%s sn:%s' %(self.asset.hostname,self.sn)
class NetworkDevice(models.Model):
    asset = models.OneToOneField('Asset') 
    sn = models.CharField(u'SN��',max_length=64,unique=True)
    manufactory = models.CharField(verbose_name=u'������',max_length=128,null=True, blank=True)
    model = models.CharField(u'�ͺ�',max_length=128,null=True, blank=True )
    firmware = models.ForeignKey('Software')
    port_num = models.SmallIntegerField(u'�˿ڸ���')
    device_detail = models.TextField(u'������ϸ����')
    class Meta:
        verbose_name = '�����豸'
        verbose_name_plural = "�����豸"   
class Software(models.Model):
    #sn = models.CharField(u'SN��',max_length=64, unique=True)
    os_types_choice = (
        (1, 'GNU/Linux'),
        (2, 'MS/Windows'),
        (3, 'Network Firmware'),
        (4, 'Softwares'),
    )
    types = models.SmallIntegerField(u'ϵͳ����', choices=os_types_choice, max_length=64,help_text=u'eg. GNU/Linux')  
    version = models.CharField(u'���/ϵͳ�汾', max_length=64, help_text=u'eg. CentOS release 6.5 (Final)', unique=True)
    #version = models.CharField(u'�汾��', max_length=64,help_text=u'2.6.32-431.3.1.el6.x86_64' )
      
    def __unicode__(self):
        return self.version    
    class Meta:
        verbose_name = '���/ϵͳ'
        verbose_name_plural = "���/ϵͳ"           
class Disk(models.Model):
    sn = models.CharField(u'SN��', max_length=128, blank=True)
    parent_sn = models.CharField(max_length=128,blank=True)
    slot = models.CharField(u'���λ',max_length=32,blank=True)
    manufactory = models.CharField(u'������', max_length=32,default=None,blank=True)
    model = models.CharField(u'�����ͺ�', max_length=128,blank=True)
    capacity = models.FloatField(u'��������GB',blank=True)
    disk_iface_choice = (
        ('SATA', 'SATA'),
        ('SAS', 'SAS'),
        ('SCSI', 'SCSI'),
        ('SSD', 'SSD'),
    )

    iface_type = models.CharField(u'�ӿ�����', max_length=64,choices=disk_iface_choice,blank=True)
    memo = models.TextField(u'��ע', blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)    
    class Meta:
        unique_together = ("parent_sn", "slot")
        verbose_name = 'Ӳ�̲���'
        verbose_name_plural = "Ӳ�̲���"      
    def __unicode__(self):
        return 'slot:%s size:%s' % (self.slot,self.capacity)
class CPU(models.Model):
    sn = models.CharField(u'SN��',max_length=64,blank=True)
    parent_sn = models.CharField(max_length=128,blank=True, unique=True)
    manufactory = models.CharField(u'������', max_length=32,default=None,blank=True)
    model = models.CharField(u'CPU�ͺ�', max_length=64,blank=True)
    memo = models.TextField(u'��ע', blank=True)
    class Meta:

        verbose_name = 'CPU����'
        verbose_name_plural = "CPU����"   
    def __unicode__(self):
        return self.model
class Monitor(models.Model):
    asset = models.OneToOneField('Asset') 
    sn = models.CharField(u'SN��',max_length=64, unique=True)
    manufactory = models.CharField(u'������', max_length=32,default=None)
    model = models.CharField(u'��ʾ�豸�ͺ�', max_length=64)
    memo = models.TextField(u'��ע', blank=True)
    class Meta:
        verbose_name = '��ʾ�豸'
        verbose_name_plural = "��ʾ�豸"   
    def __unicode__(self):
        return self.model
        
class NIC(models.Model):
    name = models.CharField(u'���',max_length=128,blank=True)
    sn = models.CharField(u'SN��',max_length=128,blank=True)
    parent_sn = models.CharField(max_length=128,blank=True)
    model = models.CharField(u'�����ͺ�', max_length=128,blank=True)
    manufactory = models.CharField(u'������', max_length=32, blank=True)
    # TODO: ���һ�������ж��IP����ô��Ҫ��IP����Ϊһ��model����ForeignKey
    ipaddr = models.IPAddressField(u'ip��ַ',blank=True)
    mac = models.CharField(u'����mac��ַ', max_length=64)
    netmask = models.CharField(max_length=64,blank=True)
    memo = models.TextField(u'��ע', blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    class Meta:
        unique_together = ("name", "mac")
        verbose_name = '��������'
        verbose_name_plural = "��������"   
    def __unicode__(self):
        return '%s:%s' %(self.name,self.ipaddr)    
        
class RaidAdaptor(models.Model):
    sn = models.CharField(u'SN��', max_length=128,blank=True)
    name = models.CharField(u'���',max_length=32,blank=True)
    parent_sn = models.CharField(max_length=128,blank=True)
    model = models.CharField(u'�ͺ�', max_length=64,blank=True)
    memo = models.TextField(u'��ע', blank=True)
    def __unicode__(self):
        return self.name 
    class Meta:
        unique_together = ("parent_sn", "name")
    
# 10w̨��������ÿ������4���ڴ���㣬memory��������40w
class Memory(models.Model):
    sn = models.CharField(u'SN��', max_length=128,blank=True)
    parent_sn = models.CharField(max_length=128,blank=True)
    model = models.CharField(u'�ͺ�', max_length=64,blank=True)
    manufactory = models.CharField(u'������', max_length=32,null=True,blank=True)
    slot = models.CharField(u'���λ',max_length=32,blank=True)
    capacity =  models.FloatField(u'����',blank=True)
    # ����ڴ�û��sn�Ļ���������model��PK
   
    memo = models.TextField(u'��ע', blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    class Meta:
        unique_together = ("parent_sn", "slot")
        verbose_name = '�ڴ沿��'
        verbose_name_plural = "�ڴ沿��"   
    def __unicode__(self):
        if self.capacity != 0:
            return '%s: %sGB '%( self.slot, self.capacity)   
        else:  
            return self.slot
class Contract(models.Model):
    sn = models.CharField(u'��ͬ��', max_length=64,unique=True)
    name = models.CharField(u'��ͬ����', max_length=64 )
    memo = models.TextField(u'��ע', blank=True)
    cost = models.IntegerField(u'��ͬ���')
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)
    license_num = models.IntegerField(u'license����',blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    class Meta:
        verbose_name = '��ͬ'
        verbose_name_plural = "��ͬ"     
    def __unicode__(self):
        return self.name
        
class IDC(models.Model):
    name = models.CharField(u'����english',max_length=30)
    display_name = models.CharField(u'������ʾ��',max_length=32,default=None)
    region = models.CharField(u'����',max_length=64,default=None)
    region_display_name = models.CharField(u'��������',max_length=64,default=None)
    isp = models.CharField(u'��Ӫ��',max_length=32,default=None)
    isp_display_name = models.CharField(u'��Ӫ������',max_length=32,default=None)
    floor = models.IntegerField(u'¥��',default=1)
    memo = models.CharField(u'��ע',max_length=64)
    def __unicode__(self):
        return 'region:%s isp:%s idc:%s floor:%s' %(self.region_display_name,
                                                    self.isp_display_name,
                                                    self.display_name,
                                                    self.floor)
                                                    
    class Meta:
        verbose_name = '����'
        verbose_name_plural = "����"  
        
class Manufactory(models.Model):
    name = models.CharField(u'��������',max_length=64, unique=True)
    support_num = models.CharField(u'֧�ֵ绰',max_length=30,blank=True)
    memo = models.CharField(u'��ע',max_length=30,blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '����'
        verbose_name_plural = "����"          
class ProductVersion(models.Model):
    name = models.CharField(u'��Ʒ�ͺ�',max_length=64, unique=True)
    version = models.CharField(u'��Ʒ�汾��',max_length=64,blank=True)
    def __unicode__(self):
        return self.name    
class BusinessUnit(models.Model):
    name = models.CharField(u'ҵ����',max_length=64, unique=True)
    contact = models.ForeignKey('UserProfile',default=None)
    memo = models.CharField(u'��ע',max_length=64, blank=True)
    def __unicode__(self):
        return self.name 
    class Meta:
        verbose_name = 'ҵ����'
        verbose_name_plural = "ҵ����"  
class BusinessUnitLevel2(models.Model):
    name = models.CharField(u'����ҵ����',max_length=64, unique=True)
    
    memo = models.CharField(u'��ע',max_length=64, blank=True)
    def __unicode__(self):
        return self.name 
    class Meta:
        verbose_name = '����ҵ����'
        verbose_name_plural = "����ҵ����"  
        
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(u'����', max_length=32)
    token = models.CharField(u'token', max_length=128,blank=True,null=True)
    department = models.CharField(u'����', max_length=32)
    business_unit = models.ManyToManyField(BusinessUnit)
    email = models.EmailField(u'����')
    phone = models.CharField(u'����', max_length=32)
    mobile = models.CharField(u'�ֻ�', max_length=32)
    
    backup_name = models.ForeignKey('self', verbose_name=u'������ϵ��',blank=True,null=True,related_name='user_backup_name')
    leader = models.ForeignKey('self', verbose_name='�ϼ��쵼',blank=True,null=True)
    memo = models.TextField(u'��ע', blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True)
    update_at = models.DateTimeField(blank=True, auto_now=True)
    class Meta:
        verbose_name = '�û���Ϣ'
        verbose_name_plural = "�û���Ϣ" 
    def __unicode__(self):
        return self.name
class Maintainence(models.Model):
    name = models.CharField(u'�¼�����', max_length=100)
    change_choices = (
        (1,u'Ӳ������'),
        (2,u'�������'),
        (3,u'�豸����'),
        (4,u'�豸����'),
        (5,u'����ά��'),
        (6,u'ҵ������\����\���'),
        (7,u'����'),
    )
    maintain_type = models.SmallIntegerField(u'�������', choices= change_choices,max_length=30)
    description = models.TextField(u'�¼�����')
    device_sn = models.CharField('AssetID',max_length=64,blank=True)
    event_start = models.DateTimeField(u'�¼���ʼʱ��',blank=True)
    event_end = models.DateTimeField(u'�¼�����ʱ��',blank=True)
    applicant = models.ForeignKey('UserProfile',verbose_name=u'������',related_name='applicant_user')
    performer = models.ForeignKey('UserProfile',verbose_name=u'ִ����')
    memo = models.TextField(u'��ע', blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '�����¼'
        verbose_name_plural = "�����¼" 

class EventLog(models.Model):
    uuid = models.CharField(u'����ID', max_length=128, unique=True)
    post_data = models.TextField(u'����Data',blank=True)
    detail = models.TextField(u'��ϸ����' ,blank=True)
    create_at = models.DateTimeField(blank=True, auto_now_add=True,null=True)
    def __unicode__(self):
        return self.uuid


class ApiAuth(models.Model):
    url = models.CharField(u'�ӿ�url',max_length=64)
    description = models.CharField(u'���', max_length=64)
    method_choice = (
        ('GET', '����Get(�ɶ�)'),          
        ('POST', '����POST(���޸�)') ,         
        ('PUT', '����PUT(�� ����)') ,         
        ('HEAD', 'HEAD(�ݲ���)') ,         
        ('PATCH', 'PATCH(�ݲ���)') ,         
                     )
    method_type = models.CharField(u'���÷���',choices=method_choice,max_length=32 )
    users = models.ManyToManyField(UserProfile, null=True)
    
    class Meta:
        unique_together = ("url", "method_type")
        verbose_name = '�ӿ�Ȩ��'
        verbose_name_plural = "�ӿ�Ȩ��"    
    def __unicode__(self):
        return '%s:: %s' %(self.method_type,self.url)