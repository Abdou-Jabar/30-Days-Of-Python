print("=" * 50)
print("Calculataeur de trajet")
print("=" * 50)
print()

continuer = "oui"

historique = []

while continuer.lower() == "oui" or continuer.lower() == "o":
    print("\n--- Nouveau trajet ---")
    
    print("\nMoyens de transport disponibles:")
    print("1. Zemidjan (Taxi-moto)")
    print("2. Taxi (Voiture)")
    
    choix = input("\nMoyen de transport (1 ou 2): ")
    
    if choix == "1":
        moyen_transport = "Zemidjan"
        tarif_base = 150
        prix_km = 75
        majoration = 0.15
    elif choix == "2":
        moyen_transport = "Taxi"
        tarif_base = 200
        prix_km = 100
        majoration = 0.25
    else:
        print("Choix invalide, Recommencer.")
        continue
    
    distance = input("\nDistance du trajet (en km) ? ")
    distance = float(distance)
    
    print("\nHeure de Trajet ?")
    heure_input = input("Entrez l'heure (format: 7.5 pour 7h30, 14 pour 14h00): ")
    heure = float(heure_input)
    
    prix_total = tarif_base + (prix_km * distance)
    
    heure_pointe = False
    
    if heure >= 7.0 and heure <= 8.75:
        heure_pointe = True
    elif heure >= 11.75 and heure <= 13.0:
        heure_pointe = True
    elif heure >= 17.0 and heure <= 19.0:
        heure_pointe = True
    
    if heure_pointe:
        prix_total = prix_total * (1 + majoration)
    
    prix_arrondi = round(prix_total / 25) * 25
    
    print("\n" + "=" * 50)
    print("Récapitulatif du trajet")
    print("=" * 50)
    print(f"Moyen de transport: {moyen_transport}")
    print(f"Distance: {distance} km")
    
    heure_entiere = int(heure)
    minutes = int((heure - heure_entiere) * 60)
    print(f"Heure du trajet: {heure_entiere}h{minutes:02d}")
    
    if heure_pointe:
        print("Heure de pointe: OUI")
        print(f"Majoration: +{int(majoration * 100)}%")
    else:
        print("Heure de pointe: NON")
    
    print("-" * 50)
    print(f"PRIX TOTAL: {prix_arrondi} FCFA")
    print("=" * 50)
    
    info_trajet = f"{moyen_transport} - {distance}km - {prix_arrondi} FCFA"
    historique.append(info_trajet)
    
    print()
    continuer = input("Un autre trajet? (oui/non): ")

if len(historique) > 0:
    print("\n" + "=" * 50)
    print("HISTORIQUE")
    print("=" * 50)
    numero = 1
    for trajet in historique:
        print(f"{numero}. {trajet}")
        numero = numero + 1
    print("=" * 50)

print(f"EYIZANDé")