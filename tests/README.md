# Tests

## Raison d’être
Le répertoire `tests` contient tous les tests unitaires et d’intégration pour le projet de calculatrice Flask.  
Ces tests permettent de vérifier la validité des fonctions arithmétiques et le bon fonctionnement du serveur Flask.

---

## Fichiers principaux

- `test_operators.py`  
  - Contient les tests unitaires pour les fonctions du module `operators.py` (`add`, `subtract`, `multiply`, `divide`).  
  - Vérifie les cas normaux, les cas limites et les erreurs (ex: division par zéro, opérandes non numériques).  

- `test_app.py`  
  - Contient les tests pour le serveur Flask (`app.py`).  
  - Vérifie la route `/` en GET et POST.  
  - Teste que les résultats des calculs sont correctement affichés dans la page HTML et que les erreurs sont bien gérées.

---

## Dépendances

- Python 3.x  
- Module `unittest` (inclus avec Python)  
- Flask (pour `test_app.py`)  
- Modules locaux : `operators.py`, `app.py`

---

## Exécution des tests

Depuis la racine du projet :

```bash
# Avec unittest
python -m unittest discover tests
