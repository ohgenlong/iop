# -*- coding: utf-8 -*-
from django.db import models

class Supplier(models.Model):
    """
    Supplier information
    """
    name = models.CharField(max_length=30, verbose_name=u'Supplier_Name', unique=True)
    seller = models.CharField(max_length=30, verbose_name=u'Seller')
    address = models.CharField(max_length=100, verbose_name=u'Supplier_Addr')
    phone = models.CharField(max_length=20, verbose_name=u'Supplier_Phone')
    email = models.EmailField(verbose_name=u'Email')
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Supplier'
        verbose_name_plural = u'Supplier_Management'


class ServerCPU(models.Model):
    """
    CPU Type for Servers
    """
    # CPU Manufacturer
    CPU_Manufacturer = (
        ('intel', u'Intel'),
        ('amd', u'AMD'),
    )
    name = models.CharField(max_length=30, verbose_name=u'CPU_Name', unique=True)
    manufacturer = models.CharField(max_length=10, choices=CPU_Manufacturer, verbose_name=u'CPU_Manufacturer', default='intel')
    cores = models.PositiveSmallIntegerField(verbose_name=u'CPU_Core_Num')
    speed = models.PositiveSmallIntegerField(verbose_name=u'CPU_Clocked_Speed(MHz)')
    l3cache = models.PositiveSmallIntegerField(verbose_name=u'CPU_3LC(MB)')
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True)

    def __unicode__(self):
        return u'%s - %s' %(self.manufacturer, self.name)

    class Meta:
        verbose_name = u'Server_CPU_Type'
        verbose_name_plural = u'Server_CPU_Type_Management'

class ServerMemory(models.Model):
    """
    Memory Type for Servers
    """
    # Memory type
    MemoryType = (
        ('ddr2', u'DDR2'),
        ('ddr3', u'DDR3'),
    )

    memory_type = models.CharField(max_length=5, choices=MemoryType, verbose_name=u'Memory_Type', default='ddr3')
    speed = models.PositiveSmallIntegerField(verbose_name=u'Memory_Frequency(MHz)')
    size = models.PositiveSmallIntegerField(verbose_name=u'Memory_Size(MB)')
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True)

    def __unicode__(self):
        return u'%s-%sM(%sMHz)' %(self.get_memory_type_display(), self.size, self.speed)

    class Meta:
        unique_together = (
            ("memory_type", "speed", "size"),
        )
        verbose_name = u'Server_Memory_Type'
        verbose_name_plural = u'Server_Memory_Type_Management'

class ServerHD(models.Model):
    """
    HardDisk Type for servers
    """
    # HardDisk type
    HDType = (
        ('hdd', u'HDD'),
        ('sdd', u'SSD'),
        ('hhd', u'HHD'),
    )
    HDSize = (
        ('2.5', u'2.5 Inch'),
        ('3.5', u'3.5 Inch'),
    )
    name = models.CharField(max_length=30, verbose_name=u'Disk_model', unique=True)
    manufacturer = models.CharField(max_length=20, verbose_name=u'Disk_Manufacturer')
    hd_type = models.CharField(max_length=3, choices=HDType, verbose_name=u'Disk_Type', default='hdd')
    speed = models.PositiveSmallIntegerField(verbose_name=u'Disk_Speed')
    size = models.CharField(max_length=3, choices=HDSize, verbose_name=u'Disk_Size')
    capacity = models.PositiveSmallIntegerField(verbose_name=u'Disk_Capacity(GB)')
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True)

    def __unicode__(self):
        return u'%s - %s' %(self.manufacturer, self.name)

    class Meta:
        verbose_name = u'Server_Disk_Type'
        verbose_name_plural = u'Server_Disk_Type_Management'

class ServerRaidLevel(models.Model):
    """
    Raid Level for servers
    """
    name = models.PositiveSmallIntegerField(max_length=2, verbose_name=u'Raid_Level', unique=True)
    min_hds = models.PositiveSmallIntegerField(max_length=1, verbose_name=u'Min_Hds_Num')
    max_hds = models.PositiveSmallIntegerField(max_length=2, verbose_name=u'Max_Hds_Num')
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True)

    def __unicode__(self):
        return u'Raid %d' %(self.name)

    class Meta:
        verbose_name = u'Server_Raid_Level'
        verbose_name_plural = u'Server_Raid_Level_Management'

class ServerRaidCard(models.Model):
    """
    Raid card type for servers
    """
    name = models.CharField(max_length=30, verbose_name=u'Raid_Card_Model', unique=True)
    manufacturer = models.CharField(max_length=20, verbose_name=u'Raid_Card_Manufacturer')
    cache = models.PositiveSmallIntegerField(verbose_name=u'Raid_Card_Cache_Size(MB)')
    battery = models.BooleanField(verbose_name=u'Raid_Card_Battery', default=True)
    support_raids = models.ManyToManyField(ServerRaidLevel, verbose_name=u'Raid_Card_Support_RaidLevel')
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True)

    def __unicode__(self):
        return u'%s - %s' %(self.manufacturer, self.name)

    class Meta:
        verbose_name = u'Server_Raid_Card_Type'
        verbose_name_plural = u'Server_Raid_Card_Type_Management'

