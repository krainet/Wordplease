# -*- coding: utf-8 -*-
from blogs.forms import PostCreateForm
from blogs.models import Post, PUBLISHED, Blog, ACTIVE
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView
from django.core.urlresolvers import reverse
from django.db.models import Q


class HomeView(View):
    def get(self, req):
        posts = Post.objects.filter(status=PUBLISHED).order_by('-created_at')
        context = {
            'post_list': posts
        }
        return render(req, 'blogs/home.html', context)


class BlogListView(View):
    def get(self, req):
        blogs = Blog.objects.filter(status=ACTIVE).order_by('-created_at')

        context = {
            'blog_list': blogs
        }
        return render(req, 'blogs/blogs_list.html', context)

class BlogUserView(View):
    def get(self, req, username):
        blogs = Blog.objects.filter(owner__username=username)
        # posts = Post.objects.all()

        context = {
            'blog_list': blogs
        }
        return render(req, 'blogs/blogs_list.html', context)


class PostsDetailView(View):
    def get(self, req, username, pk):
        posts = Post.objects.filter(pk=pk)

        context = {
            'post_list': posts
        }
        return render(req, 'blogs/post_detail.html', context)


class PostsUserView(View):
    def get(self, req, username):
        posts = Post.objects.filter(owner__username=username)
        # posts = Post.objects.all()

        context = {
            'post_list': posts
        }
        return render(req, 'blogs/home.html', context)


class PostCreateView(View):
    @method_decorator(login_required())
    def get(self, req):
        """
        Muestra un form para crear una foto y la crea si la peticion es POST
        :param req: HttpRequest
        :return: HttpResponse
        """
        error_messages = []
        form = PostCreateForm()

        context = {
            'form': form
        }
        return render(req, 'blogs/new_post.html', context)

    @method_decorator(login_required())
    def post(self, req):
        """
        Muestra un form para crear una foto y la crea si la peticion es POST
        :param req: HttpRequest
        :return: HttpResponse
        """
        error_messages = []
        success_message = ''

        # Creamos owner y se lo pasamos al form con un objeto pre-establecido
        post_with_owner = Post()
        post_with_owner.owner = req.user

        form = PostCreateForm(req.POST, instance=post_with_owner)
        if form.is_valid():
            new_post = form.save()
            form = PostCreateForm()
            success_message = u'Post guardado con éxito! '
            success_message += u'<a href="{0}">'.format(reverse('post_detail', args=[req.user.username, new_post.pk]))
            success_message += u'(ver post)</a>'
        else:
            error_messages.append(u'Formulario incompleto.')

        context = {
            'form': form,
            'success_message': success_message
        }
        return render(req, 'blogs/new_post.html', context)


# query sets
class PostQuerySet(object):
    def get_post_queryset(self, req):
        if not req.user.is_authenticated():
            posts = Post.objects.filter(state=PUBLISHED).order_by('-created_at')
        elif req.user.is_superuser:  # es super admin
            posts = Post.objects.all()
        else:
            posts = Post.objects.filter(Q(owner=req.user) | Q(state=PUBLISHED))

        return posts


class BlogQuerySet(object):
    def get_blog_queryset(self, req):
        if not req.user.is_authenticated():
            blogs = Blog.objects.filter(state=ACTIVE).order_by('-created_at')
        elif req.user.is_superuser:  # es super admin
            blogs = Blog.objects.all()
        else:
            blogs = Blog.objects.filter(Q(owner=req.user) | Q(state=ACTIVE))

        return blogs


def prueba(req):
    context = dict(myvar='Hola', myvar2='Mundo')
    return render(req, 'blogs/testurl.html', context)
