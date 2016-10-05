# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_age', models.IntegerField(null=True)),
                ('staff_sex', models.CharField(max_length=2, choices=[(b'M', b'male'), (b'F', b'Female')])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_name', models.CharField(max_length=50)),
                ('student_age', models.IntegerField(null=True)),
                ('student_sex', models.CharField(max_length=2, choices=[(b'M', b'male'), (b'F', b'Female')])),
                ('fk_primary_class', models.ForeignKey(to='school.PrimaryClass')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject_name', models.CharField(max_length=50)),
                ('subject_mark', models.IntegerField()),
                ('primary_class', models.ForeignKey(to='school.PrimaryClass')),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_subject',
            field=models.ManyToManyField(to='school.Subject'),
        ),
    ]
