from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView

from academia.models import Capitulo, Recurso

class HomeView(TemplateView):
	template_name = "index.html"

class CapituloListView(ListView):
    model = Capitulo
    template_name = "capitulo_list.html"

class RecursoListView(ListView):
    model = Recurso
    template_name = "recurso_list.html"

class BlogView(TemplateView):
    template_name = "blog.html"