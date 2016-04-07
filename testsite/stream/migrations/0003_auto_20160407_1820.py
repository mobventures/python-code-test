# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_auto_20160407_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='photo_item',
            field=models.ForeignKey(to='items.PhotoItem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='tweet_item',
            field=models.ForeignKey(to='items.TweetItem'),
            preserve_default=True,
        ),
    ]
