"""
*** app.py ***

Description    : Fichier principal du serveur Flask. Gère les requêtes HTTP, 
                 l'affichage du frontend et l'exécution des calculs arithmétiques.
                 
Dépendances :
- Flask (framework web)
- operators.py (module local contenant les fonctions d'opérations de base)
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

"""Dictionnaire associant les opérateurs symboliques à leurs fonctions respectives."""
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """
    Évalue une expression arithmétique simple à deux opérandes (ex : "5+2").

    Rôle :
        Valide et interprète l'expression reçue depuis le frontend, puis exécute
        l'opération correspondante à l'aide du module operators.

    Entrées:
        expr (str): Expression à évaluer (doit contenir exactement un opérateur valide).

    Sorties:
        float: Résultat numérique de l'opération.

    Exceptions:
        ValueError: Si l'expression est vide, invalide, ou contient plusieurs opérateurs.
        ValueError: Si les opérandes ne sont pas des nombres valides.
        Exception:  Si une erreur inattendue se produit lors du calcul.
    """
    
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application Flask.

    Rôle :
        - Affiche la page de la calculatrice.
        - Reçoit les requêtes POST contenant l'expression à calculer.
        - Affiche le résultat ou un message d'erreur.

    Sorties:
        str: Page HTML rendue avec la valeur du résultat calculé.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)