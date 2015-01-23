# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_events_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exception',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ex_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Alarms',
            new_name='Alarm',
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.RenameModel(
            old_name='Periods',
            new_name='Period',
        ),
        migrations.RemoveField(
            model_name='exceptions',
            name='evt',
        ),
        migrations.DeleteModel(
            name='Exceptions',
        ),
        migrations.AddField(
            model_name='exception',
            name='evt',
            field=models.ForeignKey(to='event.Event'),
            preserve_default=True,
        ),
    ]
