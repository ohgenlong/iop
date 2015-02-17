# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiAuth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=64, verbose_name='\ufffd\u04ff\ufffdurl')),
                ('description', models.CharField(max_length=64, verbose_name='\ufffd\ufffd\ufffd')),
                ('method_type', models.CharField(max_length=32, verbose_name='\ufffd\ufffd\ufffd\xf7\ufffd\ufffd\ufffd', choices=[(b'GET', b'\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbdGet(\xef\xbf\xbd\xc9\xb6\xef\xbf\xbd)'), (b'POST', b'\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbdPOST(\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xde\xb8\xef\xbf\xbd)'), (b'PUT', b'\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbdPUT(\xef\xbf\xbd\xef\xbf\xbd \xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd)'), (b'HEAD', b'HEAD(\xef\xbf\xbd\xdd\xb2\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd)'), (b'PATCH', b'PATCH(\xef\xbf\xbd\xdd\xb2\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd)')])),
            ],
            options={
                'verbose_name': '\ufffd\u04ff\ufffd\u0228\ufffd\ufffd',
                'verbose_name_plural': '\ufffd\u04ff\ufffd\u0228\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_type', models.CharField(default=b'server', max_length=64, choices=[(b'server', '\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd'), (b'switch', '\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd'), (b'router', '\xb7\ufffd\ufffd\ufffd\ufffd'), (b'firewall', '\ufffd\ufffd\ufffd\ufffd\u01fd'), (b'storage', '\ufffd\u6d22\ufffd\u8c78'), (b'acc_cpu', 'CPU'), (b'acc_memory', '\ufffd\u06b4\ufffd\ufffd\ufffd'), (b'acc_disk', '\u04f2\ufffd\ufffd'), (b'acc_network_adapter', '\ufffd\ufffd\ufffd\ufffd'), (b'acc_monitor', '\ufffd\ufffd\u02be\ufffd\ufffd'), (b'acc_others', '\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd')])),
                ('name', models.CharField(max_length=30)),
                ('hostname', models.CharField(unique=True, max_length=32, blank=True)),
                ('asset_op', models.CharField(max_length=32, null=True, blank=True)),
                ('trade_time', models.DateTimeField(null=True, verbose_name='\ufffd\ufffd\ufffd\ufffd\u02b1\ufffd\ufffd', blank=True)),
                ('warranty', models.SmallIntegerField(null=True, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('price', models.IntegerField(null=True, verbose_name='\ufffd\u06f8\ufffd', blank=True)),
                ('function', models.CharField(max_length=32, null=True, blank=True)),
                ('cabinet_num', models.CharField(max_length=30, null=True, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('cabinet_order', models.SmallIntegerField(null=True, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('memo', models.TextField(null=True, verbose_name='\ufffd\ufffd\u05e2', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\ufffd\u02b2\ufffd\ufffd\u0731\ufffd',
                'verbose_name_plural': '\ufffd\u02b2\ufffd\ufffd\u0731\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u04b5\ufffd\ufffd\ufffd\ufffd')),
                ('memo', models.CharField(max_length=64, verbose_name='\ufffd\ufffd\u05e2', blank=True)),
            ],
            options={
                'verbose_name': '\u04b5\ufffd\ufffd\ufffd\ufffd',
                'verbose_name_plural': '\u04b5\ufffd\ufffd\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BusinessUnitLevel2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\ufffd\ufffd\ufffd\ufffd\u04b5\ufffd\ufffd\ufffd\ufffd')),
                ('memo', models.CharField(max_length=64, verbose_name='\ufffd\ufffd\u05e2', blank=True)),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\ufffd\ufffd\u04b5\ufffd\ufffd\ufffd\ufffd',
                'verbose_name_plural': '\ufffd\ufffd\ufffd\ufffd\u04b5\ufffd\ufffd\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('definded_raid_type', models.CharField(max_length=32, null=True, verbose_name='\u0524\ufffd\ufffd\ufffd\ufffdraid\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('management_ip', models.CharField(max_length=64, null=True, verbose_name='\ufffd\ufffd\ufffd\ufffdIP', blank=True)),
                ('os_installed', models.BooleanField(default=False)),
                ('puppet_installed', models.BooleanField(default=False)),
                ('zabbix_configured', models.BooleanField(default=False)),
                ('auditing_configured', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
                ('asset', models.OneToOneField(default=None, to='website.Asset')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=64, verbose_name='\ufffd\ufffd\u036c\ufffd\ufffd')),
                ('name', models.CharField(max_length=64, verbose_name='\ufffd\ufffd\u036c\ufffd\ufffd\ufffd\ufffd')),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
                ('cost', models.IntegerField(verbose_name='\ufffd\ufffd\u036c\ufffd\ufffd\ufffd')),
                ('start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('license_num', models.IntegerField(verbose_name='license\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\u036c',
                'verbose_name_plural': '\ufffd\ufffd\u036c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=64, verbose_name='SN\ufffd\ufffd', blank=True)),
                ('parent_sn', models.CharField(unique=True, max_length=128, blank=True)),
                ('manufactory', models.CharField(default=None, max_length=32, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('model', models.CharField(max_length=64, verbose_name='CPU\ufffd\u037a\ufffd', blank=True)),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
            ],
            options={
                'verbose_name': 'CPU\ufffd\ufffd\ufffd\ufffd',
                'verbose_name_plural': 'CPU\ufffd\ufffd\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Disk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, verbose_name='SN\ufffd\ufffd', blank=True)),
                ('parent_sn', models.CharField(max_length=128, blank=True)),
                ('slot', models.CharField(max_length=32, verbose_name='\ufffd\ufffd\ufffd\u03bb', blank=True)),
                ('manufactory', models.CharField(default=None, max_length=32, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('model', models.CharField(max_length=128, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\u037a\ufffd', blank=True)),
                ('capacity', models.FloatField(verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdGB', blank=True)),
                ('iface_type', models.CharField(blank=True, max_length=64, verbose_name='\ufffd\u04ff\ufffd\ufffd\ufffd\ufffd\ufffd', choices=[(b'SATA', b'SATA'), (b'SAS', b'SAS'), (b'SCSI', b'SCSI'), (b'SSD', b'SSD')])),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u04f2\ufffd\u0332\ufffd\ufffd\ufffd',
                'verbose_name_plural': '\u04f2\ufffd\u0332\ufffd\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(unique=True, max_length=128, verbose_name='\ufffd\ufffd\ufffd\ufffdID')),
                ('post_data', models.TextField(verbose_name='\ufffd\ufffd\ufffd\ufffdData', blank=True)),
                ('detail', models.TextField(verbose_name='\ufffd\ufffd\u03f8\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\ufffd\ufffd\ufffd\ufffdenglish')),
                ('display_name', models.CharField(default=None, max_length=32, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\u02be\ufffd\ufffd')),
                ('region', models.CharField(default=None, max_length=64, verbose_name='\ufffd\ufffd\ufffd\ufffd')),
                ('region_display_name', models.CharField(default=None, max_length=64, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd')),
                ('isp', models.CharField(default=None, max_length=32, verbose_name='\ufffd\ufffd\u04ea\ufffd\ufffd')),
                ('isp_display_name', models.CharField(default=None, max_length=32, verbose_name='\ufffd\ufffd\u04ea\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd')),
                ('floor', models.IntegerField(default=1, verbose_name='\xa5\ufffd\ufffd')),
                ('memo', models.CharField(max_length=64, verbose_name='\ufffd\ufffd\u05e2')),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\ufffd\ufffd',
                'verbose_name_plural': '\ufffd\ufffd\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Maintainence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\ufffd\xbc\ufffd\ufffd\ufffd\ufffd\ufffd')),
                ('maintain_type', models.SmallIntegerField(max_length=30, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', choices=[(1, '\u04f2\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd'), (2, '\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd'), (3, '\ufffd\u8c78\ufffd\ufffd\ufffd\ufffd'), (4, '\ufffd\u8c78\ufffd\ufffd\ufffd\ufffd'), (5, '\ufffd\ufffd\ufffd\ufffd\u03ac\ufffd\ufffd'), (6, '\u04b5\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\\\ufffd\ufffd\ufffd\ufffd\\\ufffd\ufffd\ufffd'), (7, '\ufffd\ufffd\ufffd\ufffd')])),
                ('description', models.TextField(verbose_name='\ufffd\xbc\ufffd\ufffd\ufffd\ufffd\ufffd')),
                ('device_sn', models.CharField(max_length=64, verbose_name=b'AssetID', blank=True)),
                ('event_start', models.DateTimeField(verbose_name='\ufffd\xbc\ufffd\ufffd\ufffd\u02bc\u02b1\ufffd\ufffd', blank=True)),
                ('event_end', models.DateTimeField(verbose_name='\ufffd\xbc\ufffd\ufffd\ufffd\ufffd\ufffd\u02b1\ufffd\ufffd', blank=True)),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\ufffd\ufffd\ufffd\xbc',
                'verbose_name_plural': '\ufffd\ufffd\ufffd\ufffd\ufffd\xbc',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Manufactory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd')),
                ('support_num', models.CharField(max_length=30, verbose_name='\u05a7\ufffd\u05b5\u7ef0', blank=True)),
                ('memo', models.CharField(max_length=30, verbose_name='\ufffd\ufffd\u05e2', blank=True)),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\ufffd\ufffd',
                'verbose_name_plural': '\ufffd\ufffd\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, verbose_name='SN\ufffd\ufffd', blank=True)),
                ('parent_sn', models.CharField(max_length=128, blank=True)),
                ('model', models.CharField(max_length=64, verbose_name='\ufffd\u037a\ufffd', blank=True)),
                ('manufactory', models.CharField(max_length=32, null=True, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('slot', models.CharField(max_length=32, verbose_name='\ufffd\ufffd\ufffd\u03bb', blank=True)),
                ('capacity', models.FloatField(verbose_name='\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\ufffd\u06b4\u6cbf\ufffd\ufffd',
                'verbose_name_plural': '\ufffd\u06b4\u6cbf\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=64, verbose_name='SN\ufffd\ufffd')),
                ('manufactory', models.CharField(default=None, max_length=32, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd')),
                ('model', models.CharField(max_length=64, verbose_name='\ufffd\ufffd\u02be\ufffd\u8c78\ufffd\u037a\ufffd')),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
                ('asset', models.OneToOneField(to='website.Asset')),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\u02be\ufffd\u8c78',
                'verbose_name_plural': '\ufffd\ufffd\u02be\ufffd\u8c78',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NetworkDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(unique=True, max_length=64, verbose_name='SN\ufffd\ufffd')),
                ('manufactory', models.CharField(max_length=128, null=True, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('model', models.CharField(max_length=128, null=True, verbose_name='\ufffd\u037a\ufffd', blank=True)),
                ('port_num', models.SmallIntegerField(verbose_name='\ufffd\u02ff\u06b8\ufffd\ufffd\ufffd')),
                ('device_detail', models.TextField(verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\u03f8\ufffd\ufffd\ufffd\ufffd')),
                ('asset', models.OneToOneField(to='website.Asset')),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\ufffd\ufffd\ufffd\u8c78',
                'verbose_name_plural': '\ufffd\ufffd\ufffd\ufffd\ufffd\u8c78',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NIC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\ufffd\ufffd\ufffd', blank=True)),
                ('sn', models.CharField(max_length=128, verbose_name='SN\ufffd\ufffd', blank=True)),
                ('parent_sn', models.CharField(max_length=128, blank=True)),
                ('model', models.CharField(max_length=128, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\u037a\ufffd', blank=True)),
                ('manufactory', models.CharField(max_length=32, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('ipaddr', models.IPAddressField(verbose_name='ip\ufffd\ufffd\u05b7', blank=True)),
                ('mac', models.CharField(max_length=64, verbose_name='\ufffd\ufffd\ufffd\ufffdmac\ufffd\ufffd\u05b7')),
                ('netmask', models.CharField(max_length=64, blank=True)),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd',
                'verbose_name_plural': '\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NICConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='\ufffd\ufffd\ufffd', blank=True)),
                ('ipaddr', models.IPAddressField(verbose_name='ip\ufffd\ufffd\u05b7', blank=True)),
                ('mac', models.CharField(max_length=64, verbose_name='\ufffd\ufffd\ufffd\ufffdmac\ufffd\ufffd\u05b7')),
                ('netmask', models.CharField(max_length=64, blank=True)),
                ('gateway', models.IPAddressField(verbose_name='\ufffd\ufffd\ufffd\ufffd')),
                ('bonding', models.BooleanField(default=False)),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\ufffd\xf1\ufffd_\ufffd\ufffd\ufffd\ufffd',
                'verbose_name_plural': '\ufffd\ufffd\ufffd\xf1\ufffd_\ufffd\ufffd\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\ufffd\ufffd\u01b7\ufffd\u037a\ufffd')),
                ('version', models.CharField(max_length=64, verbose_name='\ufffd\ufffd\u01b7\ufffd\u6c7e\ufffd\ufffd', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RaidAdaptor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sn', models.CharField(max_length=128, verbose_name='SN\ufffd\ufffd', blank=True)),
                ('name', models.CharField(max_length=32, verbose_name='\ufffd\ufffd\ufffd', blank=True)),
                ('parent_sn', models.CharField(max_length=128, blank=True)),
                ('model', models.CharField(max_length=64, verbose_name='\ufffd\u037a\ufffd', blank=True)),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_by', models.CharField(default=b'auto', max_length=32)),
                ('sn', models.CharField(max_length=64, verbose_name='SN\ufffd\ufffd')),
                ('management_ip', models.CharField(max_length=64, null=True, verbose_name='\ufffd\ufffd\ufffd\ufffdIP', blank=True)),
                ('manufactory', models.CharField(max_length=128, null=True, verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('model', models.CharField(max_length=128, null=True, verbose_name='\ufffd\u037a\ufffd', blank=True)),
                ('cpu_count', models.SmallIntegerField(verbose_name='cpu\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('cpu_core_count', models.SmallIntegerField(verbose_name='cpu\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('raid_type', models.TextField(verbose_name='raid\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('ram_size', models.IntegerField(verbose_name='\ufffd\u06b4\ufffd\ufffd\u0734\ufffd\u0421GB', blank=True)),
                ('os_type', models.CharField(max_length=64, null=True, verbose_name='\ufffd\ufffd\ufffd\ufffd\u03f5\u0373\ufffd\ufffd\ufffd\ufffd', blank=True)),
                ('os_distribution', models.CharField(max_length=64, null=True, verbose_name='\ufffd\ufffd\ufffd\u0370\u6c7e', blank=True)),
                ('os_version', models.CharField(max_length=64, null=True, verbose_name='\ufffd\ufffd\ufffd\ufffd\u03f5\u0373\ufffd\u6c7e', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(blank=True)),
                ('asset', models.OneToOneField(to='website.Asset')),
                ('cpu_model', models.ForeignKey(to='website.CPU')),
                ('nic', models.ManyToManyField(to='website.NIC', verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\u0431\ufffd')),
                ('physical_disk_driver', models.ManyToManyField(to='website.Disk', verbose_name='\u04f2\ufffd\ufffd', blank=True)),
                ('raid_adaptor', models.ManyToManyField(to='website.RaidAdaptor', verbose_name='Raid\ufffd\ufffd', blank=True)),
                ('ram', models.ManyToManyField(to='website.Memory', verbose_name='\ufffd\u06b4\ufffd\ufffd\ufffd\ufffd\ufffd', blank=True)),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd',
                'verbose_name_plural': '\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('types', models.SmallIntegerField(help_text='eg. GNU/Linux', max_length=64, verbose_name='\u03f5\u0373\ufffd\ufffd\ufffd\ufffd', choices=[(1, b'GNU/Linux'), (2, b'MS/Windows'), (3, b'Network Firmware'), (4, b'Softwares')])),
                ('version', models.CharField(help_text='eg. CentOS release 6.5 (Final)', unique=True, max_length=64, verbose_name='\ufffd\ufffd\ufffd/\u03f5\u0373\ufffd\u6c7e')),
            ],
            options={
                'verbose_name': '\ufffd\ufffd\ufffd/\u03f5\u0373',
                'verbose_name_plural': '\ufffd\ufffd\ufffd/\u03f5\u0373',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.SmallIntegerField(unique=True, verbose_name='\ufffd\u8c78\u05f4\u032c', choices=[(1, b'Init'), (2, b'Standby'), (3, b'Online'), (4, b'Offline'), (5, b'Unreachable'), (6, b'Deprecated'), (7, b'Maintenance')])),
                ('os_installed', models.BooleanField(default=False)),
                ('puppet_installed', models.BooleanField(default=False)),
                ('zabbix_configured', models.BooleanField(default=False)),
                ('auditing_configured', models.BooleanField(default=False)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\ufffd\ufffd\ufffd\ufffd')),
                ('token', models.CharField(max_length=128, null=True, verbose_name='token', blank=True)),
                ('department', models.CharField(max_length=32, verbose_name='\ufffd\ufffd\ufffd\ufffd')),
                ('email', models.EmailField(max_length=75, verbose_name='\ufffd\ufffd\ufffd\ufffd')),
                ('phone', models.CharField(max_length=32, verbose_name='\ufffd\ufffd\ufffd\ufffd')),
                ('mobile', models.CharField(max_length=32, verbose_name='\ufffd\u05bb\ufffd')),
                ('memo', models.TextField(verbose_name='\ufffd\ufffd\u05e2', blank=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('backup_name', models.ForeignKey(related_name='user_backup_name', verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\u03f5\ufffd\ufffd', blank=True, to='website.UserProfile', null=True)),
                ('business_unit', models.ManyToManyField(to='website.BusinessUnit')),
                ('leader', models.ForeignKey(verbose_name=b'\xef\xbf\xbd\xcf\xbc\xef\xbf\xbd\xef\xbf\xbd\xec\xb5\xbc', blank=True, to='website.UserProfile', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\ufffd\xfb\ufffd\ufffd\ufffd\u03e2',
                'verbose_name_plural': '\ufffd\xfb\ufffd\ufffd\ufffd\u03e2',
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='server',
            index_together=set([('sn', 'asset')]),
        ),
        migrations.AlterUniqueTogether(
            name='raidadaptor',
            unique_together=set([('parent_sn', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='nicconfig',
            unique_together=set([('name', 'mac')]),
        ),
        migrations.AlterUniqueTogether(
            name='nic',
            unique_together=set([('name', 'mac')]),
        ),
        migrations.AddField(
            model_name='networkdevice',
            name='firmware',
            field=models.ForeignKey(to='website.Software'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='memory',
            unique_together=set([('parent_sn', 'slot')]),
        ),
        migrations.AddField(
            model_name='maintainence',
            name='applicant',
            field=models.ForeignKey(related_name='applicant_user', verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd', to='website.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='maintainence',
            name='performer',
            field=models.ForeignKey(verbose_name='\u05b4\ufffd\ufffd\ufffd\ufffd', to='website.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='disk',
            unique_together=set([('parent_sn', 'slot')]),
        ),
        migrations.AddField(
            model_name='configuration',
            name='nic',
            field=models.ManyToManyField(to='website.NICConfig', verbose_name='\ufffd\ufffd\ufffd\ufffd\ufffd\u0431\ufffd', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configuration',
            name='os',
            field=models.ForeignKey(verbose_name=b'OS', blank=True, to='website.Software', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='businessunit',
            name='contact',
            field=models.ForeignKey(default=None, to='website.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='admin',
            field=models.ForeignKey(related_name='+', verbose_name='\ufffd\u8c78\ufffd\ufffd\ufffd\ufffd\u0531', blank=True, to='website.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit',
            field=models.ForeignKey(verbose_name='\ufffd\ufffd\ufffd\u06b5\ufffd\u04b5\ufffd\ufffd\ufffd\ufffd', blank=True, to='website.BusinessUnit', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='business_unit_level2',
            field=models.ForeignKey(verbose_name='2\ufffd\ufffd\u04b5\ufffd\ufffd\ufffd\ufffd', blank=True, to='website.BusinessUnitLevel2', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='contract',
            field=models.ForeignKey(verbose_name='\ufffd\ufffd\u036c', blank=True, to='website.Contract', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(verbose_name='IDC\ufffd\ufffd\ufffd\ufffd', blank=True, to='website.IDC', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.ForeignKey(default=1, verbose_name='\ufffd\u8c78\u05f4\u032c', to='website.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apiauth',
            name='users',
            field=models.ManyToManyField(to='website.UserProfile', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='apiauth',
            unique_together=set([('url', 'method_type')]),
        ),
    ]