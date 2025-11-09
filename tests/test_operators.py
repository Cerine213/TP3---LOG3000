"""
*** test_operators.py ***

Description : Tests unitaires pour le module operators.py. Vérifie le bon fonctionnement des fonctions arithmétiques
              et détecte les bogues éventuels.
Dépendances :
    - operators.py
    - unittest (module standard Python)
"""

import unittest
from operators import add, subtract, multiply, divide

class TestOperators(unittest.TestCase):
    """Classe regroupant les tests unitaires pour les fonctions arithmétiques."""


    def test_add_positive_numbers(self):
        """Vérifie que add() retourne la somme correcte pour des nombres positifs."""
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        """Vérifie add() avec des nombres négatifs."""
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        """Vérifie add() avec un nombre positif et un nombre négatif."""
        self.assertEqual(add(5, -3), 2)
 
    def test_subtract_positive_numbers(self):
        """Vérifie subtract() avec des nombres positifs."""
        self.assertEqual(subtract(5, 3), 2)  

    def test_subtract_negative_numbers(self):
        """Vérifie subtract() avec des nombres négatifs."""
        self.assertEqual(subtract(-5, -3), -2) 

    def test_multiply_positive_numbers(self):
        """Vérifie multiply() avec des nombres positifs."""
        self.assertEqual(multiply(2, 3), 6) 

    def test_multiply_with_zero(self):
        """Vérifie multiply() avec zéro."""
        self.assertEqual(multiply(0, 5), 0)  
  
    def test_divide_positive_numbers(self):
        """Vérifie divide() avec des nombres positifs."""
        self.assertEqual(divide(6, 2), 3)  
    def test_divide_by_zero(self):
        """Vérifie que divide() lève une exception si le dénominateur est zéro."""
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_divide_negative_numbers(self):
        """Vérifie divide() avec des nombres négatifs."""
        self.assertEqual(divide(-5, 2), -2.)

if __name__ == '__main__':
    unittest.main()