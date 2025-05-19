from django.test import TestCase
import requests


class TestViewLogin(TestCase):

    def test_valid_reponse(self):

        routes_valid = [
            "http://127.0.0.1:8000/nutrinal_pa/login/client",
            "http://127.0.0.1:8000/nutrinal_pa/login/seller",
            "http://127.0.0.1:8000/nutrinal_pa/login/admin"
        ]

        message_valid = [
            "Bienvenido: client",
            "Bienvenido: seller",
            "Bienvenido: admin"
        ]

        for iter in routes_valid:
            r = requests.get(iter)
            content = r.json()

            print(f"Content: {content['data']['message']}")

            self.assertEqual(200, r.status_code,
                             "El codigo http de respuesta es diferente a 200")

    def test_invalid_response(self):

        route_invalid = [
            "http://127.0.0.1:8000/nutrinal_pa/login/body",
            "http://127.0.0.1:8000/nutrinal_pa/login/ed",
            "http://127.0.0.1:8000/nutrinal_pa/login/bee",
        ]

        for iter in route_invalid:
            r = requests.get(iter)
            content = r.json()

            print(f"Content: {content['data']}")

            self.assertEqual(404, r.status_code,
                             "El codigo http de repuesta es diferent a 404")


class TestCreateSeller(TestCase):

    def test_post_data(self):
        json = {"data": {
            "name": "juan",
            "id": "12345678",
            "username": "seller_1",
            "password": "12345678"
        }}

        url_post = "http://127.0.0.1:8000/nutrinal_pa/admin/create_seller_login"

        r = requests.post(
            url_post, json=json)

        print("status code: ", r.status_code)
        print("json: ", r.json())

        self.assertEqual(200, r.status_code, "El codigo http no es igual 200")

    def test_get_data(self):
        url_get = "http://127.0.0.1:8000/nutrinal_pa/admin/create_seller_login"

        r = requests.get(url_get)
        print(r.headers.get("Content-Type"))

        content = r.json()

        print("status code: ", r.status_code)
        print("json", content['data'])

    def test_post_valid_json(self):
        json = {
            "data": {
                "name": "Carlos",
                "id": "12345",
                "username": "carlos_user",
                "password": "securepass123"
            }
        }

        url_post = "http://127.0.0.1:8000/nutrinal_pa/admin/create_seller_login"

        r = requests.post(url_post, json=json)

        print("status code: ", r.status_code)
        print("data", r.json()['data'])

    def test_missing_field(self):
        missing_name = {
            "data": {
                "id": "12345",
                "username": "carlos_user",
                "password": "securepass123"
            }
        }

        missing_id = {
            "data": {
                "name": "Carlos",
                "username": "carlos_user",
                "password": "securepass123"
            }
        }

        missing_username = {
            "data": {
                "name": "Carlos",
                "id": "12345",
                "password": "securepass123"
            }
        }

        missing_password = {
            "data": {
                "name": "Carlos",
                "id": "12345",
                "username": "carlos_user"
            }
        }

        missing_data = {}

        url_post = "http://127.0.0.1:8000/nutrinal_pa/admin/create_seller_login"

        lista = [missing_id, missing_data, missing_name,
                 missing_username, missing_password]

        for json in lista:
            r = requests.post(
                url_post, json=json)
            content = r.json()

            print("status code: ", r.status_code)
            print("Error: ", content['data']['error'])
            print("Detalles", content['data']['details'])
            self.assertEqual(400, r.status_code,
                             "El codigo http no es igual a 400")


class ViewMakeProduct(TestCase):

    def test_post_data(self):
        content = {"data": {
            "name": "Producto Ejemplo",
            "code": "P12345",
            "price": 1000.50,
            "description": "Este es un producto de prueba"
        }}

        url_post = "http://127.0.0.1:8000/nutrinal_pa/admin/make_product"

        r = requests.post(url_post, json=content)
        data = r.json()['data']

        if r.status_code == 400:
            print("error: ", data['error'])
            print("detalles: ", data['details'])
            self.assertEqual(400, r.status_code,
                             "El codigo http es diferente a 400")
        elif r.status_code == 200:
            print("data: ", data)
            self.assertEqual(200, r.status_code,
                             "El codigo http es diferente a 200")

        print("")

    def test_missing_field(self):
        url_post = "http://127.0.0.1:8000/nutrinal_pa/admin/make_product"

        missing_code = {
            "data": {
                "name": "Producto Ejemplo",
                "price": 1000.50,
                "description": "Este es un producto de prueba"
            }
        }

        missing_price = {
            "data": {
                "name": "Producto Ejemplo",
                "code": "P12345",
                "description": "Este es un producto de prueba"
            }
        }

        missing_name = {"data": {
            "code": "P12345",
            "price": 1000.50,
            "description": "Este es un producto de prueba"
        }
        }

        missing_description = {
            "data": {
                "name": "Producto Ejemplo",
                "code": "P12345",
                "price": 1000.50
            }
        }

        missing_data = {}

        list_missing = [missing_name, missing_code,
                        missing_description, missing_price, missing_data]

        for field in list_missing:
            r = requests.post(url_post, json=field)
            content = r.json()

            print("status code: ", r.status_code)
            print("error: ", content['data']['error'])
            print("error: ", content['data']['details'])

            self.assertEqual(400, r.status_code,
                             "El codigo http es diferente a 400")


