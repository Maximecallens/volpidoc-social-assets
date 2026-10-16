# Guide éditorial Volpidoc — réseaux sociaux

À lire avant chaque post. Rédigé à partir des décisions de Maxime (oct. 2026).

## Objectif
Amener le lecteur à visiter volpidoc.com, créer un compte, se connecter, puis passer à l'abonnement payant.
Premier point d'entrée : le calculateur de ROI (`https://www.volpidoc.com/calculateur-roi`), qui demande un simple email.
Toujours ajouter le suivi : `?utm_source=<linkedin|x>&utm_medium=social&utm_campaign=<série>&utm_content=<post_id>-<slug>`.
Pas de code promo pour l'instant.

## Voix
- La figure principale est **Julien** (Julien Favereaux). Les posts LinkedIn sont écrits à la première personne (« je ») et signés « Julien ».
- Vouvoiement du lecteur. Ton direct, utile, un peu provocant dans l'accroche, jamais racoleur.
- Volpi = l'agent IA de Volpidoc. Posture de **copilote** : « Volpi ne décide pas à votre place, il rend visible ce que vous ne lisez pas. » Ne jamais parler de « conseiller » (Volpidoc n'est ni courtier ni conseil juridique).

## Structure qui marche (inspirée de la newsletter « L'angle mort »)
Accroche forte (une phrase) → le problème vu comme un angle mort structurel → 3 signes reconnaissables → une scène type (présentée comme un scénario classique, jamais comme un vrai client) → un cadeau concret (questions, checklist, méthode utilisable sans Volpidoc) → le lien naturel avec Volpi → appel à l'action vers le calculateur.

## Cibles
Indépendants et professions libérales, TPE, PME sans direction juridique. Secteurs à faire tourner : BTP, médical / santé libérale, conseil, commerce.

## Thèmes
Gestion contractuelle, assurance (multirisque, RC pro, flotte, prévoyance…), contrats fournisseurs (télécom, énergie, logiciels, maintenance, leasing), comparaison de devis, clauses (préavis, tacite reconduction, indexation, franchises, plafonds, exclusions, doublons), échéances et résiliation.
Mettre en avant ce que Volpidoc fait gagner : du temps, de l'argent, de vraies informations, un support humain (réponse sous 48 h par email), quelqu'un à vos côtés.

## Faits autorisés (vérifier sur le site avant d'en citer un autre)
- Volpi lit chaque contrat importé (PDF, Word, scan) : résumé, clauses clés, préavis, risques, en moins de 30 secondes ; Score Volpi sur 100.
- Audit IA de couverture (persona entreprise via le SIREN, double radar assurance / fournisseurs), détection des doublons.
- Comparateur : jusqu'à 5 devis **importés** face à un contrat de référence, verdict IA et économies estimées.
- Échéances : lanes de statut, export .ics, lettre de résiliation **pré-remplie** (l'envoi reste à faire par l'utilisateur).
- Chat « Demander à Volpi » avec citations des documents.
- Données hébergées en Europe, RGPD, documents jamais utilisés pour entraîner des modèles.
- Tarifs HT : Essentiel 29 €/mois, Premium 49 €/mois, Ultra 89 €/mois ; annuel avec 2 mois offerts ; essai gratuit 14 jours (carte bancaire demandée, aucun prélèvement pendant l'essai).
- Gain estimé : 6 000 à 15 000 € par an sur un portefeuille de 30 à 80 contrats (toujours préciser « retours d'usage »).
- Clients dont le logo est sur le site (3ème Cercle, Step44, Léman Maturité, Virtech Sensor…) : citables par leur nom, sans inventer de chiffres ni de citation. Ne jamais citer EvoTattoo (règle MedMax ci-dessous).

## Interdits
- Ne jamais dire que Volpidoc cherche des offres sur le marché : il compare des documents importés entre eux.
- Pas de cas client chiffré inventé, pas de faux témoignage, pas de statistique d'utilisateurs inventée.
- Pas d'affirmation juridique absolue : un préavis « souvent » de 2 mois, une reconduction « souvent » annuelle.
- Ne pas mentionner la fonction multi-organisation (volontairement non promue).
- Volpidoc est une société distincte de MedMax : aucun lien, aucune mention d'EvoTattoo, Tattoomorrow ou medmax.fr.

## Formats
- LinkedIn (2 par semaine, mardi et jeudi 9 h) : 1 200 à 2 000 caractères, lien direct dans le post, 3 hashtags maximum, signé « Julien ». En général mardi = image 1080×1350, jeudi = carrousel PDF de 5 à 8 pages 1080×1350.
- X (2 par semaine, mercredi et vendredi 12 h) : 280 caractères maximum (un lien compte 23), image 1600×900, pas de hashtag ou un seul.
- Visuels : charte claire (fond blanc → turquoise très pâle, texte bleu marine #003046, accents #0094B6, orange #F15A24 avec parcimonie), police Plus Jakarta Sans, logo couleur, renard en filigrane. Pas de fond sombre (demande de Maxime). Générateur de référence : `tools/render_semaine1.py`.
- Avant publication : passer le texte LinkedIn dans `tools/li_text.py` (sinon LinkedIn tronque le texte aux parenthèses).

## Réseaux actifs (14 oct. 2026)
- LinkedIn (page Volpidoc) et Facebook (page Volpidoc) : mardi et jeudi 9 h, même texte (Facebook reçoit l'image, ou la 1re page du carrousel).
- X (@volpidoc) : mercredi et vendredi 12 h.
- YouTube (@Volpidoc) Short + Reel Facebook : lundi 12 h.
- Instagram (@volpidoc_france) : **actif** depuis le 14/10/2026 (compte validé par Meta et relié à la page Facebook Volpidoc). Les Shorts y sont publiés en Reel : passer "publier_instagram": "oui".

## Motion designs (Shorts) — fonctionnement depuis le 16 oct. 2026
- Les vidéos sont réalisées par le développeur, d'après le planning « Volpidoc - Planning motion design.xlsx » à la racine du drive partagé Google Volpidoc (copie de référence : planning/planning-motion-design.xlsx, généré par planning/build_planning.py).
- Nom de fichier attendu : VD_SH_NN_AAAA-MM-JJ.mp4 (date = lundi de publication) ; corrections : _v2, _v3… Dépôt au plus tard le vendredi 18 h.
- Samedi (tâche « motion designs du dev ») : transfert Drive → inbox/ via le scénario Make 7970983, contrôle forme + textes du planning, programmation (plan_<lundi>_short « prêt ») ou prompt de correction pour le développeur. Vidéos hors planning : mises en réserve, utilisées seulement si la vidéo prévue manque.
- Lundi : publication seulement si le plan est « prêt ». Claude ne fabrique plus de Short lui-même.
- Ressources pour le développeur : brand/logos/, brand/fonts/, posts/short-01_preavis/ (vidéo de référence et gabarit motion.html).
