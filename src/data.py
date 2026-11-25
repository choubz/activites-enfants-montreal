# -*- coding: utf-8 -*-
# Données reprises telles quelles du tableur « Activités enfants – île de Montréal » (rév. 6).
# Champs : src, cat, nom, typ, lieu, age, prix, saison, liens, compte, statut, notes, free, tags, markers
# free : "oui" (gratuit) | "enfants" (gratuit pour les enfants) | ""
# tags : p = tout-petits 0-5, s = 6-12, t = tous âges
# markers : [(suffixe|None, requête de géocodage, "adresse"|"nom")]  — vide = non placé sur la carte

ITEMS = []

def I(src, cat, nom, typ, lieu, age, prix, saison, liens, compte, statut, notes, free="", tags="", markers=()):
    if isinstance(liens, str):
        liens = [x.strip() for x in liens.split(" ; ") if x.strip()]
    ITEMS.append(dict(src=src, cat=cat, nom=nom, typ=typ, lieu=lieu, age=age, prix=prix, saison=saison,
                      liens=liens, compte=compte, statut=statut, notes=notes, free=free, tags=tags,
                      markers=list(markers)))

TT = "tt"
VERIF = "à vérifier"
ND = "n.d."

# ---------------------------------------------------------------- Activités (TikTok + sites officiels)
I(TT, "Patinoire", "Patinoire de la Tohu", "Patinoire extérieure", "Tohu, 2345 rue Jarry E., Saint-Michel (H1Z 4P3)", ND,
  "Gratuit ; location de patins n.d. ‡", "Saison 2025-26 : fins de semaine du 29 nov. au 9 mars ; saison 2026-27 n.d.",
  "https://www.tiktok.com/@floploush/video/7453483068326677766", "Floploush", VERIF,
  "Horaires 2025-26 (site tohu.ca) ; 2026-27 non publiés. Post de déc. 2024.", "oui", "",
  [(None, "2345 rue Jarry E., Montréal, QC H1Z 4P3", "adresse")])
I(TT, "Musée / expo", "Centre des sciences de Montréal (dont Mini Mondo)", "Musée des sciences (expos, IMAX, jeux)",
  "2 rue de la Commune O., Vieux-Port (H2Y 4B2)", "Mini Mondo 0-7 ans ; Explore / Humain dès 6 ans ; Fabrik2, Nanualuk, Signes de vie dès 8 ans",
  "n.d. (Mini Mondo dès 18,50 $ †)", "Mini Mondo : 3 sept.-20 déc., lun.-jeu. 9 h-16 h ; autres horaires n.d.",
  "https://www.tiktok.com/@chloen215/video/7589829194935323924 ; https://www.tiktok.com/@chloen215/video/7590902303499013396",
  "Activities_montreal", VERIF, "Tarifs non trouvés sur le site officiel.", "", "ps",
  [(None, "2 rue de la Commune O., Montréal, QC H2Y 4B2", "adresse")])
I(TT, "Jeu intérieur", "IKEA Montréal – Småland", "Aire de jeux (magasin)", ND, ND, ND, ND,
  "https://www.tiktok.com/@montrealwithkids/video/7666050515465276679 ; https://www.tiktok.com/@montrealwithkids/video/7703970870930279698",
  "Montreal With Kids", VERIF, "Non vérifié (site IKEA non consulté).")
I(TT, "Sortie nature", "Jardin botanique de Montréal", "Sortie nature (jardins, serres)", "4101 rue Sherbrooke E., Hochelaga-Maisonneuve", ND,
  "Tarif 2026 « un musée » : adulte 25,50 $ ; 5-17 ans 13,50 $ ; famille 68 $ (2 adultes + 3 enfants 5-17) ; gratuit ≤ 4 ans (espacepourlavie.ca)",
  "Horaires n.d.",
  "https://www.tiktok.com/@miel.tropical/video/7539294838974369031 ; https://www.tiktok.com/@scotwithone.t/video/7544041998810909959",
  "miel.tropical ; Scot with one T", VERIF, "Posts sponsorisés (août 2025).", "", "",
  [(None, "4101 rue Sherbrooke E., Montréal, QC", "adresse")])
I(TT, "Jeu intérieur", "BoulZeye", "Bowling, laser tag 2 étages, arcade, escape rooms", "Pointe-aux-Trembles, 3655 boul. du Tricentenaire †", ND, ND,
  "Restaurant 11 h-minuit † ; autres horaires n.d.", "https://www.tiktok.com/@montrealwithkids/video/7671444200835075336",
  "Montreal With Kids", VERIF, "Sur l'île (Pointe-aux-Trembles).", "", "",
  [(None, "3655 boul. du Tricentenaire, Montréal, QC", "adresse")])
I(TT, "Immersif", "Carnaval des animaux immersif (OASIS immersion)", "Spectacle / expérience immersive",
  "Palais des congrès, 301 rue Saint-Antoine O., centre-ville", "4-12 ans (Arsenal)", "≈ 26 $ / adulte † ; code montrealwithkids10 (-10 %)",
  "27 fév.-30 août 2026 (TERMINÉ) ; 70-75 min", "https://www.tiktok.com/@montrealwithkids/video/7613207345216130311",
  "Montreal With Kids", VERIF, "Expo actuelle d'OASIS : « Rolling Stone Presents: Amplified » jusqu'au 14 fév. †.", "", "s",
  [(None, "301 rue Saint-Antoine O., Montréal, QC", "adresse")])
I(TT, "Immersif", "Musée Imaginarium", "Musée immersif (décors)", "290 rue de la Montagne, Griffintown", "Tous âges",
  "0-2 ans gratuit ; 3-17 ans 25 $ ; 18+ 35 $ †", "11 h-20 h tous les jours † ; ~1 h",
  "https://www.tiktok.com/@romy.etcie/video/7669552111461354760", "Romy & cie", VERIF, "Ville confirmée : Montréal.", "", "t",
  [(None, "290 rue de la Montagne, Montréal, QC", "adresse")])
