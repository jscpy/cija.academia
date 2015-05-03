from django.conf.urls import patterns, include, url
from django.contrib import admin
from academia.views import HomeView, CapituloListView, RecursoListView, PostListView
from academia import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^markdown/', include("django_markdown.urls")),
    url(r'^$', HomeView.as_view() ),
    url(r'^capitulos/', CapituloListView.as_view() ),
    url(r'^material/', RecursoListView.as_view() ),
    url(r'^blog/$', PostListView.as_view() ),
    url(r'^blog/post/(?P<pk>\d+)/$', views.Post_detail, name='post_detalles',),
    url(r'^blog/add/(?P<pk>\d+)/$', views.Comentario_create, name='comentario_crear'),
    url(r'^admin/', include(admin.site.urls)),
)
