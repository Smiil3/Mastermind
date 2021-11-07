mot1 = "AAION"
mot2 = "A***N"
mot_a_trouver = "AVION"
def nombre_caracteres_manquent(mot1, mot2, mot_a_trouver):
    caracteres_present = [] # ici on definie la variable "caracteres_present" qui est egale a une array
    mots = "" # ici on definie la variable "mots" a un string vide
    nombre = -1 # ici on definie la variable "nombre" a -1
    for caractere1 in mot1: # pour chaque caractere dans la variable "mot1"
        nombre = nombre + 1 # on ajoute 1 a la variable "nombre"
        if (not caractere1 == mot2[nombre]): # si le caracatere du "mot1" n'est pas egale au meme caratere du "mot2"
            mots = mots + caractere1 # on ajoute le caractere du "mot1" a notre variable "mots"
    for caractere2 in mots: #pour chaque caractere dans la variable "mots"
        caracteres_present.append(caractere2) #on ajoute le caractere de la variable "mots" dans l'array "a"
    nombre2 = 0 # on definie la variable "nombre2" qui est egale a 0
    for caractere3 in caracteres_present: # pour chaque caractere present dans l'array "caracteres_present"
        if caractere3 in mot_a_trouver[1:-1]: # si le caractere est present dans la variable "mot_a_trouver"
            nombre2 = nombre2+1 # on ajoute 1 a la variable "nombre2"
    return nombre2 # finalement on retourne la variable "nombre2" qui correspond au nombre de lettres mal placees par l'utilisateur

print("Test 1er Fonction:", nombre_caracteres_manquent(mot1, mot2, mot_a_trouver))



def le_mot_est_juste(mot1, mot2):
    if (mot1 == mot2): #si le mot1 est egal a mot2 alors on return True sinon false
        resultat_de_la_fonction = True # on definie la variable "resultat_de_la_fonction" qui est egal a la valeur booleene "True"
    else: #sinon
        resultat_de_la_fonction = False # on definie la variable "resultat_de_la_fonction" qui est egal a la valeur booleene "False"
    return resultat_de_la_fonction # on retourne la variable "resultat_de_la_fonction"

print("Test 2eme Fonction:", le_mot_est_juste(mot1, mot2))




