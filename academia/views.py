from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.core.context_processors import csrf

from django.views.generic import TemplateView, View, ListView, DetailView

from academia.models import Capitulo, Recurso, Post, Comentario
from academia.forms import ComentarioForm

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
    paginate_by = 2
    template_name = "post_list.html"

def Post_detail(request, pk):
	post = Post.objects.get(pk=int(pk))
	comentarios = Comentario.objects.filter(post=post)
	form = ComentarioForm()
	dict_post = dict(post = post, comentarios = comentarios, form = form)
	dict_post.update(csrf(request))
	
	return render_to_response("post.html",dict_post)

def Comentario_create(request, pk):
	p = request.POST
	comentario = Comentario(post=Post.objects.get(pk=pk))
	cf = ComentarioForm(p, instance=comentario)
	comentario = cf.save(commit=False)
	comentario.save()
	
	return HttpResponseRedirect(reverse('post_detalles',args=[pk]))