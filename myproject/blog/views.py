# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post, Comment
from datetime import datetime
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = Post.objects.filter(posted_at__lte=datetime.now()).order_by('-posted_at')


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'


def post_post(request):
    if request.method == 'POST':
        new_post = Post(title=request.POST[u'title'], content=request.POST[u'content'])
        new_post.save()
    return redirect('index')


def post_comment(request, pk):
    if request.method == 'POST':
        content = request.POST['content']
        post = Post.objects.get(id=pk)
        new_comment = Comment(content=content, post=post)
        new_comment.save()
    return redirect('post', pk=pk)
