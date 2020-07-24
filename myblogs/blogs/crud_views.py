
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import  CreateView,DeleteView,UpdateView
from .forms import BlogModelForm
from django.http import HttpResponseRedirect
from .models import Author,Blog
from django.shortcuts import get_object_or_404

class Create(CreateView):
    form_class = BlogModelForm
    template_name = 'blogs/create.html'
    success_url = '/blogs/myblogs'    
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Create, self).dispatch(*args, **kwargs)
    
    def form_valid(self,form):
        obj = form.save(commit=False)
        author = get_object_or_404(Author , pk=self.request.user.id)
        obj.author_id = author
        obj.save()        
        return super().form_valid(form)

class Update(UpdateView):
    form_class = BlogModelForm
    success_url = '/blogs/myblogs'
    pk_url_kwarg = 'blog_id'
    model = Blog
    template_name = 'blogs/update.html'
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        blog = get_object_or_404(Blog, pk=26)
        print('This is user id' , blog.author_id.user.id)
        if blog.author_id.user.id == self.request.user.id:
              return super(Update, self).dispatch(*args, **kwargs)
        
        
class Delete(DeleteView):
    success_url = reverse_lazy('my_blogs')
    pk_url_kwarg = 'blog_id'
    model = Blog
    template_name = 'blogs/delete.html'
    
    