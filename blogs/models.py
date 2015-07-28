# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


PENDING = u'PEND'
PUBLISHED = u'PUB'
DELETED = u'DEL'
ACTIVE = u'ACT'
DISABLED = u'DIS'

BLOG_STATUS = (
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


