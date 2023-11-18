from django.http import HttpResponse


def saludo(request) -> HttpResponse:
    return HttpResponse("¡Hola!!!")

# Crear una función que solicite mi nombre
# y la muestre en pantalla al ingresar a una url
# diferente a 'saludo'