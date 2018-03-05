# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-01 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.CharField(choices=[('comment', 'Comment'), ('activity', 'Activity')], default='comment', max_length=30),
            preserve_default=False,
        ),
    ]
