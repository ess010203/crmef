from .models import News , FileNews
from .serializers import NewsSerializers , FileNewsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework import filters


class NewsListAPI(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


    
class FilesNewsListAPI(generics.ListCreateAPIView):
    queryset = FileNews.objects.all()
    serializer_class = FileNewsSerializer

class News_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers    