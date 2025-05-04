from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from .JsonReponse import StatusResponse, ReponseJson, ReponseJsonError

from django.views.decorators.csrf import csrf_exempt  # para evitar errores

from . import ValidRequest

# Create your views here.


def index(request):
    return HttpResponse("Bienvenido a nutrinal")


def login(request, type_user: str):

    # Estructura de la respuesta en json
    # Un campo llamado, status,
    # que puede te valor valid y invalid.
    # Despues tiene un campo llamado,
    # data, que se almacenara la informacion

    if type_user == "admin":

        return ReponseJson(200, StatusResponse.VALID, {"message": f"Bienvenido: {type_user}"})
    elif type_user == "client":

        return ReponseJson(200, StatusResponse.VALID, {"message": f"Bienvenido: {type_user}"})
    elif type_user == "seller":

        return ReponseJson(200, StatusResponse.VALID, {"message": f"Bienvenido: {type_user}"})

    return ReponseJsonError("Tipo de usuario invalido", "La ruta no contiene un tipo de usuario iqual a seller, admin o client", 404)


@csrf_exempt
def create_seller_login(request: HttpRequest):
    """
    Recibi mediante de un metodo post del panel de administracion de
    un admin, la informacion de una entidad de tipo seller y
    seller_login.

    Esta funcion recibe los siguiente datos:
        - name: str
        - id: str
        - username: str
        - password: str
    NOTE: data_joined, debe ser asignado al momento de recibir la
        solicitud.
    """

    if request.method == "GET":
        return ReponseJsonError("Falta de permiso", "No tienen permiso para realizar la accion.", 401)

    if request.method == "POST":
        name_seller = request.POST.get("name")
        id_seller = request.POST.get("id")
        username_seller = request.POST.get("username")
        password_seller = request.POST.get("password")

        data = [name_seller, id_seller, username_seller, password_seller]

        for iter in data:
            if ValidRequest.is_valid(iter) != True:
                message = f"Falta el parametro: {type(iter).__name__}"
                return ReponseJsonError("Faltan parametros a la solicitud", details=message)

    content = {
        "message": "El usuario ha sido creado exitosamente"
    }

    return ReponseJson(200, StatusResponse.VALID, json_body=content)
