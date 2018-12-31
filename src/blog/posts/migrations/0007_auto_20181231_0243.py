# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20181231_0233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='cropping',
        ),
        migrations.AlterField(
            model_name='post',
            name='height_field',
            field=models.IntegerField(default=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.upload_location, width_field='width_field', height_field='height_field'),
        ),
        migrations.AlterField(
            model_name='post',
            name='width_field',
            field=models.IntegerField(default=750),
        ),
    ]
