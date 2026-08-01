# PyCon Togo 2026 - Projet Final du Challenge 30 Days of Python

> Document destiné aux participants du challenge 2026. À traiter comme un vrai exercice technique, dans les mêmes conditions qu'un test lors d'un entretien d'embauche.

**Deadline : 20 août 2026, 23h59 (heure de Lomé, GMT).** Seul le dernier commit reçu avant cette date/heure sera pris en compte.

---

## 1. Introduction

Ce document décrit le **projet final** du challenge 30 Days of Python 2026, organisé par **Python Software Community Togo** en partenariat avec **Fata**.

Contrairement aux modules d'apprentissage réalisés sur l'application Fata, ce projet est un **exercice indépendant**, à réaliser en dehors de l'app.

**Objectif :** produire un travail concret, fonctionnel et bien documenté que tu pourras ajouter à ton portfolio (GitHub, CV, LinkedIn) et présenter fièrement - à un recruteur, un client ou un jury.

---

## 2. Règles générales

- **Un seul exercice est obligatoire**, le second est **optionnel**, à réaliser selon ton niveau et ton envie d'apprentissage. Il n'est pas noté au même titre, cependant c'est un bonus sur la notation globale, mais c'est un vrai plus pour ton portfolio.
- **Aucune utilisation d'IA Agent/générative ou autres** (ChatGPT, Copilot, Claude, etc.) n'est autorisée pour ces projets. L'objectif est d'évaluer et de renforcer **tes propres compétences**.
- **On ne triche pas son prochain.** Chaque participant écrit et soumet son propre code. Copier le travail d'un autre participant (ou le laisser copier) est considéré comme une fraude et entraîne la disqualification des deux parties.
- Le code doit être écrit en **Python pur**, exécutable dans un terminal, sans dépendance externe complexe (sauf mention contraire dans le bonus du Projet 2).
- **Deadline : 20 août 2026, 23h59.** Aucune soumission après cette date ne sera acceptée.

---

## 3. Modalités de soumission

Voir le fichier [`SUBMISSION.md`](./SUBMISSION.md) pour la marche à suivre complète et le format exact à respecter.

