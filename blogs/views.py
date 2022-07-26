from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Blog

# Create your views here.


def blog_list(request):
    blogs = Blog.objects.all().order_by("date")
    data = {"blogs": blogs}
    return render(request, "articles/blog_list.html", data)


def blog_single(request, slug):
    blog = Blog.objects.get(slug=slug)
    if blog is not None:
        data = {"blog": blog}
        return render(request, "articles/blog_single.html", data)
    else:
        raise Http404("Post not found")
