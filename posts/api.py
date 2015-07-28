# -*- coding: utf-8 -*-
from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostQuerySet

__author__ = 'hadock'
from posts.models import Post
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostListAPI(PostQuerySet, ListCreateAPIView):
    queryset = Post.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)

    #  Al sobreescribir este método podemos usar un serializador u
    #  otro en funcion del metodo de la vista generica ListCreateApiView

    def get_serializer_class(self):
        return PostSerializer if self.request.method == 'POST' else PostListSerializer

    def get_queryset(self):
        return self.get_post_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailAPI(PostQuerySet, RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return self.get_post_queryset(self.request)
