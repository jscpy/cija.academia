from django.db import models

# Create your models here.

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
