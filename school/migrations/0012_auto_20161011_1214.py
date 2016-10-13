# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20161007_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_name',
            field=models.CharField(max_length=128, validators=[django.core.validators.RegexValidator(regex=b'^[a-zA-Z ]+$', message=b'no numbers')]),
        ),
    ]
