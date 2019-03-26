from django.urls import path
from .views import GetRandomQuestion, GetAnswerToQuestion, HelpSteps


urlpatterns = [path('question', GetRandomQuestion.as_view(), name='random-question'),
               path('answer', GetAnswerToQuestion.as_view(), name='answer'),
               path('help', HelpSteps.as_view(), name='help-steps')]
