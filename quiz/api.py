
from .models import Quiz ,Answer ,Question
from .serializers import QuestionSerializer , AnswerSerializer , QuizSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework import filters


class QuizListAPI(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class AnswerListAPI(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer    


class QuestionListAPI(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer       
