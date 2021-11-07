from os import error
from random import * 


def mot_aleatoire():  # creation de la fonction "mot_aleatoire" pour recuperer le mot aleatoire
    # creation de la variable "fichier" qui ouvre le ficher en mode lecture
    fichier = open("dictionnaire.txt", "r")
    mot = ""  # creation de la variable "mot" egale a un string
    mots = []  # creation d'une array "mots"
    # creation de la variable "nombre_de_mots" egale a -1 car l'array commence a 0
    nombre_de_mots = -1
    for ligne in fichier.readlines():
        nombre_de_mots = nombre_de_mots + 1
        # on rajoute a notre array "mots" le mot de la ligne sans le retour a la ligne "\n"
        mots.append([ligne[:-1]])
    fichier.close()  # fermeture du fichier
    nombre_aleatoire = randint(0, nombre_de_mots)
    """
    creation de la variable "nombre_aleatoire" de mots presents 
    dans le fichier et on le garde dans la variable nombre_aleatoire
    """
    mot = mot + str(mots[nombre_aleatoire]
                    )  # on ajoute le mot aleatoire sous forme de string a la variable "mot"
    # on supprime le "['" et le "']" de l'array et on retorune le mot aleatoire
    return mot[2:-2]


def nombre_de_lettres(mot):
    nombre_de_lettres = -1  # creation de la variable "nombre_de_lettres" = -1
    for lettres in mot: #pour chaque lettre on fait +1
        nombre_de_lettres = nombre_de_lettres + 1
    return nombre_de_lettres





def mot_mystere(difficulte, mode):
    if (mode == 1): #si le mode est solo alors
        mot =  mot_aleatoire() #on fait appel a la function mot_aleatoire
    elif (mode == 2): #sinon si le mode est multijoueur on demande le mot au joueur nr2
        mot = input("Joueur nr 2, veuillez introduire le mot a deviner:") #on demande le mot au joueur 2
    else: #sinon message d'erreur
        print("Ce mode de jeu n'est pas supporter: Solo/Multijoueur")

    if (difficulte == 1): # si la difficulte est facile alors
        nombre = -1  # creation de la variable "nombre" = -1
        mot_masque = ""  # creation de la variable "mot_masque"
        for caracatere in mot: 
            nombre = nombre + 1  # pour chaque caractere on ajoute 1 a la variable "nombre"
            if (nombre == 0):  # si la variable "nombre" est egale a 0 qui correspond a la premiere lettre du mot
            # on ajoute le caractere a la variable "mot_masque"
                mot_masque = mot_masque + caracatere
        # sinon si nombre est egale au nombre de lettres present dans la variable "mot"
            elif (nombre == nombre_de_lettres(mot)):
            # on ajout le caractere a la variable "mot_masque"
                mot_masque = mot_masque + caracatere
            else:
                mot_masque = mot_masque + "*"  # sinon on ajoute "*" a la variable "mot_masque"
        return mot_masque, mot  # on retourne le mot mystere et le mot de la fonction mot_aleatoire
    elif (difficulte == 2): #sinon si la difficulte est difficile 
        mot_masque = ""  # creation de la variable "mot_masque"
        for caracatere in mot:  # pour chaque caractere on remplace le caractere par un *
            mot_masque = mot_masque + "*"
        return mot_masque, mot #on retourn le mot du utilisateur et le mot mystere
    else:
        print("La difficulte n'est pas supportee!") #sinon message d'erreur

def verfication_nombre_de_lettre(mot, mot2):
    if (nombre_de_lettres(mot) < nombre_de_lettres(mot2) or nombre_de_lettres(mot) > nombre_de_lettres(mot2)): 
        #si le nombre de lettre de mot1 n'est pas egal a celui de mot2 on return false sinon true
        resultat = False
    else:
        resultat = True
    return resultat


def ajouter_lettres_valides(mot, mot2):
    nombre = -1
    mot_masque = ""
    for caractere in mot:
        nombre = nombre + 1
        if (nombre > nombre_de_lettres(mot2)):
            return #HELP
        if (nombre == 0):  # si la variable "nombre" est egale a 0 qui correspond a la premiere lettre du mot
            # on ajoute le caractere a la variable "mot_masque"
            mot_masque = mot_masque + caractere
        # sinon si nombre est egale au nombre de lettres present dans la variable "mot"
        elif (nombre == nombre_de_lettres(mot)):
            # on ajout le caractere a la variable "mot_masque"
            mot_masque = mot_masque + caractere
        elif caractere == mot2[nombre]:
            # sinon on ajoute "*" a la variable "mot_masque"
            mot_masque = mot_masque + caractere
        else:
            mot_masque = mot_masque + "*"

    return mot_masque


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


