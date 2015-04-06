# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=25, verbose_name='SN')),
                ('esc', models.CharField(max_length=20, verbose_name='Express service code', blank=True)),
                ('purchase_date', models.DateField(verbose_name='Purchase_Date')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
            ],
            options={
                'verbose_name': 'Server_Asset',
                'verbose_name_plural': 'Server_Asset_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerAssetTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='Asset_Template_Name')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Asset_Manufacturer')),
                ('height', models.PositiveSmallIntegerField(verbose_name='Height(U)')),
                ('exterior', models.ImageField(upload_to=b'asset', verbose_name='Exterior_Photo')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
                ('cpu_number', models.PositiveSmallIntegerField(default=1, verbose_name='CPU_Num')),
                ('max_cpu_number', models.PositiveSmallIntegerField(verbose_name='Max_CPU_Number')),
                ('memory_number', models.PositiveSmallIntegerField(default=1, verbose_name='Memory_Num')),
                ('max_memory_number', models.PositiveSmallIntegerField(verbose_name='Max_Memory_Num')),
            ],
            options={
                'verbose_name': 'Server_Asset_Tempalte',
                'verbose_name_plural': 'Server_Asset_Tempalte_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerCPU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='CPU_Name')),
                ('manufacturer', models.CharField(default=b'intel', max_length=10, verbose_name='CPU_Manufacturer', choices=[(b'intel', 'Intel'), (b'amd', 'AMD')])),
                ('cores', models.PositiveSmallIntegerField(verbose_name='CPU_Core_Num')),
                ('speed', models.PositiveSmallIntegerField(verbose_name='CPU_Clocked_Speed(MHz)')),
                ('l3cache', models.PositiveSmallIntegerField(verbose_name='CPU_3LC(MB)')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
            ],
            options={
                'verbose_name': 'Server_CPU_Type',
                'verbose_name_plural': 'Server_CPU_Type_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerHD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='Disk_model')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Disk_Manufacturer')),
                ('hd_type', models.CharField(default=b'hdd', max_length=3, verbose_name='Disk_Type', choices=[(b'hdd', 'HDD'), (b'sdd', 'SSD'), (b'hhd', 'HHD')])),
                ('speed', models.PositiveSmallIntegerField(verbose_name='Disk_Speed')),
                ('size', models.CharField(max_length=3, verbose_name='Disk_Size', choices=[(b'2.5', '2.5 Inch'), (b'3.5', '3.5 Inch')])),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='Disk_Capacity(GB)')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
            ],
            options={
                'verbose_name': 'Server_Disk_Type',
                'verbose_name_plural': 'Server_Disk_Type_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerMemory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('memory_type', models.CharField(default=b'ddr3', max_length=5, verbose_name='Memory_Type', choices=[(b'ddr2', 'DDR2'), (b'ddr3', 'DDR3')])),
                ('speed', models.PositiveSmallIntegerField(verbose_name='Memory_Frequency(MHz)')),
                ('size', models.PositiveSmallIntegerField(verbose_name='Memory_Size(MB)')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
            ],
            options={
                'verbose_name': 'Server_Memory_Type',
                'verbose_name_plural': 'Server_Memory_Type_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerNIC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='Nic_Model')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Nic_Manufacturer')),
                ('speed', models.CharField(default=b'1000', max_length=5, verbose_name='Nic_Max_Speend(Mbps)', choices=[(b'100', b'100Base'), (b'1000', b'1000Base'), (b'10000', b'10000Base')])),
                ('eom', models.BooleanField(default=True, verbose_name='Nic_Board_Type')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
            ],
            options={
                'verbose_name': 'Server_Nic_Type',
                'verbose_name_plural': 'Server_Nic_Type_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerRaidCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='Raid_Card_Model')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Raid_Card_Manufacturer')),
                ('cache', models.PositiveSmallIntegerField(verbose_name='Raid_Card_Cache_Size(MB)')),
                ('battery', models.BooleanField(default=True, verbose_name='Raid_Card_Battery')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
            ],
            options={
                'verbose_name': 'Server_Raid_Card_Type',
                'verbose_name_plural': 'Server_Raid_Card_Type_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerRaidLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.PositiveSmallIntegerField(unique=True, max_length=2, verbose_name='Raid_Level')),
                ('min_hds', models.PositiveSmallIntegerField(max_length=1, verbose_name='Min_Hds_Num')),
                ('max_hds', models.PositiveSmallIntegerField(max_length=2, verbose_name='Max_Hds_Num')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
            ],
            options={
                'verbose_name': 'Server_Raid_Level',
                'verbose_name_plural': 'Server_Raid_Level_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerTemplateHDS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hd_type', models.ForeignKey(verbose_name='Disk_Type', to='inv.ServerHD')),
                ('server', models.ForeignKey(to='inv.ServerAssetTemplate')),
            ],
            options={
                'verbose_name': 'Server Template Disk Info',
                'verbose_name_plural': 'Server Template Disk Info Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerTemplateNICS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nic_type', models.ForeignKey(verbose_name='Nic_Type', to='inv.ServerNIC')),
                ('server', models.ForeignKey(to='inv.ServerAssetTemplate')),
            ],
            options={
                'verbose_name': 'Server_Template_Nic_Info',
                'verbose_name_plural': 'Server_Template_Nic_Info_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='Supplier_Name')),
                ('seller', models.CharField(max_length=30, verbose_name='Seller')),
                ('address', models.CharField(max_length=100, verbose_name='Supplier_Addr')),
                ('phone', models.CharField(max_length=20, verbose_name='Supplier_Phone')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Supplier_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SwitchAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=25, verbose_name='SN')),
                ('purchase_date', models.DateField(verbose_name='Purchase_Date')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
                ('supplier', models.ForeignKey(verbose_name='Supplier', to='inv.Supplier')),
            ],
            options={
                'verbose_name': 'Switch_Asset_Info',
                'verbose_name_plural': 'Switch_Asset_Info_Management',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SwitchAssetTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name='Asset_Template_Name')),
                ('manufacturer', models.CharField(max_length=20, verbose_name='Asset_Manufacturer')),
                ('height', models.PositiveSmallIntegerField(verbose_name='Height(U)')),
                ('exterior', models.ImageField(upload_to=b'asset', verbose_name='Exterior_Photo')),
                ('notes', models.TextField(max_length=200, verbose_name='Remark', blank=True)),
                ('suppliers', models.ManyToManyField(to='inv.Supplier', verbose_name='Supplier')),
            ],
            options={
                'verbose_name': 'Switch_Asset_Template',
                'verbose_name_plural': 'Switch_Asset_Template_Management',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='switchasset',
            name='template',
            field=models.ForeignKey(verbose_name='Switch_Template', to='inv.SwitchAssetTemplate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serverraidcard',
            name='support_raids',
            field=models.ManyToManyField(to='inv.ServerRaidLevel', verbose_name='Raid_Card_Support_RaidLevel'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='servermemory',
            unique_together=set([('memory_type', 'speed', 'size')]),
        ),
        migrations.AddField(
            model_name='serverassettemplate',
            name='cpu',
            field=models.ForeignKey(verbose_name='Default_CPU_Type', to='inv.ServerCPU'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serverassettemplate',
            name='hds',
            field=models.ManyToManyField(to='inv.ServerHD', through='inv.ServerTemplateHDS'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serverassettemplate',
            name='memory',
            field=models.ForeignKey(verbose_name='Memory_Model', to='inv.ServerMemory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serverassettemplate',
            name='nics',
            field=models.ManyToManyField(to='inv.ServerNIC', through='inv.ServerTemplateNICS'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serverassettemplate',
            name='suppliers',
            field=models.ManyToManyField(to='inv.Supplier', verbose_name='Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serverasset',
            name='supplier',
            field=models.ForeignKey(verbose_name='Supplier', to='inv.Supplier'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='serverasset',
            name='template',
            field=models.ForeignKey(verbose_name='Server_Template', to='inv.ServerAssetTemplate'),
            preserve_default=True,
        ),
    ]
