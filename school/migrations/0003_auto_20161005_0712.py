# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20161005_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('staff_name', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=2, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('fk_primary_class', models.OneToOneField(to='school.PrimaryClass')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_name', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=2, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('fk_primary_class', models.ForeignKey(to='school.PrimaryClass')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=128)),
                ('subject_mark', models.CharField(max_length=3, null=True)),
                ('fk_primary_class', models.ForeignKey(to='school.PrimaryClass')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='fk_subject',
            field=models.ForeignKey(to='school.Subject'),
        ),
        migrations.AddField(
            model_name='staff',
            name='fk_subject',
            field=models.OneToOneField(to='school.Subject'),
        ),
    ]
