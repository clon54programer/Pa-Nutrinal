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
        
        return ReponseJson(200,StatusResponse.VALID,f"Bienvenido: {type_user}")
    elif type_user == "client":
        
        return ReponseJson(200,StatusResponse.VALID,f"Bienvenido: {type_user}")
    elif type_user == "seller":
        
        return ReponseJson(200,StatusResponse.VALID,f"Bienvenido: {type_user}")
    #else:
    #    raise Http404("El tipo de usuario es invalido")


    return ReponseJson(404,StatusResponse.INVALID,f"Tipo de usuario invalido")

def create_seller_login(request):
    """
    Esta funcion crea una entidad seller y luego la vincula
    con una entidad seller login.

    Esta funcion recibe los siguiente datos:
        - name: str
        - id: str
        - username: str
        - password: str
    NOTE: data_joined, debe ser asignado al momento de recibir la 
        solicitud.

    """
