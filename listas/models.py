from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Congreso(models.Model):
    nombre = models.CharField('nombre de la conferencia', max_length=200)
    fecha = models.DateTimeField('fecha y hora')
    lugar = models.CharField(max_length=200)
    conferencista = models.CharField('nombre del conferencista', max_length=200)
    asistentes = models.ManyToManyField(Persona)
    def __str__(self):
        return self.nombre
    def get_asistentes_values(self):

        ret = ''

        print(self.asistentes.all())

        for asistente in self.asistentes.all():
            ret = ret + asistente.nombre + ','
        return ret[:-1]