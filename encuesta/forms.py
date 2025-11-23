from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        # Aquí definimos qué puede editar el estudiante
        fields = ['nombre', 'curso', 'asesor', 'lider', 'integrantes']
        
        # Le ponemos estilos CSS para que se vea bonito en el celular
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nombre del Proyecto'}),
            'curso': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Inteligencia Artificial'}),
            'asesor': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Ej. Ing. Juan Pérez'}),
            'lider': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Nombre del Líder'}),
            'integrantes': forms.Textarea(attrs={'class': 'form-input', 'rows': 4, 'placeholder': 'Lista de integrantes...'}),
        }