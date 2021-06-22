from django.urls import path, re_path
from quiz.api import  QuizListAPI , AnswerListAPI ,QuestionListAPI


urlpatterns = [
	path("quizzes/", QuizListAPI.as_view()),
    path("answer/", AnswerListAPI.as_view()),
    path("question/", QuestionListAPI.as_view()),
	
]