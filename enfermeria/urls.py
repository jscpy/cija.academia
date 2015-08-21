from django.conf.urls import patterns, include, url
from enfermeria.views import HomeView, MenuView
from enfermeria import views

urlpatterns = [
    url(r'^$', HomeView.as_view() ),
    url(r'^menu/', views.Menu_index, name='menu' ),
]
