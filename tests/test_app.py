"""
*** test_app.py ***

Description : Tests unitaires pour le serveur Flask (app.py). Vérifie le bon fonctionnement de la route principale
              et l'évaluation des expressions arithmétiques.
Dépendances :
    - app.py
    - unittest (module standard Python)
    - Flask (test client)
"""

import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    """Classe regroupant les tests unitaires pour le serveur Flask."""

    def setUp(self):
        """Prépare le client de test Flask avant chaque test."""
        app.testing = True
        self.client = app.test_client()

    def test_get_index(self):
        """Vérifie que la page principale est accessible via GET."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Flask Calculator', response.data)

    def test_post_addition(self):
        """Vérifie que le résultat d'une addition simple est affiché correctement."""
        response = self.client.post('/', data={'display': '2+3'})
        self.assertIn(b'5.0', response.data)

    def test_post_subtraction(self):
        """Vérifie que le résultat d'une soustraction simple est affiché correctement."""
        response = self.client.post('/', data={'display': '5-2'})
        self.assertIn(b'3.0', response.data)

    def test_post_multiplication(self):
        """Vérifie que le résultat d'une multiplication simple est affiché correctement."""
        response = self.client.post('/', data={'display': '2*3'})
        self.assertIn(b'6.0', response.data)

    def test_post_division(self):
        """Vérifie que le résultat d'une division simple est affiché correctement."""
        response = self.client.post('/', data={'display': '6/2'})
        self.assertIn(b'3.0', response.data)

    def test_post_invalid_expression(self):
        """Vérifie qu'une expression invalide renvoie une erreur."""
        response = self.client.post('/', data={'display': '5++2'})
        self.assertIn(b'Error', response.data)

    def test_post_non_numeric(self):
        """Vérifie qu'une expression avec des lettres renvoie une erreur."""
        response = self.client.post('/', data={'display': 'a+b'})
        self.assertIn(b'Error', response.data)

    def test_post_empty(self):
        """Vérifie qu'une requête POST avec champ vide renvoie une erreur."""
        response = self.client.post('/', data={'display': ''})
        self.assertIn(b'Error', response.data)

if __name__ == '__main__':
    unittest.main()