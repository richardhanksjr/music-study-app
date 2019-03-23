from django.views.generic import TemplateView
from django.urls import path
from .views import Index


urlpatterns = [path("", Index.as_view(), name='home-page')]

