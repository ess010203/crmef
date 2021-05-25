from django.contrib import admin

# Register your models here.
from .models import Cours , CoursImage , Category ,coursdef
admin.site.register(Cours)
admin.site.register(CoursImage)
admin.site.register(Category)
admin.site.register(coursdef)
