from django.db import models
from django.core.urlresolvers import reverse
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

    def  get_absolute_url(self):
        return reverse('post_detalles', kwargs = {'pk':self.id})

    class Meta:
        ordering = ["-id"]

class Comentario(models.Model):
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    post = models.ForeignKey(Post)
    fecha = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.usuario

    class Meta:
        ordering = ["-id"]


