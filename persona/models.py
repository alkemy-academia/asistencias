from django.db import models


class Persona(models.Model):
    FEMENINO = 'femenino'
    MASCULINO = 'masculino'
    OTRO = 'otro'

    GENERO_OPCIONES = (
        (FEMENINO, 'Femenino'),
        (MASCULINO, 'Masculino'),
        (OTRO, 'Otro')
    )

    dni = models.CharField(max_length=8, unique=True)
    nombre_completo = models.CharField(max_length=200)
    domicilio = models.CharField(max_length=250, blank=True)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10, choices=GENERO_OPCIONES)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nombre_completo',)

    def __str__(self):
        return f'{self.nombre_completo} - dni: {self.dni}'


class EstadoSalud(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    es_discapacitado = models.BooleanField(default=False)
    posee_desnutricion = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f'Persona: {self.persona} - Discapacitado: {self.es_discapacitado}'
