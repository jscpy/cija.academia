from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView

from academia.models import Capitulo, Recurso, Post

class HomeView(TemplateView):
	template_name = "index.html"

class CapituloListView(ListView):
	model = Capitulo
	template_name = "capitulo_list.html"

class RecursoListView(ListView):
	model = Recurso
	template_name = "recurso_list.html"

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"