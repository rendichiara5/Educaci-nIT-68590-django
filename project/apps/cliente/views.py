from django.shortcuts import render

from . import models


def index(request):
    clientes = models.Cliente.objects.all()
    context = {"clientes": clientes}
    return render(request, "cliente/index.html", context)