I(TT, "Sortie / visite", "Centrale de la Rivière-des-Prairies (Hydro-Québec)", "Visite industrielle", "Rivière-des-Prairies (à confirmer)", ND, ND, ND,
  "https://www.tiktok.com/@hydroquebec/video/7525533680740109624", "Hydro-Québec", VERIF, "Non vérifié ; adaptée aux enfants ? Post de juil. 2025.", "", "",
  [(None, "Centrale de la Rivière-des-Prairies, Montréal, QC", "nom")])
I(TT, "Jeu intérieur", "We Rock The Spectrum", "Centre de jeu inclusif", "12395 rue Lachapelle ‡", ND, ND,
  "Mar.-ven. 10 h-19 h ; sam.-dim. 9 h-17 h ; lun. fermé ‡", "https://www.tiktok.com/@montrealwithkids/video/7615370467947351314",
  "Montreal With Kids", VERIF, "Site officiel introuvable.", "", "",
  [(None, "12395 rue Lachapelle, Montréal, QC", "adresse")])
I(TT, "Jeu intérieur", "Funville", "Centre d'amusement intérieur (grimper, glisser)", "9420 boul. de l'Acadie ‡", ND, ND, ND,
  "https://www.tiktok.com/@montrealwithkids/video/7590096543488003349", "Montreal With Kids", VERIF,
  "Adresse tirée de la légende du post (31 déc. 2025). Site officiel non vérifié.", "", "",
  [(None, "9420 boul. de l'Acadie, Montréal, QC", "adresse")])
I(TT, "Jeu intérieur", "Kawaï boutique", "Aire de jeux tout-petits + ateliers sensoriels et créatifs", "7335 boul. Décarie ‡ (métro Namur)", "Tout-petits (n.d. précis)",
  ND, ND, "https://www.tiktok.com/@montrealwithkids/video/7607200109717097746", "Montreal With Kids", VERIF,
  "Collaboration / post promotionnel. Aussi cité par Isabel.", "", "p",
  [(None, "7335 boul. Décarie, Montréal, QC", "adresse")])
I(TT, "Jeu intérieur", "Funvie Playground", "Aire de jeux intérieure", ND, ND, ND, ND,
  "https://www.tiktok.com/@isabel_mama_ortho/photo/7626367022183550216", "Isabel | Mama & orthopédagogue", VERIF,
  "Simple mention dans un post-liste ; non vérifié.")
I(TT, "Sortie / visite", "Petit zoo intérieur – Place Versailles", "Mini-ferme intérieure", "Place Versailles, 7275 rue Sherbrooke E. (H1N 1E9)", ND,
  "Gratuit ‡", "Saisonnier, ouvert vers nov. 2026 ‡", "https://www.tiktok.com/@mtlmama_/video/7704773064252247317", "Montreal Mama", VERIF,
  "Non confirmé par le centre commercial.", "oui", "",
  [(None, "7275 rue Sherbrooke E., Montréal, QC H1N 1E9", "adresse")])
I(TT, "Sortie / visite", "Chocolat Boréal (visite de chocolaterie)", "Visite de fabrication", "LaSalle (adresse n.d.)", ND, ND, "n.d. (idée jour de pluie)",
  "https://www.tiktok.com/@jedepenselocal/video/7710122130460953864", "Amélie - Je déPENSE local", VERIF, "Post sponsorisé.", "", "",
  [(None, "Chocolat Boréal, LaSalle, Montréal, QC", "nom")])
I(TT, "Jeu intérieur", "Soccer iQ Griffintown", "Soccer intérieur (3 terrains)",
  "Griffintown (adresse n.d.) ; autre site : 9055 rue Pascal-Gagnon, Saint-Léonard", "Saint-Léonard : U8-U18 ; Griffintown n.d.",
  "Journées d'ouverture gratuites 21-22 nov. 2026 ; tarifs n.d.", ND, "https://www.tiktok.com/@racha.sadk/video/7709667014721146132", "Racha Sadouk", VERIF,
  "Gratuité = jours d'ouverture (passés). Post lié à un concours PS5. Sur la carte : le site de Saint-Léonard seulement (Griffintown sans adresse).", "", "s",
  [("Saint-Léonard", "9055 rue Pascal-Gagnon, Montréal, QC", "adresse")])
I(TT, "Immersif", "Bubble Planet", "Expérience immersive", "Place Bonaventure, 800 rue de la Gauchetière O.", "Tous âges ; ≤ 2 ans gratuit †",
  "Dès 26,90 $ †", "Dates vues : 4 août-7 sept. (passées) ; actuelles n.d.", "https://www.tiktok.com/@montrealwithkids/video/7613540227663039752",
  "Montreal With Kids", VERIF, "Post sponsorisé.", "", "t",
  [(None, "800 rue de la Gauchetière O., Montréal, QC", "adresse")])
I(TT, "Immersif", "Dino's Alive", "Expo immersive dinosaures", "Place Bonaventure, 800 rue de la Gauchetière O.", "Tous âges (n.d. précis)",
  "Dès 16,90-17,90 $ † ; code MTLWITHKIDS10", "Dates variables (ex. 14 déc.-11 janv., Fever †)",
  "https://www.tiktok.com/@itsmoikaa/video/7539634269279227143", "It'sMoika", VERIF, "Post de 2025 ; dates à reconfirmer.", "", "t",
  [(None, "800 rue de la Gauchetière O., Montréal, QC", "adresse")])
I(TT, "Immersif", "FAB Expo", "Expérience immersive (20-21 mondes, grande fosse à balles)", "Centre Eaton, 705 rue Sainte-Catherine O., niveau 2", "0-2 ans gratuit ‡",
  "Famille 85 $ + taxes (2 adultes + 2 enfants 3-18 ans) ‡", ND, "https://www.tiktok.com/@montrealwithkids/video/7590526085809425672",
  "Montreal With Kids", VERIF, "Site : lafabexpo.com (tarifs non relus).", "", "",
  [(None, "705 rue Sainte-Catherine O., Montréal, QC", "adresse")])
