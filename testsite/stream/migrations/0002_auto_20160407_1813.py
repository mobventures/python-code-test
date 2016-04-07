# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='photo_item',
            field=models.OneToOneField(default=None, to='items.PhotoItem'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='stream',
            name='tweet_item',
            field=models.OneToOneField(default=None, to='items.TweetItem'),
            preserve_default=True,
        ),
    ]
