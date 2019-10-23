from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    context = {
        "post_list": posts
    }
    return render(request, "post_list.html", context)

def post_detail(request, id):
    post = Post.objects.get(id = id)
    context = {
        "post": post
    }
    return render(request, "post_detail.html", context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/posts")
    context = {
        "form": form,
        "type": "create"
        
    }
    return render(request, "post_create.html", context)

def post_update(request, id):
    post = Post.objects.get(id = id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/posts/" + str(id))
    context = {
        "form": form,
        "type": "update"
    }
    return render(request, "post_create.html", context)

def post_delete(request, id):
    post = Post.objects.get(id = id)
    post.delete()
    return HttpResponseRedirect("/posts")