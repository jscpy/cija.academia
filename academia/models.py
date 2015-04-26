from django.db import models
from django_markdown.models import MarkdownField

class Capitulo(models.Model):
    titulo = models.CharField(max_length=100)
    objetivo = MarkdownField()

    def __unicode__(self):
    	return self.titulo

class Recurso(models.Model):
	capitulo = models.ForeignKey(Capitulo)
	descripcion = models.CharField(max_length=100)
	url = models.CharField(max_length=100)
	fecha = models.DateField(auto_now=True)

	def __unicode__(self):
		return self.descripcion

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):
        return self.nombre

class Post(models.Model):
    encabezado = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario)
    fecha = models.DateField(auto_now=True)
    cuerpo = MarkdownField()

    def __unicode__(self):
        return self.encabezado

    class Meta:
        ordering = ["-fecha"]


