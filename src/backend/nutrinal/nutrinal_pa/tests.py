from django.test import TestCase, Client
from django.http import Http404

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()  

    def test_admin_user(self):
        response = self.client.get('/login/admin/')  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Bienvenido: admin", response.content)

    def test_client_user(self):
        response = self.client.get('/login/client/')  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Bienvenido: client", response.content)

    def test_seller_user(self):
        response = self.client.get('/login/seller/')  
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Bienvenido: seller", response.content)

    def test_invalid_user(self):
        with self.assertRaises(Http404):  # Prueba para un tipo de usuario inválido
            self.client.get('/login/unknown/')