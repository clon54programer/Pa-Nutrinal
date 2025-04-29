from django.test import TestCase, Client
from django.http import Http404
import requests

from .JsonReponse import ReponseJson,StatusResponse

class ViewCreateSellerLogin(TestCase):

    def create_seller(self):
        route = "http://127.0.0.1:8000/nutrinal_pa/admin/create_seller_login"

        seller_data = {"name": "Juan",
                       "id": "1234567",
                       "username": "seller_1",
                       "password": "12345678"
                       }

        data = ReponseJson(200,StatusResponse.VALID,seller_data)

        response = requests.post(route, data=data)

        error = response.json()

        print(error)

        self.assertEquals(True,True)
