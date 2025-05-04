from django.test import TestCase
import requests

from .JsonReponse import ReponseJson, StatusResponse


class TestViewLogin(TestCase):

    def test_valid_reponse(self):

        routes_valid = [
            "http://127.0.0.1:8000/nutrinal_pa/login/client",
            "http://127.0.0.1:8000/nutrinal_pa/login/seller",
            "http://127.0.0.1:8000/nutrinal_pa/login/admin"
        ]

        for iter in routes_valid:
            r = requests.get(iter)

            self.assertEqual(200, r.status_code,
                             "El codigo http de respuesta es diferente a 200")

            print(r.text)

        route_invalid = [
            "http://127.0.0.1:8000/nutrinal_pa/login/body",
            "http://127.0.0.1:8000/nutrinal_pa/login/ed",
            "http://127.0.0.1:8000/nutrinal_pa/login/bee",
        ]
