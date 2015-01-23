# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20141121_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='evt_end_time',
            field=models.TimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='events',
            name='evt_start_time',
            field=models.TimeField(),
            preserve_default=True,
        ),
    ]
