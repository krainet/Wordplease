# -*- coding: utf-8 -*-
from blogs.serializers import BlogSerializer, BlogListSerializer
from blogs.views import BlogQuerySet
from rest_framework.viewsets import ModelViewSet

__author__ = 'hadock'
from blogs.models import Blog
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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



#
#
# class BlogListAPI(BlogQuerySet, ListCreateAPIView):
#     queryset = Blog.objects.all()
#
#     permission_classes = (IsAuthenticatedOrReadOnly,)
#
#     #  Al sobreescribir este método podemos usar un serializador u
#     #  otro en funcion del metodo de la vista generica ListCreateApiView
#
#     def get_serializer_class(self):
#         return BlogSerializer if self.request.method == 'POST' else BlogListSerializer
#
#     def get_queryset(self):
#         return self.get_blog_queryset(self.request)
#
#     def perform_create(self, serializer):
#         serializer.save(blog_url='http://hola.com')
#
# class BlogDetailAPI(BlogQuerySet, RetrieveUpdateDestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#     lookup_fields = ('username',)
#
#     def get_queryset(self):
#         return self.get_blog_queryset(self.request)