I(TT, "Jeu intérieur", "Art Chaos", "Atelier d'art / jeu", "Mile End (Plateau) †, adresse n.d.", "Gratuit ≤ 4 ans ‡", ND, ND,
  "https://www.tiktok.com/@montrealwithkids/video/7594192521136229650", "Montreal With Kids", VERIF, "Post exact dans la liste MWK à confirmer.")
I(TT, "Jeu intérieur", "The Man Who Planted Trees", ND, ND, ND, ND, ND,
  "https://www.tiktok.com/@montrealwithkids/video/7594192521136229650", "Montreal With Kids", VERIF, "Rien trouvé ; post exact à confirmer.")
I(TT, "Jeu intérieur", "Espace Pauze Café", "Café-jeux (à préciser)", ND, ND, ND, ND,
  "https://www.tiktok.com/@montrealwithkids/video/7594192521136229650", "Montreal With Kids", VERIF, "Rien trouvé ; post exact à confirmer.")
I(TT, "Bibliothèque / piscine", "Centre Sanaaq (bibliothèque)", "Bibliothèque / heure du conte", "1200 rue du Sussex (H3H 0E3)", "Heure du conte dès 3 ans",
  "Gratuit", "Bibliothèque 10 h-18 h le jour consulté ; avis de grève municipale",
  "https://www.tiktok.com/@isabel_mama_ortho/video/7620933539860630792", "Isabel | Mama & orthopédagogue", VERIF,
  "Source montreal.ca ; liste Isabel (mélange Montréal / Laval).", "oui", "p",
  [(None, "1200 rue du Sussex, Montréal, QC H3H 0E3", "adresse")])
I(TT, "Immersif", "The Art of the Brick", "Expo LEGO", "312 rue Sainte-Catherine O.", "Tous âges ; ~45-50 min", "Dès 24,90 $ †",
  "Fever † : 12 déc.-10 janv. ; reste n.d.", "https://www.tiktok.com/@montrealwithkids/video/7594192521136229650", "Montreal With Kids", VERIF,
  "Post exact à confirmer.", "", "t",
  [(None, "312 rue Sainte-Catherine O., Montréal, QC", "adresse")])
I(TT, "Musée / expo", "Biodôme", "Musée nature (4 écosystèmes)", "4777 av. Pierre-De Coubertin (H1V 1B3), Hochelaga-Maisonneuve", "Gratuit ≤ 4 ans",
  "2026 « un musée » : adulte 25,50 $ ; 65+ 23 $ ; étudiant 19 $ ; 5-17 ans 13,50 $ ; famille 68 $ (2 adultes + 3 enfants 5-17). Résidents CMM : 18,50 / 17,50 / 14,75 / 9,25 / 51,50 $",
  "Horaires n.d.", "https://www.tiktok.com/@sharing_amandine/video/7343302733039930630", "Amandine", VERIF,
  "Post de mars 2024. Tarifs : espacepourlavie.ca. Cité aussi dans 2 itinéraires.", "", "",
  [(None, "4777 av. Pierre-De Coubertin, Montréal, QC H1V 1B3", "adresse")])
I(TT, "Musée / expo", "Planétarium Rio Tinto Alcan", "Spectacles du ciel (~20 min)", "4801 av. Pierre-de-Coubertin (H1V 3V4)", ND,
  "Même grille 2026 « un musée » que le Biodôme", "Horaires n.d.", "https://www.tiktok.com/@sharing_amandine/video/7343302733039930630",
  "Amandine", VERIF, "Post de 2024.", "", "",
  [(None, "4801 av. Pierre-de-Coubertin, Montréal, QC H1V 3V4", "adresse")])
I(TT, "Bibliothèque / piscine", "Bibliothèque de Pierrefonds", "Bibliothèque / activités tout-petits", "Pierrefonds (adresse n.d.)", "Tout-petits", "Gratuit ‡", ND,
  "https://www.tiktok.com/@isabel_mama_ortho/video/7620933539860630792", "Isabel | Mama & orthopédagogue", VERIF, "Adresse exacte n.d.", "oui", "p",
  [(None, "Bibliothèque de Pierrefonds, Montréal, QC", "nom")])
I(TT, "Jeu intérieur", "Nouvelle arcade (nom n.d.)", "Arcade", ND, "Grands enfants", ND, ND,
  "https://www.tiktok.com/@sharing_amandine/video/7343302733039930630", "Amandine", VERIF, "Post de 2024 ; nom non identifié.")
I(TT, "Jeu extérieur", "Tir à l'arc (nom n.d.)", "Tir à l'arc", ND, ND, ND, ND,
  "https://www.tiktok.com/@sharing_amandine/video/7343302733039930630", "Amandine", VERIF, "Post de 2024 ; nom non identifié.")
I(TT, "Jeu intérieur", "Café Actimuse", "Café + ateliers art / science", "12320 boul. Gouin O., Pierrefonds", ND,
  "-15 % sur une activité sans réservation jusqu'au 31 déc. 2026 (promo MWK)", ND,
  "https://www.tiktok.com/@montrealwithkids/photo/7685854190287015175", "Montreal With Kids", VERIF, "Post de sept. 2026.", "", "",
  [(None, "12320 boul. Gouin O., Montréal, QC", "adresse")])
I(TT, "Sortie / visite", "La Grande Roue de Montréal", "Grande roue (Vieux-Port)", "362 rue de la Commune E.", "Tous âges",
  "n.d. ; code Fever MTLWITHKIDS10 (affilié)", "Tous les jours 10 h-23 h ‡ ; 15-20 min",
  "https://www.tiktok.com/@montrealwithkids/video/7590531052687428882", "Montreal With Kids", VERIF,
  "Cité aussi dans 2 itinéraires (avec une aire de jeux cachée près du Vieux-Port, non nommée).", "", "t",
  [(None, "362 rue de la Commune E., Montréal, QC", "adresse")])
I(TT, "Jeu intérieur", "Sensetional", "Aire de jeux multisensorielle (7 salles)", "2435 rue Manella, bureau 224, Ville de Mont-Royal (H4P 2A5)",
  "Adaptée aux enfants à besoins spéciaux † ; âge n.d.", "24 $ ‡", ND, "https://www.tiktok.com/@magabounda/video/7577899733272874261", "magabounda", VERIF,
  "Sur l'île, mais dans la ville de Mont-Royal (enclave) ; site officiel non trouvé.", "", "",
  [(None, "2435 rue Manella, Mont-Royal, QC H4P 2A5", "adresse")])
