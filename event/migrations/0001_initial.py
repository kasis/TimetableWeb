# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alm_time', models.BigIntegerField()),
                ('alm_type', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evt_name', models.CharField(max_length=45)),
                ('evt_place', models.CharField(max_length=45)),
                ('evt_start_time', models.TimeField()),
                ('evt_end_time', models.TimeField()),
                ('evt_date', models.DateField()),
                ('evt_note', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exceptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ex_date', models.DateField()),
                ('evt_id', models.ForeignKey(to='event.Events')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Periods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('per_type', models.IntegerField()),
                ('per_interval', models.IntegerField()),
                ('per_week_occurences', models.IntegerField()),
                ('per_end_date', models.DateField()),
                ('per_num_of_repeats', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='events',
            name='per_id',
            field=models.ForeignKey(to='event.Periods'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='alarms',
            name='evt_id',
            field=models.ForeignKey(to='event.Events'),
            preserve_default=True,
        ),
    ]
