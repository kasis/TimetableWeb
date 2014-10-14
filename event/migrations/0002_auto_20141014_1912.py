# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarms',
            old_name='evt_id',
            new_name='evt',
        ),
        migrations.RenameField(
            model_name='events',
            old_name='per_id',
            new_name='per',
        ),
        migrations.RenameField(
            model_name='exceptions',
            old_name='evt_id',
            new_name='evt',
        ),
    ]