I(TT, "Patinoire", "Patinoire de la Place des Arts", "Patinoire extérieure", "Place des Arts, Quartier des spectacles", ND, "Gratuit ‡", "Hiver ; horaires n.d.",
  "https://www.tiktok.com/@ayiti__/video/7599349412850109718", "Ayiti", VERIF, "Post de janv. 2026.", "oui", "",
  [(None, "Place des Arts, Montréal, QC", "nom")])
I(TT, "Sortie / visite", "Croisière dans le Vieux-Port", "Croisière", "Vieux-Port (adresse n.d.)", ND, ND, ND,
  "https://www.tiktok.com/@_kristalsiu_/photo/7684793361462562055", "_kristalsiu_", VERIF, "Cité dans un itinéraire (toddler).")

# ---------------------------------------------------------------- Ajouts web
WEB = "web"
I(WEB, "Patinoire", "Patinoire réfrigérée du lac aux Castors", "Patinoire (parc du Mont-Royal)", "2000 chemin Remembrance (H3H 1X2)", "Tous âges",
  "Accès gratuit ; autres frais possibles (location)", "12 déc. 2026-8 mars 2027, dates à confirmer",
  "https://www.bonjourquebec.com/fr-fr/repertoire/quoi-faire/patinoire-refrigeree-du-lac-aux-castors/2brn", None, VERIF,
  "Source tierce (Bonjour Québec).", "oui", "t",
  [(None, "2000 chemin Remembrance, Montréal, QC H3H 1X2", "adresse")])
I(WEB, "Patinoire", "Patinoire de l'Esplanade Tranquille", "Patinoire réfrigérée (Quartier des spectacles)", "Esplanade Tranquille, Place des Arts", "Tous âges",
  "Gratuite pour tous les patineurs", "Saison 2026-27 : dates n.d.",
  "https://www.timeout.com/fr/montreal/nouvelles/la-plus-grande-patinoire-exterieure-du-centre-ville-de-montreal-ouvre-aujourdhui-111523", None, VERIF,
  "Article Time Out d'une saison passée. Probablement la patinoire de la Place des Arts du post d'Ayiti (un seul repère sur la carte).", "oui", "t")
I(WEB, "Patinoire", "La Patinoire sous l'Anneau (Place Ville Marie)", "Patinoire extérieure", "Centre-ville, près du Centre Eaton", "Tous âges",
  "Gratuite ; location de patins sur place", "27 fév.-29 mars 2026 (passé) ; 2027 n.d.",
  "https://www.timeout.com/fr/montreal/nouvelles/le-centre-ville-de-montreal-accueille-une-nouvelle-patinoire-et-ce-nest-pas-la-ou-vous-pensez-122925",
  None, VERIF, "Source tierce.", "oui", "t",
  [(None, "Place Ville Marie, Montréal, QC", "nom")])
I(WEB, "Patinoire", "Patinoires extérieures municipales (200+)", "Patinage libre, hockey libre", "Dans les parcs de tous les arrondissements",
  "Tous âges (enfants de 8 ans et moins accompagnés à Anjou)", "Gratuit",
  "Hiver, selon la météo ; exemple Anjou : lun.-ven. 16 h-22 h, sam.-dim. 10 h-22 h", "https://montreal.ca/sujets/arenas-et-patinoires-exterieures",
  None, "confirmé (site officiel)", "Vérifier l'état de la glace sur montreal.ca/conditions-des-patinoires-exterieures.", "oui", "t")
I(WEB, "Bibliothèque / piscine", "Heure du conte en bibliothèque", "Bibliothèques de quartier",
  "Ex. Frontenac, 2550 rue Ontario E. ; La Petite-Patrie, 6707 av. De Lorimier", "0-18 mois, 19-36 mois, 3-6 ans selon la bibliothèque",
  "Gratuit ; inscription souvent obligatoire, priorité aux détenteurs de la carte des bibliothèques", "Séances hebdomadaires (ex. 6 et 7 nov. 2026)",
  "https://montreal.ca/evenements/heure-du-conte-0-36-mois-115319 ; https://montreal.ca/evenements/heure-du-conte-pour-poupons-118340", None,
  "confirmé (site officiel)", "Aussi : heure du conte bilingue à la bibliothèque interculturelle.", "oui", "p",
  [("Frontenac", "2550 rue Ontario E., Montréal, QC", "adresse"), ("La Petite-Patrie", "6707 av. De Lorimier, Montréal, QC", "adresse")])
I(WEB, "Bibliothèque / piscine", "YMCA Cartierville – baignade libre gratuite", "Piscine intérieure", "YMCA Cartierville (adresse n.d.)", "Tous âges, bébés bienvenus",
  "Gratuit pour les résidents de Montréal (pièce d'identité + preuve d'adresse possibles)", "Mardi 16 h-17 h 55 (liste partielle)",
  "https://montreal.ca/lieux/ymca-cartierville", None, "confirmé (site officiel)", "Réservation aux résidents : à revoir après l'installation.", "oui", "t",
  [(None, "YMCA Cartierville, Montréal, QC", "nom")])
I(WEB, "Bibliothèque / piscine", "Piscines municipales – bain libre et pataugeoires", "Bain libre (ex. Édouard-Montpetit, Annie-Pelletier, Saint-Roch)",
  "Annie-Pelletier : 8850 av. Dubuisson ; autres : voir fiches", "Pataugeoires pour familles avec jeunes enfants", "Baignade libre gratuite",
  "Horaires par piscine et par saison",
  "https://montreal.ca/lieux/piscine-edouard-montpetit ; https://montreal.ca/lieux/piscine-annie-pelletier ; https://montreal.ca/lieux/pataugeoire-de-la-piscine-saint-roch",
  None, "confirmé (site officiel)", "Fermetures temporaires possibles ; cours de natation payants (inscription Loisirs Montréal). Sur la carte : Annie-Pelletier seulement (seule adresse connue).", "oui", "p",
  [("Annie-Pelletier", "8850 av. Dubuisson, Montréal, QC", "adresse")])
