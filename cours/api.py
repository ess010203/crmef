from .models import Cours,CoursImage,Category
from .serializers import CoursSerializer , ImageCoursSerializer , CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework import filters

"""
@api_view(['GET'])
def cours_list(request):
    cours_list = Cours.objects.all()
    data = CoursSerializer(cours_list,many = True).data
    print(Response({'data':data}))
    return Response({'data':data})
 """   


class CoursList(generics.ListCreateAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description','hours']

class Cours_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer

class CoursListImages(generics.ListCreateAPIView):
    queryset = CoursImage.objects.all()
    serializer_class = ImageCoursSerializer

class CategoryCours(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    

