# -*- coding: utf-8 -*-
from blogs.models import Blog
from posts.permissions import PostPermission
__author__ = 'hadock'
from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostQuerySet
from rest_framework.viewsets import ModelViewSet
from posts.models import Post, PUBLISHED


class PostViewSet(PostQuerySet, ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (PostPermission,)

    def get_queryset(self):
        return self.get_post_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostSerializer

    def perform_create(self, serializer):
        blog = Blog.objects.filter(owner=self.request.user)[0]
        serializer.save(owner=self.request.user, status=PUBLISHED, blog=blog)

