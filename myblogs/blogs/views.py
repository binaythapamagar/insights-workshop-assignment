from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
# Create your views here.

def all_blogs(request):
    blogs = Blog.objects.all()
    return render(request,'blogs/index.html',{'blogs':blogs})


def blog_detail(request,blog_id):
    blog = get_object_or_404(Blog.objects.filter(pk=blog_id).select_related('author_id'))
    return render(request,'blogs/blog_detail.html',{'blog':blog})