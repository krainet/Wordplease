# -*- coding: utf-8 -*-
from posts.permissions import PostPermission
from rest_framework import status

__author__ = 'hadock'
from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostQuerySet
from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PostViewSet(PostQuerySet, ModelViewSet):
    queryset = Post.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,PostPermission)
    permission_classes = (PostPermission,)

    def get_queryset(self):
        return self.get_post_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, req, pk):
        user = get_object_or_404(Post, pk=pk)
        # aqui y siempre que declaremos los metodos nosotros , nos toca comprobar a mano
        # si el usuario tiene permiso
        self.check_object_permissions(req, user)  # checar permisos
        return Response(PostSerializer(user).data)

    def update(self, req, pk):
        user = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(req, user)  # permisos a mano
        serializer = PostSerializer(instance=user, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, req, pk):
        user = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(req, user)  # permisos a manija
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)