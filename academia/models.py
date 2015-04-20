from django.db import models

class Capitulo(models.Model):
    titulo = models.CharField(max_length=100)
    objetivo = models.TextField()

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
    cuerpo = models.TextField()

    def __unicode__(self):
        return self.encabezado


