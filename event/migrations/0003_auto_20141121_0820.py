# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20141014_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='evt_end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='events',
            name='evt_start_time',
            field=models.DateTimeField(),
        ),
    ]
