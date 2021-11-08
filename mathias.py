import random

def mot_aleatoire(): # creation de la fonction "mot_aleatoire" pour recuperer le mot aleatoire
    fichier=open("dictionnaire.txt","r") # creation de la variable "fichier" qui ouvre le ficher en mode lecture
    mot = "" # creation de la variable "mot" egale a un string
    mots=[] # creation d'une array "mots"
    nombre_de_mots=-1 # creation de la variable "nombre_de_mots" egale a -1 car l'array commence a 0
    for ligne in fichier.readlines(): # cette fonction va lire tout les lignes du fichier
        nombre_de_mots=nombre_de_mots+1 # il va compter toute les lignes
        mots.append(ligne[:-1])#il va prendre tout les lettres du mots sauf la derniere
    fichier.close() # ferme le fichier
    nombre_aleatoire = random.randint(0, nombre_de_mots) # on va choisir un nombre aléatoire entre 0 et le nombre de lignes
    mot = mot + str(mots[nombre_aleatoire])#il va mettre le mot en str
    return mot # il va retourner le mot

mot_choisi = mot_aleatoire()
print(mot_choisi)



mode = 1
difficulte = 1
"""
Quand le mode = 1 signifie que le jeu va etre solo.
Quand le mode = 2 signigie que le jeu va etre en multijoueur. 
Quand la difficulte = 1 signifie que le jeu va etre facile.
Quand la difficulte = 2 signigie que le jeu va etre difficile.
"""
def mot_mystere(difficulte, mode):

    """
    Dans un premiere partie on va verifier
    si le jeu est en solo ou si il est en multijoueur.
    """
    if (mode == 1): #si le mode est solo alors
        mot =  mot_aleatoire() #on fait appel a la function mot_aleatoire
    elif (mode == 2): #sinon si le mode est multijoueur on demande le mot au joueur nr2
        mot = input("Joueur nr 2, veuillez introduire le mot a deviner en majuscule:") #on demande le mot au joueur 2
    else: #sinon message d'erreur
        print("Ce mode de jeu n'est pas supporter: Solo/Multijoueur")

    """
    Dans cette deuxieme partie on va verifier 
    si le jeu est facile ou difficile.
    """
    if (difficulte == 1): # si la "difficulte" est facile
        mot2 = " " # cette variable créé le mot2 et va le mettre en string 
        for caractere in mot: # parcourir chaque caractere dans la variable "mot"
            if caractere in mot[1 : -1]: # si la lettre est comprise entre la 1ere lettre exclue et la derniere exclue on ajoute une * genre x appartient a ]1;-1[
                mot2 = mot2 + "*" # va prendre le mot 2 + des astérixs sauf pour la premiere et derniere lettre
            else: # sinon 
                mot2 = mot2+caractere # on ajoute la lettre ici representer par la variable "i" au mot
        return mot2, mot # on retourne le mot mystere et le mot de la fonction mot_aleatoire

    elif (difficulte == 2): # sinon si la "difficulte" est difficile 
        mot2 = ""  # cette variable créé le mot2 et va le mettre en string 
        for caracatere in mot:
            mot2 = mot2 + "*" # pour chaque caractere present dans "mot" on va ajouter des astérixs
        return mot2, mot # on retourne le mot mystere et le mot aleatoire ou celui tape par le joueur nr2 en fonction du mode de jeu choisi

    else: # sinon
        print("La difficulte n'est pas supportee!") # on montre le message d'erreur au joueur

print(mot_mystere(mode, difficulte))