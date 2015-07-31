# -*- coding: utf-8 -*-
__author__ = 'hadock'
from blogs.serializers import BlogSerializer, BlogListSerializer
from blogs.views import BlogQuerySet
from rest_framework.viewsets import ModelViewSet
from blogs.models import Blog
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BlogViewSet(BlogQuerySet, ModelViewSet):
    queryset = Blog.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogListSerializer
        else:
            return BlogSerializer

        # return BlogSerializer if self.request.method == 'POST' else BlogListSerializer

    def get_queryset(self):
        return self.get_blog_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
