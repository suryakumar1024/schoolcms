# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20161005_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_mark',
            field=models.CharField(default=0, max_length=3, null=True),
        ),
    ]
