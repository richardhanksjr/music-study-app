from django.urls import path
from .views import GetRandomQuestion


urlpatterns = [path('question', GetRandomQuestion.as_view(), name='random-question')]
