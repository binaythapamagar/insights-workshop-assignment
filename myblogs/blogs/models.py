from django.db import models 

# Create your models here.
class DateInformation(models.Model):
    created_at = models.DateTimeField('Published date')
    updated_at = models.DateTimeField('Last updated')

class Author(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    
class Blog(DateInformation):
    title= models.CharField(max_length=300)
    body = models.TextField()
    author_id = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    