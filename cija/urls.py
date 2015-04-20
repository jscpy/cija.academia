from django.conf.urls import patterns, include, url
from django.contrib import admin
from academia.views import HomeView, CapituloListView, RecursoListView, PostListView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view() ),
    url(r'^capitulos/', CapituloListView.as_view() ),
    url(r'^material/', RecursoListView.as_view() ),
    url(r'^blog/', PostListView.as_view() ),
    url(r'^admin/', include(admin.site.urls)),
)