I(WEB, "Musée / expo", "Insectarium (Espace pour la vie)", "Musée nature immersif", "Hochelaga-Maisonneuve (adresse n.d.)", "Tous âges",
  "Tarif 2026 « un musée » : adulte 25,50 $ ; 5-17 ans 13,50 $ ; famille 68 $ ; gratuit ≤ 4 ans", "Horaires n.d.",
  "https://espacepourlavie.ca/droits-dentree-pour-un-musee?mode=liste", None, "confirmé pour le prix",
  "Résidents de la CMM : 18,50 $ adulte, 9,25 $ 5-17 ans, 51,50 $ famille.", "", "st",
  [(None, "Insectarium de Montréal, Montréal, QC", "nom")])
I(WEB, "Musée / expo", "Biosphère (Espace pour la vie)", "Musée de l'environnement (parc Jean-Drapeau)", "Parc Jean-Drapeau (adresse n.d.)", "Tous âges",
  "Même tarif 2026 « un musée » que l'Insectarium", "Horaires n.d.", "https://espacepourlavie.ca/droits-dentree-pour-un-musee?mode=liste", None,
  "confirmé pour le prix", "", "", "st",
  [(None, "Biosphère, parc Jean-Drapeau, Montréal, QC", "nom")])
I(WEB, "Sortie / visite", "Zoo Ecomuseum", "Zoo extérieur de la faune du Québec", "21125 chemin Ste-Marie, Sainte-Anne-de-Bellevue (H9X 3Y7)",
  "Mini-explorateurs : visite autonome pour les jusqu'à 5 ans ; Camp nature 6-12 ans", "Prix d'entrée n.d. (non trouvé sur le site)",
  "Été 2026 : tous les jours 9 h-17 h ; hiver n.d.",
  "https://www.quebecvacances.com/fr/explorer/decouvrez-la-faune-du-quebec-au-seul-zoo-exterieur-a-montreal ; https://zooecomuseum.ca/workspace/uploads/files/camp-nature_zooecomuseum.pdf",
  None, VERIF, "Sur l'île de Montréal (ouest). Horaire été vient de Québec Vacances, tierce.", "", "ps",
  [(None, "21125 chemin Ste-Marie, Sainte-Anne-de-Bellevue, QC H9X 3Y7", "adresse")])
I(WEB, "Musée / expo", "Musée des beaux-arts de Montréal (MBAM)", "Musée d'art, ateliers famille", "1380 rue Sherbrooke O.", "Tous âges",
  "Collection permanente gratuite 0-20 ans (Time Out) ; Samedis matin en famille BMO gratuits 10 h-13 h (Narcity, janv. 2026)", "Ateliers les week-ends",
  "https://www.timeout.com/fr/montreal/que-faire/musees-gratuits-montreal ; https://www.narcity.com/fr/montreal/musees-montreal-gratuit-janvier-2026",
  None, VERIF, "Sources tierces ; confirmer sur le site du MBAM.", "enfants", "st",
  [(None, "1380 rue Sherbrooke O., Montréal, QC", "adresse")])
I(WEB, "Musée / expo", "Musée McCord Stewart", "Musée d'histoire", "690 rue Sherbrooke O.", "Tous âges",
  "Gratuit ≤ 12 ans et 13-17 ans (fondations DeSève et Rossy)", "Horaires n.d.",
  "https://www.musee-mccord-stewart.ca/app/uploads/2026/02/informations-pratique-musee-mccord-stewart_02272026.pdf", None, "confirmé (site officiel)",
  "Document février 2026.", "enfants", "st",
  [(None, "690 rue Sherbrooke O., Montréal, QC", "adresse")])
I(WEB, "Musée / expo", "Musée d'art contemporain (MAC)", "Musée d'art, « MAC en famille »", "Centre-ville (adresse n.d.)", "Tous âges",
  "Gratuit pour les moins de 18 ans", "Horaires n.d.", "https://www.mtl.org/fr/experience/musees-toute-famille-montreal", None, VERIF,
  "Source tierce (Tourisme Montréal).", "enfants", "st",
  [(None, "Musée d'art contemporain de Montréal, Montréal, QC", "nom")])
I(WEB, "Musée / expo", "Centre canadien d'architecture (CCA)", "Musée d'architecture", "1920 rue Baile",
  "Expo permanente non destinée aux moins de 8 ans (Narcity, 2024)", "Gratuit pour les 17 ans et moins (laissez-passer bibliothèque)", "Horaires n.d.",
  "https://montreal.ca/en/services/borrow-museum-pass-city-library", None, "confirmé pour la gratuité", "", "enfants", "s",
  [(None, "1920 rue Baile, Montréal, QC", "adresse")])
I(WEB, "Musée / expo", "Pointe-à-Callière", "Musée d'archéologie et d'histoire", "Vieux-Montréal", "Tous âges",
  "Tarifs enfants contradictoires entre sources (gratuit ≤ 17 ans vs 13 $ pour 13-17 ans et gratuit ≤ 4 ans)", "Mar.-ven. 10 h-17 h ; sam.-dim. 11 h-17 h",
  "https://pacmusee.qc.ca/en/plan-your-visit/hours-and-rates/ ; https://citiesinsider.com/country/canada/montreal/museums-and-art-galleries/fr",
  None, VERIF, "Horaires : site officiel ; prix à relire sur pacmusee.qc.ca.", "", "st",
  [(None, "Pointe-à-Callière, Montréal, QC", "nom")])
I(WEB, "Musée / expo", "Musée de l'Illusion Montréal", "Musée interactif", "Montréal (adresse n.d.)", "Gratuit 0-5 ans", "Tarif autres âges n.d.", "Horaires n.d.",
  "https://www.mtl.org/fr/experience/musees-toute-famille-montreal", None, VERIF, "Source tierce.", "", "ps",
  [(None, "Musée de l'Illusion, Montréal, QC", "nom")])
