# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_auto_20161011_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_mark',
            field=models.CharField(default=b'N/A', max_length=3, null=True),
        ),
    ]
