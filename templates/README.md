# Module templates

## Raison d’être
Le répertoire `templates` contient les fichiers HTML qui composent l'interface utilisateur de l'application. 
Flask utilise ces templates pour générer les pages web dynamiques avec les résultats des calculs.

## Fichiers principaux et responsabilités
- `index.html` : page principale de la calculatrice. Contient :
  - le champ d'affichage (`display`) pour montrer l’expression ou le résultat,
  - tous les boutons numériques et opérateurs,
  - le script JavaScript pour la gestion de l'affichage côté client.

## Dépendances / hypothèses
- Dépend de `style.css` dans `static/` pour le style.
- Les valeurs des boutons sont envoyées au serveur via une requête POST sur `/`.
- Assumes que Flask est configuré pour trouver les templates dans ce répertoire.