class ServerNIC(models.Model):
    """
    Network interface type for servers
    """
    # Network Interface Speed
    NICSpeed = (
        ('100', '100Base'),
        ('1000', '1000Base'),
        ('10000', '10000Base'),
    )
    name = models.CharField(max_length=30, verbose_name=u'Nic_Model', unique=True)
    manufacturer = models.CharField(max_length=20, verbose_name=u'Nic_Manufacturer')
    speed = models.CharField(max_length=5, choices=NICSpeed, verbose_name=u'Nic_Max_Speend(Mbps)', default='1000')
    eom = models.BooleanField(verbose_name=u'Nic_Board_Type', default=True)
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True)

    def __unicode__(self):
        return u'%s - %s' %(self.manufacturer, self.name)

    class Meta:
        verbose_name = u'Server_Nic_Type'
        verbose_name_plural = u'Server_Nic_Type_Management'




class AssetBasicTemplate(models.Model):
    """
    Asset Basic Template
    """
    name = models.CharField(max_length=30, verbose_name=u'Asset_Template_Name', unique=True)
    manufacturer = models.CharField(max_length=20, verbose_name=u'Asset_Manufacturer')
    height = models.PositiveSmallIntegerField(verbose_name=u'Height(U)')
    exterior = models.ImageField(upload_to='asset', verbose_name=u'Exterior_Photo', blank=True)
    suppliers = models.ManyToManyField(Supplier, verbose_name=u'Supplier')
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u'%s - %s' %(self.manufacturer, self.name)


class ServerAssetTemplate(AssetBasicTemplate):
    """
    Server Asset Template
    """
    cpu = models.ForeignKey(ServerCPU, verbose_name=u'Default_CPU_Type')
    cpu_number = models.PositiveSmallIntegerField(default=1, verbose_name=u'CPU_Num')
    max_cpu_number = models.PositiveSmallIntegerField(verbose_name=u'Max_CPU_Number')
    memory = models.ForeignKey(ServerMemory, verbose_name=u'Memory_Model')
    memory_number = models.PositiveSmallIntegerField(default=1, verbose_name=u'Memory_Num')
    max_memory_number = models.PositiveSmallIntegerField(verbose_name=u'Max_Memory_Num')
    hds = models.ManyToManyField(ServerHD, through='ServerTemplateHDS')
    nics = models.ManyToManyField(ServerNIC, through='ServerTemplateNICS')

    class Meta:
        verbose_name = u'Server_Asset_Tempalte'
        verbose_name_plural = u'Server_Asset_Tempalte_Management'

class ServerTemplateHDS(models.Model):
    """
    Server Template Disk Info
    """
    hd_type = models.ForeignKey(ServerHD, verbose_name=u'Disk_Type')
    server = models.ForeignKey(ServerAssetTemplate)

    def __unicode__(self):
        return u'%s' %(self.hd_type)

    class Meta:
        verbose_name = u'Server Template Disk Info'
        verbose_name_plural = u'Server_Template_Disk_Info_Management'

class ServerTemplateNICS(models.Model):
    """
    Server Template Nic Info
    """
    nic_type = models.ForeignKey(ServerNIC, verbose_name=u'Nic_Type')
    server = models.ForeignKey(ServerAssetTemplate)

    def __unicode__(self):
        return u'%s' %(self.nic_type)

    class Meta:
        verbose_name = u'Server_Template_Nic_Info'
        verbose_name_plural = u'Server_Template_Nic_Info_Management'

class ServerAsset(models.Model):
    """
    Server Asset Info
    """
    template = models.ForeignKey(ServerAssetTemplate, verbose_name=u'Server_Template')
    supplier = models.ForeignKey(Supplier, verbose_name=u'Supplier')
    sn = models.CharField(max_length=25, verbose_name=u'SN', unique=True)
    esc = models.CharField(max_length=20, verbose_name=u'Express service code', blank=True)
    purchase_date = models.DateField(verbose_name=u'Purchase_Date')
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True)

    def __unicode__(self):
        return u'%s - %s' %('Server', self.sn)

    class Meta:
        verbose_name = u'Server_Asset'
        verbose_name_plural = u'Server_Asset_Management'

class SwitchAssetTemplate(AssetBasicTemplate):
    """
    Switch Asset Template
    """
    class Meta:
        verbose_name = u'Switch_Asset_Template'
        verbose_name_plural = u'Switch_Asset_Template_Management'

class SwitchAsset(models.Model):
    """
    Switch Asset Info
    """
    template = models.ForeignKey(SwitchAssetTemplate, verbose_name=u'Switch_Template')
    supplier = models.ForeignKey(Supplier, verbose_name=u'Supplier')
    sn = models.CharField(max_length=25, verbose_name=u'SN', unique=True)
    purchase_date = models.DateField(verbose_name=u'Purchase_Date')
    notes = models.TextField(max_length=200, verbose_name=u'Remark', blank=True) 

    def __unicode__(self):
        return u'%s - %s' %('Switch', self.sn)

    class Meta:
        verbose_name = u'Switch_Asset_Info'
        verbose_name_plural = u'Switch_Asset_Info_Management'
        
        
        
        
        
        
        



