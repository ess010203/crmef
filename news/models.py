from django.db import models
from django.db.models.base import Model
from django.db.models.fields import NullBooleanField, TextField
from django.utils import timezone


# Create your models here.



class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    date =  models.DateTimeField(default = timezone.now)
    date_creation = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField( upload_to='news/images',blank = True)
    document = models.FileField(upload_to='news/files',null=True,blank = True)

    
    def __str__(self):
        return self.title



class FileNews(models.Model):

    news = models.ForeignKey(News,related_name = 'filesNews', on_delete=models.CASCADE)
    files = models.FileField(upload_to='news/files',null=True,blank = True)
    images = models.ImageField(upload_to='news/images',blank = True)

    def __str__(self):
        return str(self.news)

