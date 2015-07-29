# -*- coding: utf-8 -*-
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet
from users.permissions import UserPermission

__author__ = 'hadock'
from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class UserViewSet(GenericViewSet):
    # serializer_class = UserSerializer
    permission_classes = (UserPermission,)
    pagination_class = PageNumberPagination

    def list(self, req):
        users = User.objects.all()
        self.paginate_queryset(users)  # pagino el resultado
        serializer = UserSerializer(users, many=True)
        return self.get_paginated_response(serializer.data)  # devuelvo una respuesta paginada

    def create(self, req):
        serializer = UserSerializer(data=req.data)
        if serializer.is_valid():
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        # aqui y siempre que declaremos los metodos nosotros , nos toca comprobar a mano
        # si el usuario tiene permiso
        self.check_object_permissions(req, user)  # checar permisos
        return Response(UserSerializer(user).data)

    def update(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(req, user)  # permisos a mano
        serializer = UserSerializer(instance=user, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, req, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(req, user)  # permisos a manija
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        return UserSerializer