class TestViewsGetter(TestCase):

    def SetUp(self):
        self.url_seller = "http://127.0.0.1:8000/nutrinal_pa/admin/get_seller"
        self.url_seller_login = "http://127.0.0.1:8000/nutrinal_pa/admin/get_seller_login"
        self.url_client = "http://127.0.0.1:8000/nutrinal_pa/admin/get_client"
        self.url_product = "http://127.0.0.1:8000/nutrinal_pa/admin/get_product"
        self.url_production = "http://127.0.0.1:8000/nutrinal_pa/admin/get_production"

    def test_get_seller_empty_db(self):
        """Verifica que `get_seller` retorna 204 cuando no hay datos."""
        url_seller = "http://127.0.0.1:8000/nutrinal_pa/admin/get_seller"
        r = requests.get(url_seller)

        if r.status_code != 204:
            print(r.json())
        else:
            self.assertEqual(204, r.status_code,
                             "El codigo http es diferente a 204")

    def test_getter_wrong_method(self):
        """Verifica que  retorna 405 si el método no es GET."""

        url_seller = "http://127.0.0.1:8000/nutrinal_pa/admin/get_seller"
        url_seller_login = "http://127.0.0.1:8000/nutrinal_pa/admin/get_seller_login"
        url_client = "http://127.0.0.1:8000/nutrinal_pa/admin/get_client"
        url_product = "http://127.0.0.1:8000/nutrinal_pa/admin/get_product"
        url_production = "http://127.0.0.1:8000/nutrinal_pa/admin/get_production"

        list = [url_production, url_client,
                url_product, url_seller, url_seller_login]

        for url in list:
            r = requests.post(url, json={"data": "jaun"})

            self.assertEqual(405, r.status_code,
                             "El codigo http es diferente a 405")

    def test_get_seller_login_empty_db(self):
        """Verifica que `get_seller_login` retorna 204 cuando no hay datos."""
        url_seller_login = "http://127.0.0.1:8000/nutrinal_pa/admin/get_seller_login"
        r = requests.get(url_seller_login)

        if r.status_code != 204:
            print(r.json())
        else:
            self.assertEqual(204, r.status_code,
                             "El codigo http es diferente a 204")

    def test_get_client_empty_db(self):
        """Verifica que `get_client` retorna 204 cuando no hay datos."""
        url_client = "http://127.0.0.1:8000/nutrinal_pa/admin/get_client"
        r = requests.get(url_client)

        if r.status_code != 204:
            print(r.json())
        else:
            self.assertEqual(204, r.status_code,
                             "El codigo http es diferente a 204")

    def test_get_product_empty_db(self):
        """Verifica que `get_product` retorna 204 cuando no hay datos."""
        url_product = "http://127.0.0.1:8000/nutrinal_pa/admin/get_product"
        r = requests.get(url_product)

        if r.status_code != 204:
            print(r.json())
        else:
            self.assertEqual(204, r.status_code,
                             "El codigo  http es diferente a 204")

    def test_get_production_empty_db(self):
        """Verifica que `get_production` retorna 204 cuando no hay datos."""
        url_production = "http://127.0.0.1:8000/nutrinal_pa/admin/get_production"
        r = requests.get(url_production)

        if r.status_code != 204:
            print(r.json())
        else:
            self.assertEqual(204, r.status_code,
                             "El codigo  http es diferente a 204")


class TestViewUpdateProduct(TestCase):

    def test_wrong_method(self):
        code = "123"
        url = f"http://127.0.0.1:8000/nutrinal_pa/admin/update_production/{code}"

        json = {
            "code": code,
            "cant_available": 1000
        }

        r = requests.post(url, json=json)

        self.assertEqual(405, r.status_code,
                         "El codigo http es diferente a 405")

    def test_no_exist_product(self):
        code = "P1234"
        new_can_avaible = 20
        url = f"http://127.0.0.1:8000/nutrinal_pa/admin/update_production/{code}"

        json = {
            "code": code
        }

        r = requests.patch(url, json=json)

        print("json: ", r.json())

        self.assertEqual(404, r.status_code,
                         "El codigo http es diferente a 404")

    def test_missing_field_product(self):
        code = "P12345"
        new_can_avaible = 20
        url = f"http://127.0.0.1:8000/nutrinal_pa/admin/update_production/{code}"

        json = {
            "code": code
        }

        r = requests.patch(url, json=json)

        print("json: ", r.json())

        self.assertEqual(400, r.status_code,
                         "El codigo http es diferente a 400")

    def test_update_cant_avaible(self):

        code = "P12345"
        new_can_avaible = 20
        url = f"http://127.0.0.1:8000/nutrinal_pa/admin/update_production/{code}"

        json = {
            "cant_available": new_can_avaible
        }

        r = requests.patch(url, json=json)

        print("json:", r.json())
        r.raise_for_status()

        self.assertEqual(200, r.status_code,
                         "El codigo http es diferente a 200")


