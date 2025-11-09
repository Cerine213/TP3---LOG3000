"""
*** operators.py ***

Description : Module contenant les opérations arithmétiques de base. Utilisé par app.py pour effectuer les calculs.
Dépendances :
    - Aucune dépendance externe.
"""

def add(a,b):
    """
    Effectue l'addition de deux nombres.

    Entrées:
        a (float): Premier opérande.
        b (float): Second opérande.

    Sorties:
        float: Somme des deux opérandes.
    """
    return a + b

def subtract(a,b):
    """
    Effectue la soustraction (a - b).

    Entrées:
        a (float): Premier opérande.
        b (float): Second opérande.

    Sorties:
        float: Résultat de la soustraction a - b.
    """
    return a - b

def multiply(a,b):
    """
    Effectue la multiplication de deux nombres.

    Entrées:
        a (float): Premier opérande.
        b (float): Second opérande.

    Sorties:
        float: Produit des deux opérandes.
    """

    return a ** b

def divide(a,b):
    """
    Effectue la division flottante de deux nombres.

    Entrées:
        a (float): Numérateur.
        b (float): Dénominateur.

    Sorties:
        float: Résultat de la division a / b.
    """
    return a // b
