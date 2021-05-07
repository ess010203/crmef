
from django.urls import path
from . import api

app_name = 'cours'

urlpatterns = [
    #path('api/list', api.cours_list,name ='cours_list'),
    #path("<int:id>",views.product_detail,name='product_detail'),
    path('api/list', api.CoursList.as_view()),
    path('api/list/<int:pk>', api.Cours_pk.as_view()),
    path('api/category', api.CategoryCours.as_view()),
    path('api/image/list', api.CoursList.as_view()),

]