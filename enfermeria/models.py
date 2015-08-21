from django.db import models

class Medicamento(models.Model):
    concepto = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=50)
    unidad_medida = models.CharField(max_length=50)
    lote = models.CharField(max_length=15, unique=True)
    cantidad = models.IntegerField()
    fecha_caducidad = models.DateField()
    fecha_ingreso = models.DateField(auto_now=True)

    def __unicode__(self):
    	return self.concepto

    class Meta:
    	ordering = ["-fecha_caducidad"]