I(WEB, "Jeu extérieur", "Le Vélo des beaux-arts", "Ateliers de création en plein air", "Parcs et sites d'organismes (varie)", "Enfants de tous âges avec parents",
  "Gratuit", "Été", "https://montreal.ca/evenements/le-velo-des-beaux-arts-114135", None, "confirmé (site officiel)", "Saisonnier.", "oui", "p")
I(WEB, "Bibliothèque / piscine", "Empruntez un musée (laissez-passer de bibliothèque)", "Entrée gratuite dans plusieurs musées", "Bibliothèques de Montréal", "Familles",
  "Gratuit avec carte de bibliothèque ; pass valide 3 semaines (CCA, MAC, McCord Stewart, Écomusée du fier monde, MEM)", "Toute l'année",
  "https://montreal.ca/en/services/borrow-museum-pass-city-library", None, "confirmé (site officiel)", "Utile après l'obtention de la carte de bibliothèque.", "oui", "")

# ---------------------------------------------------------------- Parcs et plein air
PK = "parc"
def P(cat, arr, nom, typ, adr, comm, prix, saison, liens, statut, free="", tags="", markers=()):
    lieu = arr if adr == ND else (adr if arr.startswith("n.d.") else arr + " — " + adr)
    I(PK, cat, nom, typ, lieu, comm, prix, saison, liens, None, statut, "", free, tags, markers)

P("Plage", "n.d. (parc Jean-Drapeau)", "Plage Jean-Doré", "Plage avec baignade", "151 circuit Gilles-Villeneuve",
  "Grande zone de baignade ; accessible en métro", "Sources contradictoires (9 $ chez Narcity ; gratuit avant 17 h chez Culture Trip)", "Été ; horaires n.d.",
  "https://montreal.ca/articles/des-activites-dans-les-parcs-pour-profiter-de-la-nature-tout-lete-31981 ; https://www.narcity.com/fr/montreal/4-plages-qui-rouvrent-ce-mois-ci--montral-pour-profiter-de-lt",
  "à vérifier (prix)", markers=[(None, "151 circuit Gilles-Villeneuve, Montréal, QC", "adresse")])
P("Plage", "Pierrefonds-Roxboro (parc-nature)", "Plages du Cap-Saint-Jacques (2 plages)", "Plage avec baignade", "21115 boul. Gouin O. (H9K 1C7)",
  "Moins de 18 ans : test de nage ou veste de flottaison obligatoire ; baignade seulement en présence de sauveteurs ; location de kayak",
  "Entrée : 6,25 $ adulte, 4,50 $ enfant 6+ (Narcity, date n.d.) ; stationnement 9,50 $", "Ouvertes en saison ; ex. 10 h-19 h",
  "https://montreal.ca/lieux/plage-du-parc-nature-du-cap-saint-jacques ; https://montreal.ca/en/places/parc-nature-du-cap-saint-jacques-beachs",
  "confirmé (règles) ; prix à vérifier", tags="s", markers=[(None, "21115 boul. Gouin O., Montréal, QC H9K 1C7", "adresse")])
P("Plage", "Verdun", "Plage urbaine de Verdun", "Plage avec baignade", ND, "À quelques pas du métro", ND, "Été",
  "https://montreal.ca/articles/des-activites-dans-les-parcs-pour-profiter-de-la-nature-tout-lete-31981", "confirmé (existence)",
  markers=[(None, "Plage urbaine de Verdun, Montréal, QC", "nom")])
P("Plage", "Parc-nature du Bois-de-l'Île-Bizard", "Plage du Bois-de-l'Île-Bizard", "Petite plage ombragée", ND, "Idéale pour les jeunes enfants", ND, "Été",
  "https://montreal.ca/articles/des-activites-dans-les-parcs-pour-profiter-de-la-nature-tout-lete-31981", "confirmé (existence)", tags="p",
  markers=[(None, "Parc-nature du Bois-de-l'Île-Bizard, Montréal, QC", "nom")])
P("Plage", "Vieux-Port", "Plage de l'Horloge", "Plage sans baignade", "Vieux-Port, métro Champ-de-Mars", "Pas d'eau pour se baigner", "Entrée libre", "Été",
  "https://lepetitjournal.com/vivre-a-montreal/plage-montreal-363097 ; https://www.noovomoi.ca/voyager/plein-air/article.plages-proximite-montreal-a-decouvrir.1.1410196.html",
  "à vérifier (source tierce)", free="oui",
  markers=[(None, "Plage de l'Horloge, Vieux-Port, Montréal, QC", "nom")])
P("Plage", "Rivière-des-Prairies–Pointe-aux-Trembles", "Plage de l'Est", "Plage sans baignade, activités nautiques, jeux d'eau", "16240 rue Bureau (jeux d'eau)",
  "Jeux d'eau sur place", ND, "Été",
  "https://montreal.ca/articles/des-activites-dans-les-parcs-pour-profiter-de-la-nature-tout-lete-31981 ; https://montreal.ca/lieux?page=7",
  "confirmé (existence)", markers=[(None, "16240 rue Bureau, Montréal, QC", "adresse")])
P("Parc", "Le Plateau-Mont-Royal", "Parc La Fontaine", "Grand parc : aire de jeux, jeux d'eau, patinoire", "3819 av. Calixa-Lavallée",
  "40 hectares ; aire de jeux et pataugeoire ; patinoire en hiver", "Gratuit ; prêt de patins gratuit au chalet (pièce d'identité)",
  "Toute l'année ; pataugeoires fermées pour travaux (pôle famille), jeux d'eau activés",
  "https://montreal.ca/lieux/parc-la-fontaine ; https://montreal.ca/articles/se-rafraichir-cet-ete-dans-le-plateau", "confirmé (site officiel)",
  free="oui", tags="t", markers=[(None, "3819 av. Calixa-Lavallée, Montréal, QC", "adresse")])
P("Parc", "Villeray–Saint-Michel–Parc-Extension", "Parc Jarry", "Grand parc : pataugeoire, skate park, terrains", "205 rue Gary-Carter",
  "Pataugeoire, skate park, terrains de soccer", "Gratuit (n.d. pour la pataugeoire)", ND, "https://montreal.ca/en/places?page=14",
  "confirmé (existence)", markers=[(None, "205 rue Gary-Carter, Montréal, QC", "adresse")])
