from django.test import TestCase, Client
from django.http import Http404

class LoginViewTest(TestCase):
   
    def setUp(self):
        self.client = Client()  # Cliente de prueba para simular solicitudes HTTP

    def test_admin_user(self):
        response = self.client.get('/login/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenido: admin")  # Corrige la verificación de contenido

    def test_client_user(self):
        response = self.client.get('/login/client/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenido: client")  # Corrige la verificación de contenido

    def test_seller_user(self):
        response = self.client.get('/login/seller/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenido: seller")  # Corrige la verificación de contenido

    def test_invalid_user(self):
        response = self.client.get('/login/unknown/')
        self.assertEqual(response.status_code, 404)