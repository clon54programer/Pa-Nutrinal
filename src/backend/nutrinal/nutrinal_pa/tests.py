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

    def test_get_data(self):
        url_get = "http://127.0.0.1:8000/nutrinal_pa/admin/create_seller_login"

        r = requests.get(url_get)
        print(r.headers.get("Content-Type"))

        content = r.json()

        print("status code: ", r.status_code)
        print("json", content['data'])

    def test_missing_field():
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
