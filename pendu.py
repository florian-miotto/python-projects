import random

# Fonction qui lit le dictionnaire et renvoie un mot aléatoire
def choisir_mot():
    with open("dico_france.txt", "r") as f:
        mots = f.readlines()
    return random.choice(mots).strip()

# Fonction qui affiche le mot en masquant les lettres non trouvées
def afficher_mot(mot, lettres_trouvees):
    for lettre in mot:
        if lettre in lettres_trouvees:
            print(lettre, end=" ")
        else:
            print("_", end=" ")
    print("\n")


# Fonction qui gère une tentative du joueur
def jouer_tour(mot, lettres_proposees, lettres_trouvees, vies_restantes):
    print("Il vous reste", vies_restantes, "vies")
    print("Lettres proposées :", ", ".join(sorted(list(lettres_proposees))))
    afficher_mot(mot, lettres_trouvees)
    proposition = input("Proposez une lettre : ").lower()
    if len(proposition) != 1:
        print("Vous devez proposer une seule lettre")
        return vies_restantes
    lettres_proposees.add(proposition)
    if proposition in mot:
        lettres_trouvees.add(proposition)
        print("Bonne réponse !")
    else:
        vies_restantes -= 1
        print("Mauvaise réponse...")
    return vies_restantes

# Fonction principale qui gère le déroulement de la partie
def jouer():
    niveaux = {
        "débutant": 10,
        "intermédiaire": 7,
        "expert": 4
    }
    niveau = input("Choisissez un niveau (débutant, intermédiaire ou expert) : ").lower()
    if niveau not in niveaux:
        print("Niveau invalide, choisissez parmi débutant, intermédiaire ou expert")
        return
    vies_restantes = niveaux[niveau]
    mot = choisir_mot()
    lettres_proposees = set()
    lettres_trouvees = set()
    while vies_restantes > 0 and len(lettres_trouvees) < len(set(mot)):
        vies_restantes = jouer_tour(mot, lettres_proposees, lettres_trouvees, vies_restantes)
    if len(lettres_trouvees) == len(set(mot)):
        print("Bravo, vous avez gagné ! Le mot était :", mot)
    else:
        print("Perdu... Le mot était :", mot)

# Lancer le jeu
jouer()
