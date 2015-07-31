# -*- coding: utf-8 -*-
from posts.models import Post
from django.core.urlresolvers import reverse
__author__ = 'hadock'
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ('owner', 'status', 'blog')


class PostListSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):  # ojo a heredar correctamente la clase meta también!!!!
        fields = ('id', 'title', 'image_url')

