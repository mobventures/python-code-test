# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0004_auto_20160407_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='photo_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='items.PhotoItem', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stream',
            name='tweet_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='items.TweetItem', null=True),
            preserve_default=True,
        ),
    ]
