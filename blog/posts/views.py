from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    if request.user.is_authenticated():
        queryset = Post.objects.all()
        context = {
            "title": "Authenticated user List",
            "object_list": queryset
        }
    else:
        context = {
            "title": "List"
        }
    return render(request, "index.html", context)


def post_update(request):
    context = {
        "title": "Update"
    }
    return render(request, "index.html", context)


def post_delete(request):
    context = {
        "title": "Delete"
    }
    return render(request, "index.html", context)

