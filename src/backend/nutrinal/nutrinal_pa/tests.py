from django.test import TestCase
import requests

from .JsonReponse import ReponseJson, StatusResponse


class TestViewLogin(TestCase):

    def test_valid_reponse():

        routes_valid = [
            "http://127.0.0.1:8000/nutrinal_pa/login/client",
            "http://127.0.0.1:8000/nutrinal_pa/login/seller",
            "http://127.0.0.1:8000/nutrinal_pa/login/admin"
        ]

        route_invalid = [
            "http://127.0.0.1:8000/nutrinal_pa/login/body",
            "http://127.0.0.1:8000/nutrinal_pa/login/ed",
            "http://127.0.0.1:8000/nutrinal_pa/login/bee",
        ]
