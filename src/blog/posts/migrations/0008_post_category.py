# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20181231_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=6, default='all', choices=[('all', 'ALL'), ('android', 'ANDROID'), ('iphone', 'IPHONE')]),
        ),
    ]
