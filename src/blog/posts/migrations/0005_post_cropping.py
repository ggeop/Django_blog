# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20181230_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '750x300', free_crop=False, adapt_rotation=False, allow_fullsize=False, verbose_name='cropping', help_text=None, hide_image_field=False, size_warning=False),
        ),
    ]
