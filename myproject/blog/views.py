# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views.generic import DetailView, ListView
from .models import Post, Comment
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.filter(posted_at__lte=timezone.now()).order_by('-posted_at')


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'


@login_required()
def post_post(request):
    if request.method == 'POST':
        new_post = Post(title=request.POST[u'title'], content=request.POST[u'content'], author=request.user)
        new_post.save()
        messages.success(request, 'Post Successfully!')
    return redirect('index')


@login_required()
def post_comment(request, pk):
    if request.method == 'POST':
        content = request.POST['content']
        post = Post.objects.get(id=pk)
        new_comment = Comment(content=content, post=post, author=request.user)
        new_comment.save()
        messages.success(request, 'Comment Successfully!')
    return redirect('post', pk=pk)
