from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from .JsonReponse import StatusResponse, ReponseJson, ReponseJsonError

from django.views.decorators.csrf import csrf_exempt  # para evitar errores
import json
from .models import Seller, SellerLogin, Client, ClientLogin, Order, Product, Production, Admin
from django.db.models import Model

from . import ValidRequest

# Create your views here.


def create_default_data(request: HttpRequest):
    """
    Crea datos por default para realizar pruebas.
    """

    # Crear un administrador
    admin = Admin.objects.create(
        username="admin_nutrinal", password="adminpass123")

    # Crear dos vendedores
    seller1 = Seller.objects.create(name="Juan Pérez", identifier="123456")
    seller2 = Seller.objects.create(name="Ana Gómez", identifier="654321")

    # Crear un cliente
    client = Client.objects.create(
        name="Carlos Rodríguez", email="carlos@example.com", phone_number="1234567890", identifier="CLT001")

    # Crear un producto
    product = Product.objects.create(name="Suplemento Nutricional", code="PROD001",
                                     price=49.99, description="Mejora la salud y el bienestar.")

    # Crear una producción para el producto
    production = Production.objects.create(product=product, cant_available=100)

    # Crear registros de acceso para el vendedor y el cliente
    seller_login1 = SellerLogin.objects.create(
        identifier=seller1, username="juan_vendedor", password="securepass")

    seller_login2 = SellerLogin.objects.create(
        identifier=seller2, username="ana_vendedora", password="securepass")
    client_login = ClientLogin.objects.create(
        identifier=client, username="carlos_cliente", password="clientpass")


def index(request):
    return HttpResponse("Bienvenido a nutrinal")


def login(request: HttpRequest, type_user: str):

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

            if "data" not in json_data:
                return ReponseJsonError("Falta un campo", "El campo data no esta incluido en json")

            data = json_data['data']

            for field in fields:
                if field not in data:
                    return ReponseJsonError("Falta un campo", f"El campo {field} no esta incluido en json")

            print("Json Recibido exitosamente")
            print("data: ", json_data['data'])

            name = data['name']
            id = data['id']

            if Seller.objects.filter(id=id).exists():
                return ReponseJsonError("Dato redundante", f'El id recibido ya existe en la base de datos')
            if Seller.objects.filter(name=name).exists():
                return ReponseJsonError("Dato redundante", f'El name recibido ya existe en la base de datos')

            # Insertando informacion en la base de datos

            seller = Seller.objects.create(name=name, identifier=id)

            user_name = data['username']
            password = data['password']

            SellerLogin.objects.create(
                identifier=seller, username=user_name, password=password)

        except json.JSONDecodeError:
            return ReponseJsonError("Error de formato", "El json recibido no sigue el estandar habitual", 400)

    content = {
        "message": "El vendedor ha sido creado exitosamente"
    }

    return ReponseJson(200, StatusResponse.VALID, json_body=content)
