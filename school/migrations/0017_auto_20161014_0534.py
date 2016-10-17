# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0016_auto_20161014_0443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='period',
            old_name='fk_primary_class',
            new_name='fk_timetable',
        ),
    ]
