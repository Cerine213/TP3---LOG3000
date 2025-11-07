# Module static

## Raison d’être
Le répertoire `static` contient tous les fichiers statiques utilisés par l'application Flask, 
comme les feuilles de style CSS et les images éventuelles. Ces fichiers définissent le style 
et l'apparence de l'interface utilisateur de la calculatrice.

## Fichiers principaux et responsabilités
- `style.css` : définit la mise en page, la palette de couleurs, les styles des boutons, 
  et les animations lors des interactions utilisateur.

## Dépendances / hypothèses
- Les fichiers CSS sont référencés dans le template HTML via `url_for('static', filename='style.css')`.
- Aucun autre fichier statique n’est actuellement utilisé, mais le répertoire peut accueillir 
  des images, des icônes ou des scripts JavaScript si nécessaire.