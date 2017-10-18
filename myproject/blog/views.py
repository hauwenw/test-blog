# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.views.generic import DetailView, ListView
from .models import Post, Comment
from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Post.objects.filter(posted_at__lte=datetime.now()).order_by('-posted_at')


class PostView(DetailView):
    model = Post
    template_name = 'blog/post.html'


@login_required()
def post_post(request):
    if request.method == 'POST':
        new_post = Post(title=request.POST[u'title'], content=request.POST[u'content'], author=request.user)
        new_post.save()
    return redirect('index')


@login_required()
def post_comment(request, pk):
    if request.method == 'POST':
        content = request.POST['content']
        post = Post.objects.get(id=pk)
        new_comment = Comment(content=content, post=post, author=request.user)
        new_comment.save()
    return redirect('post', pk=pk)


# def login(request):
#
#     if request.user.is_authenticated():
#         return redirect('index')
#
#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')
#
#     user = auth.authenticate(username=username, password=password)
#
#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return redirect('index')
#     else:
#         return render(request, 'login.html')
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect('index')
