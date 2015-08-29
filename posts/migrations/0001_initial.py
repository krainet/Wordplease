# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('short_description', models.CharField(max_length=255)),
                ('image_url', models.URLField(default=b'', null=True, blank=True)),
                ('status', models.CharField(default='ACT', max_length=10, choices=[('ACT', 'Activated'), ('DIS', 'Disabled')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('short_description', models.CharField(max_length=255)),
                ('body', models.TextField(default=b'', null=True, blank=True)),
                ('image_url', models.URLField()),
                ('status', models.CharField(default='PUB', max_length=10, choices=[('PEND', b'Pendiente Moderacion'), ('PUB', b'Publicado'), ('DEL', b'Eliminado')])),
                ('post_type', models.CharField(default='PUB', max_length=10, choices=[('PUB', 'Public'), ('PRIV', 'Private')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(to='blogs.Blog')),
                ('categories', models.ManyToManyField(to='posts.Category')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
