from django.contrib import admin
from .models import Proyecto, Voto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    # Agregamos 'lider' a las columnas visibles
    list_display = ('nombre', 'lider', 'curso') 
    
    # Permitimos buscar por el nombre del líder
    search_fields = ('nombre', 'asesor', 'lider', 'integrantes')
    
    # Organizamos el formulario de edición
    fields = (
        'nombre', 
        ('curso', 'asesor'), 
        'lider',       # Aquí va el líder solo
        'integrantes'  # Y aquí el resto del equipo
    )

@admin.register(Voto)
class VotoAdmin(admin.ModelAdmin):
    list_display = ('proyecto', 'opcion', 'creado_en')
    list_filter = ('proyecto', 'opcion')