from django.db import models
from django.utils import timezone


# Create your models here.

class Category(models.Model):

    categoryName =models.CharField(max_length=50)
    catImage = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.categoryName

class Cours(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(default = '')
    crated = models.DateTimeField(default = timezone.now)
    hours = models.IntegerField(default = None)
    niveau = models.CharField(max_length=50)
    image = models.ImageField(upload_to='cours')
    color = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name = 'categorys', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CoursImage(models.Model):
    CImage = models.ForeignKey(Cours,related_name = 'images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cours/')

    def __str__(self):
        return str(self.CImage)






