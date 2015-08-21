from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView

from forms import MedicamentoForm

class HomeView(TemplateView):
    template_name = "enfermeria/index.html"

class MenuView(TemplateView):
    template_name = "enfermeria/menu.html"

def Menu_index(request):
	form = MedicamentoForm()
	dict_menu = dict(medicamento = form ) 
	return render_to_response("enfermeria/menu.html",dict_menu)

