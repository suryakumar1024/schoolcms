# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_auto_20161005_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='fk_subject',
        ),
        migrations.AddField(
            model_name='subject',
            name='fk_student',
            field=models.ForeignKey(to='school.Student', null=True),
        ),
    ]
