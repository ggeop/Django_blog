# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import image_cropping.fields
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_cropping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=image_cropping.fields.ImageCropField(blank=True, null=True, upload_to=posts.models.upload_location),
        ),
    ]
