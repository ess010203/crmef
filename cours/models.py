from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.utils import timezone
from colorfield.fields import ColorField


# Create your models here.

class Category(models.Model):

    categoryName =models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True,null=True, related_name='categories',on_delete=models.CASCADE)
    catImage = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.categoryName





class Cours(models.Model):
    pre = '1er année collège'
    sec = '2ème année collège'
    tre = '3ème année collège'
    prel = 'tronc commun'
    choix = [
        (pre, '1er année collège'),
        (sec, '2ème année collège'),
        (tre, '3ème année collège'),
        (prel, 'tronc commun'),
        
    ]

    


    title = models.CharField(max_length=50)
    description = models.TextField(default = '')
    crated = models.DateTimeField(default = timezone.now)
    hours = models.IntegerField(default = None)
    niveau = models.CharField(max_length=50,choices=choix,default=pre)
    image = models.ImageField(upload_to='cours')
    color = ColorField(format='hexa')
    category = models.ForeignKey(Category,related_name = 'categorys', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class CoursImage(models.Model):
    CImage = models.ForeignKey(Cours,related_name = 'images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='cours/cours/')

    def __str__(self):
        return str(self.CImage)



class coursdef(models.Model):
    Cdef = models.ForeignKey(Cours,related_name = 'definitions',on_delete=models.CASCADE)
    definition = models.TextField()

    def __str__(self):
        return str(self.Cdef)