class TestViewMakeOrder(TestCase):

    def test_wrong_method(self):
        url = f"http://127.0.0.1:8000/nutrinal_pa/make_order"

        r = requests.get(url)

        self.assertEqual(405, r.status_code,
                         "El codigo http es diferente a 405")

    def test_missing_field(self):
        """
        "data":{
    "identifier_client": ""
    "identifier_seller": "",
    "code_product":"",
    "cant_product":{},
    "shipping_destination": ""

        """

        missing_client = {
            "data": {
                "identifier_seller": "12345",
                "code_product": "123",
                "cant_product": 100,
                "shipping_destination": "jajjdjjd"
            }
        }
        missing_seller = {"data": {
            "identifier_client": "JP123",
            "code_product": "123",
            "cant_product": 100,
            "shipping_destination": "jajjdjjd"
        }}

        missing_product = {"data": {
            "identifier_seller": "12345",
            "identifier_client": "JP123",
            "cant_product": 100,
            "shipping_destination": "jajjdjjd"
        }}

        missing_cant_product = {
            "data": {
                "identifier_seller": "12345",
                "identifier_client": "JP123",
                "code_product": "123",
                "shipping_destination": "jajjdjjd"
            }
        }

        missing_shipping = {
            "data": {
                "identifier_seller": "12345",
                "identifier_client": "JP123",
                "code_product": "123",
                "cant_product": 100,
            }
        }

        missing_data = {}

        list = [missing_client, missing_seller, missing_cant_product,
                missing_data, missing_product, missing_shipping]

        url = f"http://127.0.0.1:8000/nutrinal_pa/make_order"

        for field in list:
            r = requests.post(url=url, json=field)

            self.assertEqual(400, r.status_code, "El codigo http es igual 400")
            print("json: ", r.json())

    def test_do_no_exist_client(self):

        data = {
            "data": {
                "identifier_client": "P123",
                "identifier_seller": "12345",
                "code_product": "123",
                "cant_product": 100,
                "shipping_destination": "jajjdjjd"
            }
        }

        url = f"http://127.0.0.1:8000/nutrinal_pa/make_order"

        r = requests.post(url=url, json=data)

        self.assertEqual(404, r.status_code, "El codigo http es igual 404")
        print("json: ", r.json())

    def test_do_no_exist_seller(self):
        data = {
            "data": {
                "identifier_client": "JP123",
                "identifier_seller": "1235",
                "code_product": "123",
                "cant_product": 100,
                "shipping_destination": "jajjdjjd"
            }
        }

        url = f"http://127.0.0.1:8000/nutrinal_pa/make_order"

        r = requests.post(url=url, json=data)

        self.assertEqual(404, r.status_code, "El codigo http es igual 404")
        print("json: ", r.json())

    def test_do_no_exist_product(self):
        data = {
            "data": {
                "identifier_client": "JP123",
                "identifier_seller": "12345",
                "code_product": "12",
                "cant_product": 100,
                "shipping_destination": "jajjdjjd"
            }
        }

        url = f"http://127.0.0.1:8000/nutrinal_pa/make_order"

        r = requests.post(url=url, json=data)

        self.assertEqual(404, r.status_code, "El codigo http es igual 404")
        print("json: ", r.json())

    def test_post_valid(self):
        data = {
            "data": {
                "identifier_client": "JP123",
                "identifier_seller": "12345",
                "code_product": "123",
                "cant_product": {
                    "code": "123",
                    "cant": 100
                },
                "shipping_destination": "jajjdjjd"
            }
        }

        url = f"http://127.0.0.1:8000/nutrinal_pa/make_order"

        r = requests.post(url=url, json=data)

        self.assertEqual(200, r.status_code, "El codigo http es igual 200")
        print("json: ", r.json())


class TestViewGetCantProduct(TestCase):

    def test_post_data(self):

        data = {
            "code": "122466"
        }

        url = "http://127.0.0.1:8000/nutrinal_pa/admin/get_cant_product"

        r = requests.post(url=url, json=data)

        cant = r.json()['data']

        print("cant: ", cant)
