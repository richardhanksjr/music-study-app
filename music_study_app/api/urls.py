from django.urls import path
from .views import GetRandomQuestion


urlpatterns = [path('', GetRandomQuestion.as_view(), name='random-question')]