def le_mot_est_juste(mot1, mot2):
    if (mot1 == mot2): #si le mot1 est egal a mot2 alors on return True sinon false
        resultat_de_la_fonction = True # on definie la variable "resultat_de_la_fonction" qui est egal a la valeur booleene "True"
    else: #sinon
        resultat_de_la_fonction = False # on definie la variable "resultat_de_la_fonction" qui est egal a la valeur booleene "False"
    return resultat_de_la_fonction # on retourne la variable "resultat_de_la_fonction"


def jeu():

    """
    Ici on va presenter au joueur les differents paramettres du jeu, 
    et il devra choisir quel mode de jeu il aimerait jouer.
    """
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
    mot_myst = resultat_de_la_fonction_m_myst[1]
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
    print("TEST", resultat_de_la_fonction_m_myst[1], nombre_de_lettres(resultat_de_la_fonction_m_myst[1]))
    print("Mot mystere :", resultat_de_la_fonction_m_myst[0])
    mot_utilisateur = input("Proposez un mot :")

    if (nombre_de_tentatives == tentatives):
        print("Tu as perdu.")
        boucle1 = False
        boucle2 = False
        boucle3 = False
    else:
        nombre_de_tentatives = nombre_de_tentatives+1




    """
    Dans cette premiere boucle nous allons verifier le nombre de lettres que l'utlisateur
    a entre, correspond bien au nombre de lettres du mot mystere a trouver, sinon on lui redemande
    de rentrer le mot jusqu'a ce que le nombre de lettres corresponde. 
    """
    while boucle1 == True:

        if (verfication_nombre_de_lettre(mot_utilisateur, mot_myst) == False): # si notre fonction "verification_nombre_de_lettres" retourne une valuer booleen "False"
            print("Votre mot contient", nombre_de_lettres(mot_utilisateur) + 1, "lettres alors qu'il en faut", nombre_de_lettres(mot_myst)+1) # on montre l'erreur au joueur
            mot_utilisateur = input("Proposez un mot :") #on redemande au joueur de resaisir le mot

            """
            Ici nous verifions que le joueur ne 
            depasse pas le nombre de tentatives.
            """
            if (nombre_de_tentatives == tentatives): # si le nombre de tentatives est egal a la limite de tentatives
                print("Vous avez perdu.") # ici on averti le joueur qu'il a perdu
                break # ici on arrete toute la fonction ici.
            else:  # sinon
                nombre_de_tentatives = nombre_de_tentatives + 1 # on ajoute une tentative de plus au nombre de tentatives

        elif (verfication_nombre_de_lettre(mot_utilisateur, mot_myst) == True): # sinon si notre fonction "verification_nombre_de_lettres" retourne une valeur booleen "True"
            boucle1 = False # on sort de la boucle 1
            boucle2 = True # on rentre dans la boucle 2

    
    
    

    """
    Dans cette deuxieme boucle nous allons verifier que la premiere lettre que l'utlisateur
    a entre, correspond bien a la premiere lettre du mot mystere a trouver, sinon on lui redemande
    de rentrer le mot jusqu'a ce que le nombre de lettres corresponde et de meme pour la derniere lettre. 
    """
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



    """
    Dans cette deuxieme boucle nous allons verifier que la premiere lettre que l'utlisateur
    a entre, correspond bien a la premiere lettre du mot mystere a trouver, sinon on lui redemande
    de rentrer le mot jusqu'a ce que le nombre de lettres corresponde et de meme pour la derniere lettre. 
    """
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



    """
    Cette 4eme boucle est pour le mode difficile ou on n'a plus 
    besoin de la 1er, 2eme et de la 3eme boucle pour faire les verifications et les ajouts de lettres.
    """
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

"""
Modes possible pour jouer:
1 - jeu("multijoueur", "facile")
2 - jeu("solo", "facile")
3 - jeu("multijoueur", "difficile")
4 - jeu("solo", "difficile")
"""

jeu()


