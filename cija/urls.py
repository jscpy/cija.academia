from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^markdown/', include("django_markdown.urls")),
	url(r'^academia/', include("academia.urls")),
	url(r'^enfermeria/', include("enfermeria.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
