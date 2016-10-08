# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-08 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=20)),
                ('task_desc', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(verbose_name='task creation date')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.Student')),
            ],
        ),
    ]
