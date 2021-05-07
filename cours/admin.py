from django.contrib import admin

# Register your models here.
from .models import Cours , CoursImage , Category

admin.site.register(Cours)
admin.site.register(CoursImage)
admin.site.register(Category)
