from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .JsonReponse import ResponseJson,StatusResponse

# Create your views here.

def index(request):
    return HttpResponse("Bienvenido a nutrinal")


def login(request,type_user: str):

    

    # Estructura de la respuesta en json
    # Un campo llamado, status,
    # que puede te valor valid y invalid.
    # Despues tiene un campo llamado,
    # data, que se almacenara la informacion

    if type_user == "admin":
        #return HttpResponse(f"Bienvenido: {type_user}")
        return ResponseJson(StatusResponse.VALID,{"data": f"Bienvenido {type_user}"}).get_reponse()
    elif type_user == "client":
        #return HttpResponse(f"Bienvenido: {type_user}")
        return ResponseJson(StatusResponse.VALID,{"data": f"Bienvenido {type_user}"}).get_reponse()
    elif type_user == "seller":
        #return HttpResponse(f"Bienvenido: {type_user}")
        return ResponseJson(StatusResponse.VALID,{"data": f"Bienvenido {type_user}"}).get_reponse()
    #else:
    #    raise Http404("El tipo de usuario es invalido")


    return ResponseJson(StatusResponse.INVALID,{"data": "No existe ese usuario"}).get_reponse()