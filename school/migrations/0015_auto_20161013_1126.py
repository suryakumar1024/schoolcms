# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0014_auto_20161012_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(default=b'-', max_length=2, choices=[(b'F', b'Female'), (b'M', b'Male')]),
        ),
    ]