P("Parc", "Le Sud-Ouest", "Parc Angrignon", "Grand parc urbain", "3400 boul. des Trinitaires", "Détails des jeux n.d.", ND, ND,
  "https://montreal.ca/en/places?listType=map&page=6", "confirmé (adresse)", markers=[(None, "3400 boul. des Trinitaires, Montréal, QC", "adresse")])
P("Parc-nature", "Ahuntsic-Cartierville, Montréal-Nord (parc-nature)", "Parc-nature de l'Île-de-la-Visitation", "Parc-nature riverain, ruines de moulins, buttes de glissade",
  "2425 boul. Gouin E. (H2B 1X7)", "Famille, sentiers, belvédères, location d'équipement de plein air", ND, "Ouvert 7 h-22 h",
  "https://montreal.ca/en/places/parc-nature-de-lile-de-la-visitation ; https://montreal.ca/lieux/parc-nature-de-lile-de-la-visitation",
  "confirmé (site officiel)", markers=[(None, "2425 boul. Gouin E., Montréal, QC H2B 1X7", "adresse")])
P("Parc-nature", "Rivière-des-Prairies–Pointe-aux-Trembles (parc-nature)", "Parc-nature de la Pointe-aux-Prairies", "Parc-nature : marais, forêt, camping, soirée sous les étoiles",
  "14905 rue Sherbrooke E. (H1A 4G4)", "261 hectares ; 180 espèces d'oiseaux", ND, "Ouvert 7 h-22 h",
  "https://montreal.ca/en/places/parc-nature-de-la-pointe-aux-prairies ; https://www.mtl.org/en/activities/parc-nature-de-la-pointe-aux-prairies",
  "confirmé (site officiel)", markers=[(None, "14905 rue Sherbrooke E., Montréal, QC H1A 4G4", "adresse")])
P("Parc-nature", "Ahuntsic-Cartierville, Pierrefonds-Roxboro, Saint-Laurent (parc-nature)", "Parc-nature du Bois-de-Liesse", "Parc-nature, stations d'observation, buttes de glissade",
  "9432 boul. Gouin O.", "Famille", ND, ND, "https://montreal.ca/lieux/parc-nature-du-bois-de-liesse ; https://montreal.ca/en/places?listType=map&page=18",
  "confirmé (site officiel)", markers=[(None, "9432 boul. Gouin O., Montréal, QC", "adresse")])
P("Parc-nature", "Divers (parcs-nature)", "Autres parcs-nature : Anse-à-l'Orme, Bois-de-Saraguay, Ruisseau-De Montigny", "Parcs-nature",
  "21134 boul. Gouin O. (Pierrefonds-Roxboro) ; 12200 av. Joseph-Saucier (Ahuntsic-Cartierville) ; 7123 boul. Maurice-Duplessis (RDP–PAT)",
  ND, ND, ND, "https://montreal.ca/en/places?page=18", "confirmé (adresses)",
  markers=[("Anse-à-l'Orme", "21134 boul. Gouin O., Montréal, QC", "adresse"), ("Bois-de-Saraguay", "12200 av. Joseph-Saucier, Montréal, QC", "adresse"),
           ("Ruisseau-De Montigny", "7123 boul. Maurice-Duplessis, Montréal, QC", "adresse")])
P("Parc", "Anjou", "Parc Goncourt", "Parc de quartier : 2 aires de jeux, butte de glissade", "Anjou (adresse n.d.)",
  "Aires de jeux moins de 5 ans et plus de 5 ans ; module tout-petits", "Gratuit", "Butte de glissade en hiver", "https://montreal.ca/lieux/parc-goncourt",
  "confirmé (site officiel)", free="oui", tags="ps", markers=[(None, "Parc Goncourt, Anjou, Montréal, QC", "nom")])
P("Parc", "Rivière-des-Prairies–Pointe-aux-Trembles", "Parc Jeanne-Lapierre", "Parc de quartier, rénové en 2022", "Pointe-aux-Trembles (adresse n.d.)",
  "Aire de jeux combinée 2-12 ans, balançoires bébé, nid de coco, mini-soccer", "Gratuit", ND, "https://montreal.ca/lieux/parc-jeanne-lapierre",
  "confirmé (site officiel)", free="oui", tags="ps", markers=[(None, "Parc Jeanne-Lapierre, Pointe-aux-Trembles, Montréal, QC", "nom")])
P("Parc", "n.d.", "Parc Giuseppe-Garibaldi", "Aire de jeux universelle (6-12 ans)", ND, "Aire accessible universellement pour 6-12 ans", "Gratuit", ND,
  "https://montreal.ca/actualites/de-nouvelles-installations-de-jeu-au-parc-giuseppe-garibaldi-112565", "confirmé (site officiel)", free="oui", tags="s")

# Jeux d'eau : un repère par adresse citée (les noms de parcs ne sont pas appariés aux adresses dans la source).
def JE(arr, nom, typ, adr, prix, saison, liens, adresses, free=""):
    P("Jeux d'eau", arr, nom, typ, adr, "Enfants", prix, saison, liens, "confirmé (adresses)", free=free,
      markers=[("adresse %d" % (i + 1), a + ", Montréal, QC", "adresse") for i, a in enumerate(adresses)])

JE("Le Plateau-Mont-Royal", "Jeux d'eau : Alphonse-Télesphore-Lépine, Baldwin, La Fontaine, Lhasa-De Sela", "Jeux d'eau",
   "5155 av. de Gaspé ; 4355 rue Fullum ; 3819 av. Calixa-Lavallée", "Gratuit", "Tous les jours de mai à octobre",
   "https://montreal.ca/articles/se-rafraichir-cet-ete-dans-le-plateau ; https://montreal.ca/lieux?page=8",
   ["5155 av. de Gaspé", "4355 rue Fullum", "3819 av. Calixa-Lavallée"], free="oui")
