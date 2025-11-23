from django.shortcuts import render, get_object_or_404, redirect
from .models import Proyecto, Voto

def estadisticas(request):
    proyectos = Proyecto.objects.all()
    datos = []

    for proyecto in proyectos:
        total = proyecto.votos.count()
        c1 = proyecto.votos.filter(opcion=1).count()
        c2 = proyecto.votos.filter(opcion=2).count()
        c3 = proyecto.votos.filter(opcion=3).count()
        c4 = proyecto.votos.filter(opcion=4).count()

        datos.append({
            "proyecto": proyecto,
            "total": total,
            "c1": c1,
            "c2": c2,
            "c3": c3,
            "c4": c4,
        })

    return render(request, "encuesta/estadisticas.html", {
        "datos": datos,
    })

def inicio(request):
    proyecto = Proyecto.objects.first()
    if proyecto:
        return redirect('votar', proyecto_id=proyecto.id)
    return render(request, 'encuesta/sin_proyectos.html')
def votar(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    # 1. Revisar si ya votó este proyecto (por cookie)
    cookie_name = f"voto_proyecto_{proyecto_id}"
    if request.COOKIES.get(cookie_name):
        return render(request, "encuesta/ya_voto.html", {"proyecto": proyecto})

    # 2. Si envió el formulario (POST)
    if request.method == 'POST':
        opcion = int(request.POST.get('opcion', 0))
        if opcion in [1, 2, 3, 4]:
            Voto.objects.create(proyecto=proyecto, opcion=opcion)
            
            # 3. Crear la respuesta y agregar la cookie
            response = render(request, 'encuesta/gracias.html', {"proyecto": proyecto})
            response.set_cookie(cookie_name, "true", max_age=60*60*24*365)  # dura 1 año
            return response

    return render(request, 'encuesta/votar.html', {"proyecto": proyecto})



def resultados(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    total = proyecto.votos.count()
    conteos = {
        1: proyecto.votos.filter(opcion=1).count(),
        2: proyecto.votos.filter(opcion=2).count(),
        3: proyecto.votos.filter(opcion=3).count(),
        4: proyecto.votos.filter(opcion=4).count(),
    }

    return render(request, 'encuesta/resultados.html', {
        'proyecto': proyecto,
        'total': total,
        'conteos': conteos,
    })


