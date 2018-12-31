# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20181231_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=7, default=None, choices=[('all', 'ALL'), ('android', 'ANDROID'), ('iphone', 'IPHONE')]),
        ),
    ]
