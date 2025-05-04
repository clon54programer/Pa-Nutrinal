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
        json = {}

        r = requests.post(
            "http://127.0.0.1:8000/nutrinal_pa/create_seller_login", js)
