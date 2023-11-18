from django.http import HttpResponse


def saludo(request) -> HttpResponse:
    return HttpResponse("¡Hola!!!")

# Crear una función que solicite mi nombre
# y la muestre en pantalla al ingresar a una url
# diferente a 'saludo'

def saludo2(request):
    nombre = input("Dime tu nombre: ")
    return HttpResponse(f"<h1> Hola {nombre} </h1")

def nombre(request, nombre):
    return HttpResponse(nombre)

# Crear una función que reciba 2 parámetros en la url: nombre y apellido
# Devolver el apellido en mayúsculas y el nombre en minúsculas.

def nombre2(request, nombre: str, apellido: str):
    nombre = nombre.lower()
    apellido = apellido.upper()
    return HttpResponse(f"{apellido}, {nombre}")

def fecha_hora(request):
    from datetime import datetime
    ahora = datetime.now().strftime(r"%d/%m/%Y %H:%M:%S.%f")
    return HttpResponse(f"Fecha y hora: {ahora}")

# Crear una vista que muestre "Has tirado el dado: <numero>"
# Si el número es 6, mostrar una felicitación
# Si no, mostrar que vuelva a intentar
# import random
# randint(1, 6)

def tirar_dado(request):
    import random
    numero_dado = random.randint(1, 6)
    if numero_dado == 6:
        return HttpResponse(f"<h1> Has tirado el dado: 🎲{numero_dado} ✨ Suerte! </h1>")
    else:
        return HttpResponse(f"<h1> Has tirado el dado: 🎲{numero_dado} </h1> <br> Sigue intentando...")
