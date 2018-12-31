# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(max_length=7, null=True, default='all', choices=[('all', 'ALL'), ('android', 'ANDROID'), ('iphone', 'IPHONE')]),
        ),
    ]
