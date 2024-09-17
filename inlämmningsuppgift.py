#!/usr/bin/env python
def beräkna_näringsbehov(proteinmål, kalorimål, fettmål, måltid):
    protein_ätit = 0
    kalorier_ätit = 0
    fett_ätit = 0

    for rätt in måltid:
        protein_ätit += rätt['protein']
        kalorier_ätit += rätt['kalorier']
        fett_ätit += rätt['fett']

    protein_kvar = proteinmål - protein_ätit
    kalorier_kvar = kalorimål - kalorier_ätit
    fett_kvar = fettmål - fett_ätit

    return protein_kvar, kalorier_kvar, fett_kvar

def lägg_till_maträtt():
    namn = input("Vad heter maträtten? ")
    protein = float(input(f"Hur mycket protein finns i {namn} (gram)? "))
    kalorier = float(input(f"Hur mycket kalorier finns i {namn}? "))
    fett = float(input(f"Hur mycket fett finns i {namn} (gram)? "))
    
    return {'namn': namn, 'protein': protein, 'kalorier': kalorier, 'fett': fett}

def huvudprogram():
    print("Välkommen till din näringsplanerare!")
    
    proteinmål = float(input("Hur mycket protein vill du äta idag (gram)? "))
    kalorimål = float(input("Hur många kalorier vill du äta idag? "))
    fettmål = float(input("Hur mycket fett vill du äta idag (gram)? "))
    
    maträtter = [
        {'namn': 'Kycklingfilé', 'protein': 31, 'kalorier': 165, 'fett': 3.6},
        {'namn': 'Ägg', 'protein': 13, 'kalorier': 155, 'fett': 11},
        {'namn': 'Avokado', 'protein': 2, 'kalorier': 160, 'fett': 15},
    ]
    
    måltid = []

    while True:
        val = input("Vill du lägga in en maträtt från listan (l), lägga till en ny maträtt (n), eller avsluta (a)? ").lower()

        if val == 'l':
            print("\nTillgängliga maträtter:")
            for i, rätt in enumerate(maträtter):
                print(f"{i+1}. {rätt['namn']} (Protein: {rätt['protein']}g, Kalorier: {rätt['kalorier']}, Fett: {rätt['fett']}g)")

            maträtt_val = int(input("Ange numret på maträtten du vill lägga till: ")) - 1
            måltid.append(maträtter[maträtt_val])
            print(f"{maträtter[maträtt_val]['namn']} har lagts till i din måltid.\n")

        elif val == 'n':
            ny_rätt = lägg_till_maträtt()
            måltid.append(ny_rätt)
            print(f"{ny_rätt['namn']} har lagts till i din måltid.\n")
        
        elif val == 'a':
            break

        else:
            print("Ogiltigt val. Välj 'l', 'n' eller 'a'.")

    protein_kvar, kalorier_kvar, fett_kvar = beräkna_näringsbehov(proteinmål, kalorimål, fettmål, måltid)
    
    print("\nResultat:")
    print(f"Du har kvar att äta {protein_kvar:.2f}g protein, {kalorier_kvar:.2f} kalorier och {fett_kvar:.2f}g fett.")
    print("Lycka till med dina mål!")

huvudprogram()
