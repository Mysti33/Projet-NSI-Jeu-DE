from random import randint
from Déefonctions2 import *
def generer_nombre() -> int:
    '''
    Génére un nombre aléatoire entre 1 et 6
    '''
    d = randint(1,6)
    return d

def determiner_somme(d1 : int, d2 : int) -> int:
    '''
    Calcule la somme des dées tirées.
    '''
    d1= generer_nombre()
    d2= generer_nombre()
    
    somme = d1 + d2
    return somme

def jeu() -> None:
    '''
    Permet de créer la boucle de jeu.
    '''
    print("")
    rejouer = input("Veut tu rejouer ? [Y/N] ")
    print("")
    if rejouer == "Y" or rejouer == "y":
        demander_valeur()
    elif rejouer == "N" or rejouer == "n":
        return(True)