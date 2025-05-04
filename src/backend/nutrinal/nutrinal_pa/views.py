from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from .JsonReponse import StatusResponse, ReponseJson, ReponseJsonError

from django.views.decorators.csrf import csrf_exempt  # para evitar errores
import json

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
        try:
            json_data = json.loads(request.body)
            fields = ['name', 'id', 'username', 'password']
            data = json_data['data']

            if "data" not in json_data:
                return ReponseJsonError("Falta un campo", "El campo data no esta incluido en json")

            for field in fields:
                if field not in data:
                    return ReponseJsonError("Falta un campo", f"El campo {field} no esta incluido en json")

            print("Json Recibido exitosamente")
            print("data: ", json_data['data'])

        except json.JSONDecodeError:
            return ReponseJsonError("Error de formato", "El json recibido no sigue el estandar habitual", 400)

    content = {
        "message": "El vendedor ha sido creado exitosamente"
    }

    return ReponseJson(200, StatusResponse.VALID, json_body=content)
