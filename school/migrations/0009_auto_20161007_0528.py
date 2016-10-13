# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20161007_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_mark',
            field=models.CharField(default=0, max_length=3, null=True, validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'Only numeric characters are allowed.')]),
        ),
    ]
