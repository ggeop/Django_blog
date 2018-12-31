# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_auto_20181231_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=7, default='none', choices=[('none', None), ('android', 'ANDROID'), ('iphone', 'IPHONE')]),
        ),
    ]
