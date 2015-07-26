# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20150726_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 12, 4, 36, 343640, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 12, 4, 42, 719021, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 12, 4, 47, 998899, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 26, 12, 4, 52, 734512, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
