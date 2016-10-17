# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_auto_20161013_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_period', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_of_day', models.CharField(max_length=10)),
                ('fk_primary_class', models.OneToOneField(to='school.PrimaryClass')),
            ],
        ),
        migrations.AddField(
            model_name='period',
            name='fk_primary_class',
            field=models.ForeignKey(to='school.Timetable'),
        ),
    ]
