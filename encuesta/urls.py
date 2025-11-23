from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # para la página principal "/"
    path('votar/<int:proyecto_id>/', views.votar, name='votar'),
    path('resultados/<int:proyecto_id>/', views.resultados, name='resultados'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
]
