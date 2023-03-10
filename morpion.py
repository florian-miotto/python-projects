# Écrivez un programme morpion.py, qui permet à l’utilisateur de faire une partie à 2
# joueurs du célèbre jeu le morpion dans le terminal.

# Le programme devra dans un premier temps demander si on souhaite jouer ou voir les
# scores. Puis, il demandera aux deux joueurs de renseigner leur ursername. Il affichera
# ensuite la map uniquement remplie de “-”.

# Le programme demandera au premier joueur, les croix, de rentrer en input une ligne et
# une colonne, où il souhaite jouer.
# Le programme ré affichera la map, avec une croix là où le joueur a choisi.
# C’est au tour des ronds de jouer, et ainsi de suite.

# Une fois la partie finie, le programme devra écrire dans un fichier score.txt les username,
# et leur nombre de victoires. Si le username du gagnant existe déjà, il devra incrémenter
# son nombre de victoires de 1. Sinon, il ajoutera à la fin du fichier son username, avec
# une victoire.


#affichage de la map
def affichage(map,joueur):
    print("Tour du joueur", joueur)
    print(" __________________________")
    print("|OFFo oON                  |")
    print("| .----------------------. |")
    print("| |  .----------------.  | |")
    for i in range(3):
       
        print("\033[96m| |  | " + map[i][0] + "  |  " + map[i][1] + "  |  " + map[i][2]+"  |  | |")
        if i != 2:
            print("| |  |_______________ |  | |")
    print("| |  |                |  | |")
    print("| |  '----------------'  | |")
    print("| |__GAME BOY____________/ |")
    print("| |  |                |  | |")
    print("|    .    (Nintendo)       |")
    print("|  _| |_              .-.  |")
    print("|-[_   _]-       .-. (   ) |")
    print("|   |_|         (   ) '-'  |")
    print("|    '           '-'   A   |")
    print("|                 B        |")
    print("|          ___   ___       |")
    print("|         (___) (___)  ,., |")
    print("|        select start ;:;: |")
    print("|                    ,;:;' /")
    print("|                   ,:;:'.'")
    print("'-----------------------`")
        
#vérification de la victoire
def victoire(map):
    for i in range(3):   
        if map[i][0] == map[i][1] == map[i][2] and map[i][0] != "-":
            return True
        if map[0][i] == map[1][i] == map[2][i] and map[0][i] != "-":
            return True
        if map[0][0] == map[1][1] == map[2][2] and map[0][0] != "-":
         return True
        if map[0][2] == map[1][1] == map[2][0] and map[0][2] != "-":
            return True
    return False
#vérification de la fin de partie
def fin(map):
    for i in range(3):
        for j in range(3):
            if map[i][j] == "-":
                return False
    return True
#vérification de la validité de la case
def validite(map, ligne, colonne):
    if ligne < 0 or ligne > 2 or colonne < 0 or colonne > 2:
        return False
    if map[ligne][colonne] != "-":
        return False
    return True
#affichage choix entre jouer et voir les scores
def choix():
    print("1 - Jouer")
    print("2 - Voir les scores")
    choix = int(input("Que voulez-vous faire ? "))
    if choix == 2:
        affichage_scores()
        exit()
    elif choix == 1:
        jeu()
        exit()
    else:
        print("Choix invalide")
        choix()
#affichage des scores
def affichage_scores():
    fichier = open("scores.txt", "r")
    scores = fichier.read()
    print("\___High Score________/")
    print(scores)
    print("_______________________")
    fichier.close()
    choix()
#le joueur inscrit son username
def username():
    username = input("Entrez votre username : ")
    
    print("\033[85mBonjour " + username)
    print("___________")
    return username
#création du fichier scores.txt
def creation_fichier():
    fichier = open("scores.txt", "w")
    fichier.close()
#vérification de l'existence du fichier scores.txt
def existance_fichier():
    try:
        fichier = open("scores.txt", "r")
        fichier.close()
    except FileNotFoundError:
        creation_fichier()
#vérification de l'existence du username
def existance(username):
    fichier = open("scores.txt", "r")
    scores = fichier.read()
    if username in scores:
        return True
    else:
        return False
#ajout du username dans le fichier
def ajout(username):
    fichier = open("scores.txt", "a")
    fichier.write(username + " 1")
    fichier.close()
    
def incrementation(username):
    fichier = open("scores.txt", "r")
    scores = fichier.read()
    fichier.close()
    scores = scores.split("\n")
    for i in range(len(scores)):
        if scores[i].startswith(username):
            name, score = scores[i].split()
            score = str(int(score) + 1)
            scores[i] = name + " " + score

    fichier = open("scores.txt", "w")
    for i in range(len(scores)):
        fichier.write(scores[i] + "\n")
    fichier.close()

#affichage du gagnant
def affichage_gagnant(username):
    print("Le gagnant est " + username)
    letsgo = input("Voulez-vous rejouer ? (oui/non) ")
    if letsgo == "oui":      
        jeu()
    elif letsgo == "non":
        exit()

def affichage_match_nul():
    print("Match nul")
    
#lancer le jeu
def jeu():
    print("_______")
    print("|.---.|")
    print("||___||")
    print("|+  .'|")
    print("| _ _ |")
    print("|_____/")
    existance_fichier()
    username = input("joueur 1 entrez votre nom : ")
    print("_____________")
    print("Bonjour " + username)
    username2 = input("joueur 2 entrez votre nom : ")
    print("_____________")
    print("Bonjour " + username2)
    map = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    
    affichage(map,username)
    joueur = 0
    ligne, colonne = -1, -1  # Initialize to invalid values
    while not victoire(map) and not fin(map):
        while not validite(map, ligne, colonne):
            

            position = input("Entrez une position, par ex 0,0(ligne,colonne) : ")
            if position == "exit":
                exit()
            elif position == "":
                 position = input("Entrez une position, par ex 0,0(ligne,colonne) : ")
                 ligne, colonne = position.split(",")
                 ligne = int(ligne)
                 colonne = int(colonne)
            else:
                ligne, colonne = position.split(",")
                ligne = int(ligne)
                colonne = int(colonne)

        if joueur == 0:
            map[ligne][colonne] = "X"
        else:
            map[ligne][colonne] = "O"
        affichage(map,username if joueur == 0 else username2)
        
        joueur = (joueur + 1) % 2
        ligne, colonne = -1, -1  # Reset for the next player's move
    affichage(map,joueur)
    if victoire(map):
        if joueur == 0:
            affichage_gagnant(username)
          
            if existance(username):
                incrementation(username)
                
            else:
                ajout(username)
        else:
            affichage_gagnant(username2)
           
            if existance(username2):
                incrementation(username2)
            else:
                ajout(username2)
    else:
        affichage_match_nul()

        
        
#lancer le programme
choix()
