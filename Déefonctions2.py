from Déefonctions1 import *
def comparer_et_afficher(somme: int, essai: int) -> bool:
    '''
    Permet de comparer la somme des dées avec la valeur donnée
    par le joueur.
    '''
    if essai < somme:
        print("La somme est supérieur à votre réponse")
    elif essai > somme:
        print("La somme est Inférieur à votre réponse")
    else:
        print("Bravo ! Tu à trouvé")

def demander_valeur() -> int:
    '''
    Demande au joueur la valeur pour trouver celle du dé.
    '''
    import time
    print("Génération des dés")
    time.sleep(2)
    print("Dés générées, début de la partie !")
    time.sleep(0.3)
    print("")
    
    from Déefonctions1 import determiner_somme
    somme = determiner_somme(1,1)
    essai = 0
    while essai != somme:
        essai = int(input("Qu'elle est la somme des dés ? "))
        resultat = comparer_et_afficher(somme,essai)