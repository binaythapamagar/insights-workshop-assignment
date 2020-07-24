from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login,logout
from django.urls import reverse
from blogs.models import Author
# Create your views here.

def dashboard(request):
    return render(request,'users/dashboard.html')

def registration(request):
    if request.method == 'GET':
        if request.user:
            logout(request)
        return render(request,'users/register.html',{'form':CustomUserCreationForm})
    
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            author = Author.objects.create(user= user,name=user.username)
            author.save()
            login(request,user)
            return redirect('users_dashboard')
        else:
            return redirect('users_dashboard')