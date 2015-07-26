# -*- coding: utf-8 -*-
from blogs.models import Post, Blog
from django.core.urlresolvers import reverse

__author__ = 'hadock'
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ('owner',)

class PostListSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):  # ojo a heredar correctamente la clase meta también!!!!
        fields = ('id', 'title', 'image_url')


class BlogSerializer(serializers.ModelSerializer):
    # my_blog_url = serializers.SerializerMethodField('get_blog_url')

    class Meta:
        model = Blog
        read_only_fields = ('owner',)
        fields = ('id', 'title', 'image_url',)

    # def get_blog_url(self, obj):
    #     return reverse('blogs_detail', args=[obj.pk])


class BlogListSerializer(BlogSerializer):
    class Meta(BlogSerializer.Meta):  # ojo a heredar correctamente la clase meta también!!!!
        fields = ('id', 'title', 'image_url',)