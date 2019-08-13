from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'application/index.html'
