from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin, AdminMarkdownWidget
from django.db.models import TextField
from academia.models import Capitulo, Recurso, Usuario, Post

class PostAdmin(MarkdownModelAdmin):
	formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(Capitulo)
admin.site.register(Recurso)
admin.site.register(Usuario)
admin.site.register(Post, PostAdmin)