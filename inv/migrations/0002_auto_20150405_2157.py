# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servertemplatehds',
            options={'verbose_name': 'Server Template Disk Info', 'verbose_name_plural': 'Server_Template_Disk_Info_Management'},
        ),
    ]
