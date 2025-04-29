from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .JsonReponse import StatusResponse,ReponseJson

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
        return ReponseJson(200,StatusResponse.VALID,f"Bienvenido: {type_user}")
    elif type_user == "client":
        #return HttpResponse(f"Bienvenido: {type_user}")
        return ReponseJson(200,StatusResponse.VALID,f"Bienvenido: {type_user}")
    elif type_user == "seller":
        #return HttpResponse(f"Bienvenido: {type_user}")
        return ReponseJson(200,StatusResponse.VALID,f"Bienvenido: {type_user}")
    #else:
    #    raise Http404("El tipo de usuario es invalido")


    return ReponseJson(404,StatusResponse.INVALID,f"Tipo de usuario invalido")