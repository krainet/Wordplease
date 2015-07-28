# -*- coding: utf-8 -*-
__author__ = 'hadock'
from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostQuerySet
from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(PostQuerySet, ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_post_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