JE("Mercier–Hochelaga-Maisonneuve", "Jeux d'eau : Beauclerk, Lalancette, Liébert, Morgan, Pierre-Tétreault", "Jeux d'eau",
   "1855 av. Émile-Legrand ; 2315 rue Nicolet ; 2848 rue Liébert ; 4370 rue Sainte-Catherine E. ; 383 rue Baldwin", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=7 ; https://montreal.ca/lieux?listType=map&page=8",
   ["1855 av. Émile-Legrand", "2315 rue Nicolet", "2848 rue Liébert", "4370 rue Sainte-Catherine E.", "383 rue Baldwin"])
JE("Villeray–Saint-Michel–Parc-Extension", "Jeux d'eau : Bélair, De Lestre ; pataugeoire du parc de Turin", "Jeux d'eau, pataugeoire",
   "7035 2e Av. ; 8001 av. Bloomfield ; 7205 rue Chambord", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=7 ; https://montreal.ca/lieux?listType=map&page=20",
   ["7035 2e Av.", "8001 av. Bloomfield", "7205 rue Chambord"])
JE("Ahuntsic-Cartierville", "Jeux d'eau : Ahuntsic, Avila-Vidal, De Mésy, Henri-Julien", "Jeux d'eau",
   "10555 rue Lajeunesse ; 11565 rue Jean-Massé ; 12120 rue Grenet ; 9300 rue Saint-Denis", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=7",
   ["10555 rue Lajeunesse", "11565 rue Jean-Massé", "12120 rue Grenet", "9300 rue Saint-Denis"])
JE("Montréal-Nord", "Jeux d'eau : Aimé-Léonard, Henri-Bourassa, Le Carignan, Maurice-Bélanger, Ménard, Monty, Ottawa", "Jeux d'eau, pataugeoires",
   "Ex. 4975 boul. Gouin E. ; 6100 rue Pascal ; 11481 av. P.-M.-Favier", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=7 ; https://montreal.ca/lieux?page=8",
   ["4975 boul. Gouin E.", "6100 rue Pascal", "11481 av. P.-M.-Favier"])
JE("LaSalle", "Jeux d'eau : Boivin, Dalmany, Hayward, Lawrence, Ménard, Ouellette, Leroux, Père-Marquette", "Jeux d'eau",
   "Ex. 9650 rue Dalmany ; 9640 rue Clément ; 1407 rue Serre", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?page=7 ; https://montreal.ca/lieux?listType=map&page=8",
   ["9650 rue Dalmany", "9640 rue Clément", "1407 rue Serre"])
JE("Verdun", "Jeux d'eau : Joannette, Maynard-Ferguson, Monseigneur-J.-A.-Richard, de l'Épervière, Orée-du-Fleuve, Reine-Élizabeth", "Jeux d'eau",
   "Ex. 292 rue Hickson ; 44 rue Claude-Vivier ; 5150 boul. LaSalle", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=8 ; https://montreal.ca/lieux?page=7",
   ["292 rue Hickson", "44 rue Claude-Vivier", "5150 boul. LaSalle"])
JE("Le Sud-Ouest", "Jeux d'eau : Curé-Albert-Arnold, Joe-Beef, Le Ber, Oscar-Peterson, Campbell Ouest", "Jeux d'eau, pataugeoire Saint-Gabriel",
   "6855 rue Hamilton ; 2491 rue Centre ; 202 av. Ash ; 810 rue Chatham ; 1990 rue de Maricourt", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=7 ; https://montreal.ca/lieux?listType=map&page=8",
   ["6855 rue Hamilton", "2491 rue Centre", "202 av. Ash", "810 rue Chatham", "1990 rue de Maricourt"])
JE("Côte-des-Neiges–Notre-Dame-de-Grâce", "Jeux d'eau : Martin-Luther-King, Notre-Dame-de-Grâce, de la Savane ; pataugeoire Trenholme", "Jeux d'eau, pataugeoire",
   "3453 av. Kent ; 3500 av. Girouard ; 5111 rue Paré ; 6800 rue Sherbrooke O.", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?page=8 ; https://montreal.ca/lieux?page=20",
   ["3453 av. Kent", "3500 av. Girouard", "5111 rue Paré", "6800 rue Sherbrooke O."])
JE("Saint-Laurent", "Jeux d'eau : Beaulac, Decelles, Hartenstein, Painter ; pataugeoire Saint-Laurent", "Jeux d'eau, pataugeoire",
   "1145 rue Elizabeth ; 845 rue Roy ; 1505 rue Cardinal ; 260 rue Marcotte", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=7 ; https://montreal.ca/lieux?listType=map&page=8",
   ["1145 rue Elizabeth", "845 rue Roy", "1505 rue Cardinal", "260 rue Marcotte"])
JE("Saint-Léonard", "Jeux d'eau : Coubertin, Delorme", "Jeux d'eau", "4755 rue Valéry ; 6060 rue de Honfleur", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=7", ["4755 rue Valéry", "6060 rue de Honfleur"])
JE("Pierrefonds-Roxboro / L'Île-Bizard–Sainte-Geneviève", "Jeux d'eau : Cyril-W.-McDonald, de Deauville, Parkinson ; Jonathan-Wilson (Île-Bizard)", "Jeux d'eau",
   "Ex. 3243 boul. Chèvremont (Jonathan-Wilson)", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=7 ; https://montreal.ca/lieux?listType=map&page=8", ["3243 boul. Chèvremont"])
JE("Rosemont–La Petite-Patrie, Outremont, Lachine, Anjou", "Jeux d'eau : Montcalm ; Beaubien-Outremont ; parc LaSalle (Lachine) ; de Talcy (Anjou)", "Jeux d'eau",
   "6855 av. Papineau ; 461 ch. de la Côte-Sainte-Catherine ; 10661 rue Victoria ; 8151 av. de Talcy", ND, "Été (dates n.d.)",
   "https://montreal.ca/lieux?listType=map&page=8 ; https://montreal.ca/lieux?page=7",
   ["6855 av. Papineau", "461 ch. de la Côte-Sainte-Catherine", "10661 rue Victoria", "8151 av. de Talcy"])
