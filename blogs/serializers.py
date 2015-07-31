# -*- coding: utf-8 -*-
from blogs.models import Blog
from django.core.urlresolvers import reverse

__author__ = 'hadock'
from rest_framework import serializers



class BlogSerializer(serializers.ModelSerializer):
    my_blog_url = serializers.SerializerMethodField('get_blog_url')

    class Meta:
        model = Blog
        read_only_fields = ('owner',)
        fields = ('id', 'title', 'image_url', 'my_blog_url')

    def get_blog_url(self, obj):
        return self.context['request'].build_absolute_uri(reverse('blog_detail', kwargs={'username': obj.owner, 'pk': obj.pk}))


class BlogListSerializer(BlogSerializer):
    my_blog_url = serializers.SerializerMethodField('get_blog_url')

    class Meta(BlogSerializer.Meta):  # ojo a heredar correctamente la clase meta también!!!!

        fields = ('id', 'title', 'image_url', 'my_blog_url')
