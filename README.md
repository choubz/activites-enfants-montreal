# Activités enfants – île de Montréal

Liste d'activités pour enfants sur l'île de Montréal (80 fiches) : musées, patinoires, plages, parcs, jeux d'eau.

- **Page de consultation :** https://choubz.github.io/activites-enfants-montreal/
- **`index.html`** : page autonome (filtres par âge, gratuité, catégorie, statut ; une fiche ancrée par lieu, ex. `#patinoire-de-la-tohu`).
- **`carte.csv`** : 101 repères prêts à importer dans Google My Maps.

## Importer la carte dans Google My Maps

1. Ouvrir https://www.google.com/maps/d/ puis « Créer une carte ».
2. « Importer » et choisir `carte.csv`.
3. Colonne de position : **Recherche (adresse ou lieu)**. Titre des repères : **Nom**.
4. Style par catégorie : colonne **Catégorie**.
5. Vérifier les repères dont la colonne **Précision** vaut `nom` (placés d'après le nom du lieu, sans adresse).
6. « Partager » : accès « Toute personne disposant du lien ». Puis menu ⋮ de la carte → « Intégrer sur mon site » et copier l'URL de l'attribut `src`.
7. Coller cette URL dans `index.html`, constante `MAP_EMBED_URL` (déjà fait : carte « carte activite montreal »).

La colonne **Fiche (lien)** de chaque repère pointe vers la fiche correspondante de la page.

## Limites

- Les informations viennent de publications TikTok, de sites officiels et de quelques sources tierces. Chaque fiche indique son statut (confirmé ou à vérifier). « n.d. » = non disponible, rien n'a été deviné.
- 13 fiches n'ont pas de repère : adresse inconnue ou lieu non précis (voir les fiches sans repère sur la page).
- Les prix et horaires changent : confirmer avant de se déplacer.

## Régénérer le site

Les sources sont dans `src/` (`data.py` : les fiches, `template.html` : la page, `build.py` : le générateur).
Depuis la racine du dépôt : `python3 -I src/build.py .` réécrit `index.html` et `carte.csv`.
`aujourdhui.json` est mis à jour chaque matin par le workflow n8n « Activités enfants du jour (Montréal) ».
