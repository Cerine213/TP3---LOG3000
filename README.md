# TP3---LOG3000

**Équipe : 30**

## Objectif du projet
Développer une application web en Python permettant d’effectuer des opérations mathématiques simples, comme une calculatrice.  
L’interface web est générée via un fichier HTML et les calculs sont exécutés côté serveur avec la bibliothèque Flask de Python.

---

## Structure du projet

TP3-LOG3000/
│
├── app.py # Application principale Flask
├── operators.py # Fonctions arithmétiques de base
├── templates/
| ├── README.md # Documentation du module templates
│ └── index.html # Interface utilisateur
├── static/
| ├── README.md # Documentation du module static
│ └── style.css # Feuille de style
│
├── tests/
| ├── README.md # Documentation du module  tests
│ ├── test_app.py # Tests unitaires pour Flask
│ └── test_operators.py # Tests unitaires pour les opérations
│
└── README.md # Documentation du projet

---

## 🧩 Prérequis d’installation

Avant de lancer le projet, vous devez avoir installé :

- **Python 3.11 ou supérieur**
- **pip**
- **Git**

---

## Instructions d’installation & d’exécution


1. **Créer et activer un environnement virtuel**
   - **macOs / Linux**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows (PowerShell)**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
       
2. **Installer les dépendances**
   ```bash
   pip install flask
   ```
   
3. **Lancer l'application**
   - Avec **python**:
   ```bash
   python app.py
   ```
   - Ou avec **Flask**
   ```bash
   flask run
   ```
   L'application devrait être accessible via votre navigateur à l'adresse: http://127.0.0.1:5000.

---

## Exécution des tests unitaires

Depuis la racine du projet, assurez-vous que votre environnement virtuel est activé.

**Lancer tous les tests automatiquement :**
```bash
python -m unittest discover tests
```

**Lancer uniquement les tests du module des opérateurs :**
```bash
python -m unittest tests/test_operators.py
```

**Lancer uniquement les tests du serveur Flask :**
```bash
python -m unittest tests/test_app.py
```

Si tous les tests passent, vous verrez un message similaire à :
```bash
----------------------------------------------------------------
 ..
----------------------------------------------------------------
Ran 8 tests in 0.023s

OK
```

En cas d’erreur, le message affichera le test qui a échoué,
accompagné d’un message d’erreur détaillé (par ex. division par zéro ou mauvaise réponse HTTP).

--- 

## Flux de contribution

Pour contribuer au projet, suivez ce processus recommandé afin de maintenir une base de code propre et collaborative :

1. **Branches**
   - La branche principale `main` contient toujours la version stable.
   - Pour chaque nouvelle fonctionnalité, bugfix ou test, créez une branche depuis `main` :
     ```bash
     git checkout -b nom-de-votre-branche
     ```
   - Nommez vos branches de manière descriptive, par exemple :
     - `feature/calculatrice-avancee`
     - `bugfix/division-par-zero`
     - `test/operators-module`

2. **Pull Requests (PR)**
   - Une fois votre travail terminé sur votre branche, poussez-la sur GitHub :
     ```bash
     git push origin nom-de-votre-branche
     ```
   - Ouvrez une Pull Request (PR) vers `main`.
   - Décrivez clairement les changements, le problème résolu ou la fonctionnalité ajoutée.
   - Attendez la revue d’au moins un membre de l’équipe avant de fusionner.

3. **Issues**
   - Utilisez les issues pour signaler :
     - Les bugs détectés
     - Les suggestions de nouvelles fonctionnalités
     - Les questions sur le projet
   - Lors de la création d’une issue, fournissez :
     - Un titre descriptif
     - Une description claire du problème ou de la proposition
     - Les étapes pour reproduire un bug ou tester une suggestion
   - Assignez les issues aux membres responsables pour le suivi.

4. **Bonnes pratiques**
   - Commits fréquents et descriptifs
   - Messages de commit clairs : 
     - `Add tests for operators module`
     - `Fix subtraction bug in operators.py`
   - Garder la branche `main` propre et stable
   - Exécuter les tests avant chaque PR

---