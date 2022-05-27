from django.shortcuts import render
from .models import Blog

# Create your views here.


def blogs_home(request):

    blogs = Blog.objects.all()

    return render(request, "blog/blogs_home.html", {"blogs": blogs})
