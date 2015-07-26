# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


PENDING = u'PEND'
PUBLISHED = u'PUB'
DELETED = u'DEL'
ACTIVE = u'ACT'
DISABLED = u'DIS'

POST_STATUS = (
    (PENDING, 'Pendiente Moderación'),
    (PUBLISHED, 'Publicado'),
    (DELETED, 'Eliminado')
)

BLOG_STATUS = (
    (ACTIVE, u'Activated'),
    (DISABLED, u'Disabled')
)

CATEGORY_STATUS = (
    (ACTIVE, u'Activated'),
    (DISABLED, u'Disabled')
)


class Blog(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True, default="")
    status = models.CharField(max_length=10, choices=BLOG_STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class Category(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True, default="")
    status = models.CharField(max_length=10, choices=CATEGORY_STATUS, default=ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    owner = models.ForeignKey(User)
    categories = models.ManyToManyField('Category')
    blog = models.ForeignKey(Blog)
    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    # body = models.TextField(blank=True, null=True, default="", validators=[badwords_detector])
    body = models.TextField(blank=True, null=True, default="")
    image_url = models.URLField()
    status = models.CharField(max_length=10, choices=POST_STATUS, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title