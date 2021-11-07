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

mot_choisi = mot_aleatoire
print(mot_choisi)