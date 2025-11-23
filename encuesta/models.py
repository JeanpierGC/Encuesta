from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Voto(models.Model):
    OPCIONES = (
        (1, "Muy feliz"),
        (2, "Feliz"),
        (3, "Neutral"),
        (4, "Triste"),
    )

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='votos')
    opcion = models.PositiveSmallIntegerField(choices=OPCIONES)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.proyecto} - {self.get_opcion_display()}"
