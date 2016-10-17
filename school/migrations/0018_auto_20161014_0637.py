# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_auto_20161014_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='fk_primary_class',
            field=models.ForeignKey(to='school.PrimaryClass'),
        ),
    ]
