#fonction1
mot=""
def nombre_de_lettres(mot): 
    m=0 #au départ le nombre de caractere "m" est égal a 0
    for caractere in mot: #parcours un caractere dans le mot
        m=m+1 #ajoute 1 au nombre de lettre
    return m #retourne le nombre de lettre (résultat)
print(nombre_de_lettres(mot)) #afficher le résultat de la fonction (m)

#fonction2
mot1=""
mot2=""
def verification_nombre_de_lettre(mot1, mot2):
    if (nombre_de_lettres(mot1) < nombre_de_lettres(mot2) or nombre_de_lettres(mot1) > nombre_de_lettres(mot2)): #le nombre de lettres (fonction1) du mot1 < ou > au nombre de lettres du mot2
        n = False #n est égal a la valeur booléen False (faux)
    else : #sinon
        n = True #alors n est égal a la valeur booléen True (vrai)
    return n #retourne la valeur booléene
verification_nombre_de_lettre(mot1, mot2) 

#fonction3
def ajouter_lettres_valides(mot1, mot2):
    nombre  = -1 #au départ le caractere "nombre" est égal a -1 soit 0
    m = ""
    for caractere in mot1: #parcours un caractere dans le mot1
        nombre = nombre + 1 #ajoute 1 a nombre au départ égal a -1
        if (caractere == mot2[nombre]): #si caractere du mot1 correspond au même caractere du mot2
            m = m + caractere #on ajoute le caractere a "m"
        else: #sinon
            m = m + "*" #puisque caractere n'est pas valide on ajoute un "*"
    return m #retourne la valeur de m soit un caractere ou bien un "*"
print(ajouter_lettres_valides("BAUJOUR", "BONJOUR")) #afficher le résultat de la fonction (m)