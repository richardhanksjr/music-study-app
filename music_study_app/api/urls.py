from django.urls import path
from .views import GetRandomQuestion, GetAnswerToQuestion


urlpatterns = [path('question', GetRandomQuestion.as_view(), name='random-question'),
               path('answer', GetAnswerToQuestion.as_view(), name='answer'),]
