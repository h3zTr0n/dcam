# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_auto_20160110_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
