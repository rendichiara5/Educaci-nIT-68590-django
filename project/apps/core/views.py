from django.shortcuts import render


def index(request):
    return render(request, "core/index.html")


def prueba(request):
    context = {
        "nombre": "Ferretería",
        "notas": [2, 3, 5, 7, 10, 10],
    }
    return render(request, "core/prueba.html", context)
