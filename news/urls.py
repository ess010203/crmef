from django.urls import path
from news.api import NewsListAPI , FilesNewsListAPI , News_pk

app_name = 'news'

urlpatterns = [
  
    path('all', NewsListAPI.as_view()),
    path('filesNews', FilesNewsListAPI.as_view()),
    path('all/<int:pk>', News_pk.as_view()),
   

]