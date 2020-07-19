from django.shortcuts import render
from blogs.models import Blog
# Create your views here.

def home(request):
    latest_blogs = Blog.objects.all()[:4]
    return render(request,'myblogs/index.html',{'blogs':latest_blogs})