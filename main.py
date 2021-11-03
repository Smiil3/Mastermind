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
    for lettres in mot:
        nombre_de_lettres = nombre_de_lettres + 1
    return nombre_de_lettres





def mot_mystere(difficulte, mode):
    if (mode == "SOLO" or mode == "Solo" or mode == "solo"):
        mot =  mot_aleatoire()
    elif (mode == "Multijoueur" or mode == "MULTIJOUEUR" or mode == "multijoueur"):
        mot = input("Joueur nr 2, veuillez introduire le mot a deviner:")
    else:
        print("Ce mode de jeu n'est pas supporter: Solo/Multijoueur")

  # creation de la variable "mot" avec le mot aleatoire
    if (difficulte == "Facile" or difficulte == "FACILE" or difficulte == "facile"):
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
        return mot_masque, mot  # on retourne le mot mystere
    elif (difficulte == "Difficile" or difficulte == "difficile" or difficulte == 'DIFFICILE'):
        mot_masque = ""  # creation de la variable "mot_masque"
        for caracatere in mot:
            mot_masque = mot_masque + "*"
        return mot_masque, mot
    else:
        print("La difficulte n'est pas supporter: Facile/Difficile")

def verfication_nombre_de_lettre(mot, mot2):
    if (nombre_de_lettres(mot) < nombre_de_lettres(mot2) or nombre_de_lettres(mot) > nombre_de_lettres(mot2)):
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


def nombre_caracteres_manquent(mot1, mot2, mot):
    a = []
    mots = ""
    nombre = -1
    for i in mot1:
        nombre = nombre + 1
        if (not i == mot2[nombre]):
            mots = mots + i
    for caracteres in mots:
        a.append(caracteres)
    nombre2 = 0
    for i in a:
        if i in mot[1:-1]:
            nombre2 = nombre2+1
    return nombre2


def le_mot_est_juste(mot1, mot2):
    if (mot1 == mot2):
        a = True
    else:
        a = False
    return a


def jeu(mode, difficulte):
    a = mot_mystere(difficulte, mode)
    mot_myst = a[1]
    print("TEST1", mot_myst)
    nombre_de_tentatives = 0

    if (difficulte == "facile" or difficulte=="Facile" or difficulte == "FACILE"):
        boucle1 = True
        boucle2 = False
        boucle3 = False
        boucle4 = False
        tentatives = 10
    elif (difficulte == "difficile" or difficulte == "Difficile" or difficulte == "DIFFICILE"):
        boucle1 = False
        boucle2 = False
        boucle3 = False
        boucle4= True
        tentatives = 7
    print("TEST URGENT", tentatives)
    print("Mot mystere :", a[0])
    mot_utilisateur = input("Proposez un mot :")

    if (nombre_de_tentatives == tentatives):
        print("Tu as perdu.")
        boucle1 = False
        boucle2 = False
        boucle3 = False
    else:
        nombre_de_tentatives = nombre_de_tentatives+1

    while True == True:
        while boucle1 == True:
            # verif du nombre de lettres
            if (verfication_nombre_de_lettre(mot_utilisateur, mot_myst) == False):
                print("Votre mot contient", nombre_de_lettres(mot_utilisateur) +
                1, "lettres alors qu'il en faut", nombre_de_lettres(mot_myst)+1)
                mot_utilisateur = input("Proposez un mot :")

                if (nombre_de_tentatives == tentatives):
                    print("Tu as perdu.")
                    break
                else:
                    nombre_de_tentatives = nombre_de_tentatives+1
                    print("BOUCLE1", nombre_de_tentatives)

            elif (verfication_nombre_de_lettre(mot_utilisateur, mot_myst) == True):
                boucle1 = False
                boucle2 = True

        while boucle2 == True:
            if (not mot_utilisateur[0] == mot_myst[0]):
                print("La 1ere lettre de votre mot est un",
                    mot_utilisateur[0], "alors que ca devrait etre un", mot_myst[0])
                mot_utilisateur = input("Proposez un mot :")

                if (nombre_de_tentatives == tentatives):
                    print("Tu as perdu.")
                    break
                else:
                    nombre_de_tentatives = nombre_de_tentatives+1
                    print("BOUCLE2", nombre_de_tentatives)

            if (not mot_utilisateur[nombre_de_lettres(mot_utilisateur)] == mot_myst[nombre_de_lettres(mot_myst)]):
                print("La derniere lettre de votre mot est un", mot_utilisateur[nombre_de_lettres(mot_utilisateur)], "alors que ca devrait etre", mot_myst[nombre_de_lettres(mot_myst)])
                mot_utilisateur = input("Proposez un mot :")

                if (nombre_de_tentatives == tentatives):
                    print("Tu as perdu.")
                    break
                else:
                    nombre_de_tentatives = nombre_de_tentatives+1
                    print("BOUCLE2B", nombre_de_tentatives)

            elif (mot_utilisateur[0] == mot_myst[0] and mot_utilisateur[nombre_de_lettres(mot_utilisateur)] == mot_myst[nombre_de_lettres(mot_myst)]):
                boucle1 = True
                boucle2 = False
                boucle3 = True

        while boucle3 == True:
            # suite ajout des lettres valides au mot mystere zbi
            nouveau_mot = ajouter_lettres_valides(mot_myst, mot_utilisateur)
            nombre_caracteres = nombre_caracteres_manquent(
                mot_utilisateur, nouveau_mot, mot_myst)

            if (le_mot_est_juste(mot_utilisateur, mot_myst) == False):
                if (nombre_de_tentatives == tentatives):
                    print("Tu as perdu.")
                    break
                else:
                    nombre_de_tentatives = nombre_de_tentatives+1
                    print("BOUCLE3", nombre_de_tentatives)

                print("Mot mystere :", nouveau_mot)
                print("Lettres mal place :", nombre_caracteres)
                mot_utilisateur = input("Proposez un mot :")


            elif(le_mot_est_juste(mot_utilisateur, mot_myst) == True):
                boucle3 = False
                print('Bravo tu as trouver le mot, nombre de tenatives:',nombre_de_tentatives)
        while boucle4 == True:
                if(le_mot_est_juste(mot_utilisateur, mot_myst) == False):
                    if (nombre_de_tentatives == tentatives):
                        print("Tu as perdu.")
                        boucle3 = False
                        break
                    else:
                        nombre_de_tentatives = nombre_de_tentatives+1
                    print("Mot mystere :", a[0])
                    mot_utilisateur = input("Proposez un mot :")
                elif(le_mot_est_juste(mot_utilisateur, mot_myst) == True):
                    boucle4 = False
                    print('Bravo tu as trouver le mot, nombre de tenatives:',nombre_de_tentatives)
jeu("multijoueur", "facile")
