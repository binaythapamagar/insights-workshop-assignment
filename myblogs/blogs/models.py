from django.db import models 
from django.contrib.auth.models import User
        
# Create your models here.
class DateInformation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
class Blog(DateInformation):
    title= models.CharField(max_length=300)
    body = models.TextField()
    author_id = models.ForeignKey(Author,on_delete=models.CASCADE)    
    def __str__(self):
        return self.title
    