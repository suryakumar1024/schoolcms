# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20161005_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fk_subject',
            field=models.ForeignKey(to='school.Subject', null=True),
        ),
    ]