# Pour tester cette fonction il faut lancer tout le programme complet. 
"""
# fonction Eduard
def jeu():

    menu_selection = True
    while menu_selection == True:
        print("Modes de jeu disponibles:\n 1 - Solo | Facile\n 2 - Solo | Difficile\n 3 - Multijoueur | Facile\n 4 - Multijoueur | Difficile")
        mode_de_jeu = int(input("Veuillez choisir le nombre correspondant au mode du jeu auquel vous voulez jouer:"))
        if (mode_de_jeu == 1):
            mode = 1
            difficulte = 1
            menu_selection = False
        elif (mode_de_jeu == 2):
            mode = 1
            difficulte = 2
            menu_selection = False
        elif (mode_de_jeu == 3):
            mode = 2
            difficulte = 1
            menu_selection = False
        elif (mode_de_jeu == 4):
            mode = 2
            difficulte = 2
            menu_selection = False
        else:
            print("Le mode de jeu choisi est n'existe pas.")

    resultat_de_la_fonction_m_myst = mot_mystere(difficulte, mode) # on enregistre les 2 resultats de la fonction "mot_mystere" dans la variable "resultat_de_la_fonction_m_myst"
    mot_myst = resultat_de_la_fonction_m_myst[1] # on enregistre le deuxieme resultat de la fonction "mot_mystere" dans la variable "mot_myst"
    nombre_de_tentatives = 0 # on definie la variable "nombre_de_tentatives" qui est egale  0


    if (difficulte == 1):
        boucle1 = True
        boucle2 = False
        boucle3 = False
        boucle4 = False
        tentatives = 10
    elif (difficulte == 2):
        boucle1 = False
        boucle2 = False
        boucle3 = False
        boucle4= True
        tentatives = 7

    print("Mot mystere :", resultat_de_la_fonction_m_myst[0])
    mot_utilisateur = input("Proposez un mot :")

    if (nombre_de_tentatives == tentatives): # si le nombre de tentatives est egal a la limite de tentatives
        print("Vous avez perdu perdu.") # ici on averti le joueur qu'il a perdu
        # on desactive toutes les boucles
        boucle1 = False 
        boucle2 = False
        boucle3 = False
        boucle4 = False
    else: # sinon
        nombre_de_tentatives = nombre_de_tentatives + 1 # on ajoute une tentative de plus au nombre de tentatives



    while boucle1 == True:
        if (verification_nombre_de_lettre(mot_utilisateur, mot_myst) == False): # si notre fonction "verification_nombre_de_lettres" retourne une valuer booleen "False"
            print("Votre mot contient", nombre_de_lettres(mot_utilisateur) + 1, "lettres alors qu'il en faut", nombre_de_lettres(mot_myst)+1) # on montre l'erreur au joueur
            mot_utilisateur = input("Proposez un mot :") #on redemande au joueur de resaisir le mot

            if (nombre_de_tentatives == tentatives): # si le nombre de tentatives est egal a la limite de tentatives
                print("Vous avez perdu.") # ici on averti le joueur qu'il a perdu
                break # ici on arrete toute la fonction ici.
            else:  # sinon
                nombre_de_tentatives = nombre_de_tentatives + 1 # on ajoute une tentative de plus au nombre de tentatives

        elif (verification_nombre_de_lettre(mot_utilisateur, mot_myst) == True): # sinon si notre fonction "verification_nombre_de_lettres" retourne une valeur booleen "True"
            boucle1 = False # on sort de la boucle 1
            boucle2 = True # on rentre dans la boucle 2

    
    
    

    while boucle2 == True:

        if (not mot_utilisateur[0] == mot_myst[0]):  #si la premiere lettre du "mot_utilisateur" n'es pas egale a la premiere lettre du "mot_myst"
            print("La 1ere lettre de votre mot est un", mot_utilisateur[0], "alors que ca devrait etre un", mot_myst[0]) # on montre l'erreur au joueur
            mot_utilisateur = input("Proposez un mot :") 

            if (nombre_de_tentatives == tentatives):
                print("Vous avez perdu.")
                break
            else:
                nombre_de_tentatives = nombre_de_tentatives + 1

        if (not mot_utilisateur[nombre_de_lettres(mot_utilisateur)] == mot_myst[nombre_de_lettres(mot_myst)]): #si la derniere lettre du "mot_utilisateur" n'es pas egale a la derniere lettre du "mot_myst" 
            print("La derniere lettre de votre mot est un", mot_utilisateur[nombre_de_lettres(mot_utilisateur)], "alors que ca devrait etre", mot_myst[nombre_de_lettres(mot_myst)])
            mot_utilisateur = input("Proposez un mot :")

            if (nombre_de_tentatives == tentatives):
                print("Vous avez perdu.")
                break
            else:
                nombre_de_tentatives = nombre_de_tentatives + 1

        elif (mot_utilisateur[0] == mot_myst[0] and mot_utilisateur[nombre_de_lettres(mot_utilisateur)] == mot_myst[nombre_de_lettres(mot_myst)]): #sinon si la premiere et la derniere lettre du "mot_utilisateur" correspondent a la premiere et la derniere lettre du "mot_myst"
            boucle2 = False # on sort de la boucle 2
            boucle3 = True # on rentre dans la boucle 3



    while boucle3 == True:

        nouveau_mot = ajouter_lettres_valides(mot_myst, mot_utilisateur) # on definie la variable "nouveau_mot" qui va contenir le mot mystere avec les lettres deja trouves par le joueur
        nombre_caracteres = nombre_caracteres_manquent(mot_utilisateur, nouveau_mot, mot_myst) # on definie la variable "nombre_caracteres" qui va contenir le resultat de la fonction "nombre_caracteres_manquent"

        if (le_mot_est_juste(mot_utilisateur, mot_myst) == False): # si la fonction "le_mot_est_juste" nous retourne une valeur booleen "False"
            if (nombre_de_tentatives == tentatives):
                print("Vous avez perdu.")
                break
            else:
                nombre_de_tentatives = nombre_de_tentatives + 1

            print("Mot mystere :", nouveau_mot) # on montrer le mot mystere au joueur avec les nouvelles lettres
            print("Lettres mal place :", nombre_caracteres) # on lui montre le nombre de lettres qu'il a mal placee
            mot_utilisateur = input("Proposez un mot :")


        elif(le_mot_est_juste(mot_utilisateur, mot_myst) == True): # sinon si la fonction "le_mot_est_juste" nous retourne une valeur booleen "True"
            boucle3=False # on sort de la boucle 3
            print('Bravo tu as trouver le mot, nombre de tenatives:', nombre_de_tentatives) # on montre au joueur qu'il a gagner



    mot_mystere_afficher = resultat_de_la_fonction_m_myst[0] # on definie la variable "mot_mystere_afficher" qui contient le mot_mystere
    while boucle4 == True:
        nouveau_mot = ajouter_lettres_valides(mot_myst, mot_utilisateur) # on definie la variable "nouveau_mot" qui va contenir le mot mystere avec les lettres deja trouves par le joueur

        if (le_mot_est_juste(mot_utilisateur, mot_myst) == False): # si la fonction "le_mot_est_juste" nous retourne une valeur booleen "False"

            if (nombre_de_tentatives == tentatives):
                print("Vous avez perdu.")
                break
            else:
                nombre_de_tentatives = nombre_de_tentatives + 1

            if (nouveau_mot == None): # si le joueur ne respecte pas le nombre de "*" qui correspond au nombre de lettres du mot a trouver la fonction "nouveau_mot" va retourner "None" qui est un valeur vide
                print("Mot mystere :", mot_mystere_afficher) # on affiche le mot mystere qui va etre le resultat de la fonction "mot_mystere"
            else: #sinon si le joueur a trouver des lettres valides
                print("Mot mystere :", nouveau_mot) # on affiche la variable "nouveau_mot"
                mot_mystere_afficher = nouveau_mot # on definie la variable "mot_mystere_afficher" a la variable "nouveau_mot"
            mot_utilisateur = input("Proposez un mot :")
        elif (le_mot_est_juste(mot_utilisateur, mot_myst) == True): # sinon si la fonction "le_mot_est_juste" nous retourne une valeur booleen "True"
            print('Bravo tu as trouver le mot, nombre de tenatives:', nombre_de_tentatives) # on montre au joueur qu'il a gagner
            boucle4 = False #on sort de la boucle 4

jeu()
"""