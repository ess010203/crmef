from django.db import models
from django.db.models.base import Model
from django.db.models.fields import NullBooleanField, TextField

# Create your models here.



class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    image = models.ImageField( upload_to='news/images',blank = True)
    document = models.FileField(upload_to='news/files',null=True,blank = True)

    
    def __str__(self):
        return self.title



class FileNews(models.Model):

    news = models.ForeignKey("news.News", on_delete=models.CASCADE)
    files = models.FileField(upload_to='news/files',null=True,blank = True)
    images = models.ImageField(upload_to='news/images',blank = True)

    def __str__(self):
        return self.news

