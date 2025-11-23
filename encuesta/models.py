from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=100, null=True, blank=True, verbose_name="Curso / Ciclo")
    asesor = models.CharField(max_length=100, null=True, blank=True, verbose_name="Asesor / Docente")
    
    # --- NUEVO CAMPO PARA EL LÍDER ---
    lider = models.CharField(max_length=100, null=True, blank=True, verbose_name="Líder del Proyecto")
    
    # Mantenemos 'integrantes' por si quieres poner al resto del equipo aparte
    integrantes = models.TextField(null=True, blank=True, verbose_name="Resto de Integrantes", help_text="Escribe un nombre por línea")

    def __str__(self):
        return f"{self.nombre} ({self.curso})"

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