Résumé rapide :
1. Fork ce dépôt.
2. Crée ton projet dans un dépôt GitHub personnel.
3. Ajoute un `README.md` à **ton** projet (nom, comment le lancer, capture d'écran/exemple).
4. Ajoute ta ligne dans [`SUBMISSION.md`](./SUBMISSION.md) de ce dépôt (prénom, username Fata, lien GitHub).
5. Ouvre une Pull Request avant le **20 août 2026, 23h59**.

---

## 4. Projet 1 - Calculateur de Trajet Zemidjan/Taxi

**Statut : OBLIGATOIRE - pour tous les niveaux**

### 4.1 Contexte

À Lomé, deux moyens de transport très utilisés sont le **zemidjan** (taxi-moto) et le **taxi** (voiture). Chacun a son propre tarif de base et son propre prix au kilomètre, avec une majoration aux heures de pointe.

**Ton projet :** construire un programme qui calcule le prix d'un trajet selon le moyen de transport choisi.

### 4.2 Fonctionnalités attendues

1. Demander à l'utilisateur de choisir le moyen de transport : zemidjan (taxi-moto) ou taxi (voiture).
2. Demander la distance du trajet, en kilomètres.
3. Demander l'heure du trajet.
4. Calculer le prix : `prix_total = tarif_de_base + (prix_au_km × distance)`.
5. Si l'heure correspond à une plage d'heure de pointe, appliquer la majoration correspondante **sur le prix total**.
6. Afficher un récapitulatif clair (moyen de transport, distance, heure de pointe ou non, prix final), be creative.
7. Permettre de calculer plusieurs trajets à la suite, jusqu'à ce que l'utilisateur quitte le programme.

### 4.3 Paramètres officiels

| Paramètre | Zemidjan (Taxi-moto) | Taxi (Voiture) |
|---|---|---|
| Tarif de base | 150 FCFA | 200 FCFA |
| Prix au km | 75 FCFA / km | 100 FCFA / km |
| Majoration heure de pointe | +15% sur le prix total | +25% sur le prix total |

**Plages horaires d'heure de pointe** (identiques pour les deux moyens de transport) :
- 07h00 - 08h45 (matin)
- 11h45 - 13h00 (pause déjeuner)
- 17h00 - 19h00 (soir)

> ⚠️ **Règle de calcul :** la majoration s'applique sur le **prix total** du trajet (tarif de base + prix au km × distance), jamais sur une composante isolée.

**Exemple :** trajet en zemidjan de 5 km à 07h30 (heure de pointe)
→ prix de base = 150 + (75 × 5) = 525 FCFA
→ avec majoration 15% = 525 × 1.15 = **603,75 FCFA**

### 4.4 Bonus (optionnel)

- Arrondir le prix final à un montant réaliste (ex. au multiple de 25 FCFA le plus proche).
- Garder un historique des trajets calculés pendant la session.
- Détecter automatiquement l'heure de pointe à partir de l'heure système (module `datetime`).

### 4.5 Ressources

- `input()` renvoie toujours du texte - utiliser `float()` pour les distances et convertir l'heure en nombre décimal pour la comparaison.
- Pour augmenter un prix de 15% : `prix × 1.15` (pas d'addition directe de "15").
- Comparaison d'intervalles horaires : convertir l'heure en décimal (ex. 7h30 → 7.5) puis comparer avec les bornes.
- Module `datetime` (bonus) : https://docs.python.org/3/library/datetime.html

---

## 5. Projet 2 - Simulateur de Change FCFA / Devises

**Statut : OPTIONNEL - recommandé niveau intermédiaire/avancé**

### 5.1 Contexte

Le FCFA (XOF) se convertit quotidiennement vers d'autres devises pour le commerce, les études à l'étranger, ou les transferts d'argent.

**Ton projet :** construire un simulateur de change qui convertit le FCFA vers plusieurs devises, applique des frais de change, et garde un historique.

### 5.2 Fonctionnalités attendues

1. Menu pour choisir une devise de destination parmi : EUR, USD, CAD, CHF, NGN, CNY, GHS.
2. Demander le montant en FCFA à convertir.
3. Calculer la conversion selon les taux fournis ci-dessous.
4. Appliquer des frais de change de **1%**, et afficher le montant net reçu.
5. Garder un historique des conversions effectuées pendant la session.
6. Afficher l'historique complet à la demande.
7. Quitter proprement le programme.

### 5.3 Taux de change officiels

> Taux fixes (snapshot), à coder en dur pour la version de base - ne varient pas en temps réel.

| Devise | Code | 1 unité = |
|---|---|---|
| Euro | EUR | 655,96 FCFA |
| Dollar américain | USD | 558,26 FCFA |
| Dollar canadien | CAD | 407,60 FCFA |
| Franc suisse | CHF | 707,49 FCFA |
| Naira nigérian | NGN | 0,3655 FCFA |
| Yuan chinois | CNY | 77,88 FCFA |
| Cedi ghanéen | GHS | 53,52 FCFA |

**Exemple :** convertir 50 000 FCFA en EUR → 50 000 ÷ 655,96 ≈ 76,23 EUR. Avec 1% de frais : 76,23 × 0,99 ≈ **75,47 EUR net reçu**.

### 5.4 Bonus (optionnel, pour aller plus loin)

- **Utilisation réseau :** au lieu de taux fixes, récupérer les taux en direct avec le module `requests` depuis l'API publique et gratuite : https://raw.githubusercontent.com/ismartcoding/currency-api/main/latest/data.json (donne le taux de chaque devise pour 1 USD - il faut calculer le taux FCFA/devise à partir de ces valeurs).
- **Développement web :** transformer le simulateur en petite application web (ex. avec FastAPI/Flask) plutôt qu'un programme en ligne de commande.
- Le programme de base (sans bonus) doit fonctionner entièrement en local, sans connexion réseau.

### 5.5 Ressources

- Dictionnaires Python : https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- Notion de taux de change et de frais de change : un taux de change indique combien d'unités d'une devise sont nécessaires pour obtenir une unité d'une autre. Des frais de change réduisent le montant final reçu.
- Module `requests` (bonus réseau) : https://requests.readthedocs.io/en/latest/
- Flask (bonus web) : https://flask.palletsprojects.com/

**Bases générales**
- Dictionnaires Python : https://docs.python.org/3/tutorial/datastructures.html#dictionaries
- Module `requests` (bonus réseau), méthode `.json()` : https://requests.readthedocs.io/en/latest/

**Vidéos - FastAPI**
- [Créez une API Python en 10 minutes avec FastAPI (Le Guide Rapide)](https://www.youtube.com/watch?v=b_pYyoZsTUY) - FR, rapide et concret
- [Créer des API en Python avec FastAPI en seulement 2H](https://www.youtube.com/watch?v=7D_0JTeaKWg) - FR, plus complet
- [FastAPI Tutorial for Beginners – Full Course](https://www.youtube.com/watch?v=VirndPTeRaw) - EN, cours complet pour aller plus loin

**Blogs/Docs FastAPI**
- Documentation officielle (tutoriel pas à pas) : https://fastapi.tiangolo.com/tutorial/

**Vidéos Flask**
- [Flask pour Python : Introduction en 10min au framework web](https://www.youtube.com/watch?v=rGn9XvODhOs) - FR, récent et clair
- [Tutoriel Flask (Français) - Découverte du micro-framework Web Python](https://www.youtube.com/watch?v=ajrfDEi8F7Y) - FR, bases

** Blogs/Docs - Flask & Jinja**
- Documentation Flask en français : https://flask-fr.readthedocs.io/templating/
- Introduction à Jinja2 (blog, très pédagogique, avec exemples) : https://codewithmpia.com/courses/apprendre-flask-le-guide-ultime/introduction-a-jinja2
- Jinja2 en français (tutoriel pas à pas avec code) : https://learntutorials.net/fr/jinja2/topic/10025/demarrer-avec-jinja2

---

## 6. Grille d'évaluation indicative

| Critère | Poids |
|---|---|
| Fonctionnalité complète et correcte | 40% |
| Qualité du code (structure, fonctions, noms clairs) | 25% |
| Gestion des erreurs (try/except sur les saisies) | 15% |
| Documentation (README clair et complet) | 10% |
| Bonus / créativité | 10% |

---

## 7. Rappel important

- Un seul exercice est obligatoire (Projet 1). Le Projet 2 est un bonus qui valorise ton profil.
- Aucune utilisation d'IA générative n'est autorisée.
- On ne triche pas son prochain - chaque soumission doit être un travail personnel.
- **Deadline : 20 août 2026, 23h59 GMT.**
- Traite ce travail comme un véritable exercice technique de recrutement.

---

*Python Software Community Togo × Fata - PyCon Togo 2026*