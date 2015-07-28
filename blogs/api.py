# -*- coding: utf-8 -*-
from blogs.serializers import PostListSerializer, PostSerializer, BlogSerializer, BlogListSerializer
from blogs.views import PostQuerySet, BlogQuerySet

__author__ = 'hadock'
from blogs.models import Blog
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BlogListAPI(BlogQuerySet, ListCreateAPIView):
    queryset = Blog.objects.all()

    permission_classes = (IsAuthenticatedOrReadOnly,)

    #  Al sobreescribir este método podemos usar un serializador u
    #  otro en funcion del metodo de la vista generica ListCreateApiView

    def get_serializer_class(self):
        return BlogSerializer if self.request.method == 'POST' else BlogListSerializer

    def get_queryset(self):
        return self.get_blog_queryset(self.request)

    def perform_create(self, serializer):
        serializer.save(blog_url='http://hola.com')

class BlogDetailAPI(BlogQuerySet, RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_fields = ('username',)

    def get_queryset(self):
        return self.get_blog_queryset(self.request)
