# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='staff_subject',
        ),
        migrations.RemoveField(
            model_name='student',
            name='fk_primary_class',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='primary_class',
        ),
        migrations.DeleteModel(
            name='PrimaryClass',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
