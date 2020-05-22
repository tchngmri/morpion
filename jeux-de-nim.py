import random
import time 

def preambule():
    print("Bienvenue dans le jeu de Nim, qui se joue à 2. On dispose de n pièces (vous pourrez choisir votre nombre de pièces à chaque partie).", end="")
    print("Vous pourrez choisir à chaque tour d'enlever entre 1 et 3 pièces. Le gagnant sera celui qui prendra la dernière pièce.", end="")
    print("Vous pouvez choisir de jouer à 2, ou bien seul contre notre IA, qui s'appelle Hubert. Bonjour Hubert.")

def choix_mode():
    mode = input("Combien de joueurs veulent jouer? : ")
    if(int(mode)==2):
        joueur1 = input("Comment s'appelle le premier joueur? : ")
        print ("Quel beau prénom !")
        joueur2 = input("Et toi, cher deuxième joueur? : ")
        print ("Encore plus beau prénom !")
        return mode, joueur1, joueur2
    if (int(mode)==1):
        joueur1 = input("Tu as donc choisi de jouer contre Hubert. Comment t'appelles-tu? : ")
        joueur2 = "Hubert"
        return mode, joueur1, joueur2
    else: 
        raise Exception ("Vous devez jouer soit à 1 soit à 2 !")

def creerPlateau(n):
    plateau = []
    for i in range(n):
        plateau.append(0)
    return plateau

def retirerNpieces(n, plateau):
    if(1<=n<=3)and(n<=len(plateau)):
        for i in range (n):
            plateau.pop()
        return plateau 
    if(n==0) or (n>3):
        raise Exception ("Vous devez retirer entre une et trois pièces !")
    if(n>len(plateau)):
        for i in range(len(plateau - n)):
            plateau.pop()
        return plateau

def afficherPlato(plateau):
    print("|", end="")
    for i in range (len(plateau)):
        print (" ♦ |", end="")

def unTour(plateau, joueur):
    print("À ton tour,", joueur, "!")
    afficherPlato(plateau)
    print("")
    n = input("Combien de pièces veux tu retirer? : ")
    return retirerNpieces(int(n), plateau)

def partieFinie(plateau):
    if (len(plateau)==0):
        return True

def nombreDePieces():
    n = input("Avec combien de pièces voulez-vous jouer? (on conseille d'en prendre au moins 5, et vous pouvez aller jusqu'à 500 si le coeur vous en prend!) : ")
    if(int(n)>500):
        raise Exception ("Oui bon c'est un peu trop ça quand même")
    return int(n) 

def quiAgagne(i,joueur1, joueur2):
    if (i%2==0):
        return joueur1, joueur2
    return joueur2, joueur1

def queFaitHubert(plateau):
    afficherPlato(plateau)
    if(len(plateau)%4==0):
        n = random.randint(1,3)
        time.sleep(1.0)
        print("Hubert décide de retirer", n , "pièces.")
        return retirerNpieces(n, plateau)
    else: 
        time.sleep(1.0)
        print("Hubert décide de retirer", len(plateau)%4, "pièces.")
        return retirerNpieces(len(plateau)%4, plateau)

def quiCommence(joueur1, joueur2):
    i = random.randint(1,6)
    print("Le dé est tombé sur", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", i, "!")
    time.sleep(0.5)
    if (i%2==0):
        print("C'est pair : ", joueur1, "c'est donc à toi de commencer, bonne chance :)")
        return joueur1, joueur2
    else:
        print("C'est impair : Hubert commence. Bonne chance à tous les deux!")
        return joueur2, joueur1

def jeu_a_deux(joueur1, joueur2, plateau):
    print("Allez, c'est parti ;)")
    print("")
    for i in range (len(plateau)):
        if (i%2==0):
            plateau = unTour(plateau,joueur1)
        else:
            plateau = unTour(plateau,joueur2)
        print("")
        if (partieFinie(plateau)):
            gagnant, perdant = quiAgagne(i,joueur1,joueur2)
            break
    print("Bravo", gagnant, "tu es trop fort.e !!")
    print("Déso", perdant, "retournes t'entraîner :D")

def jeu_a_un(joueur1, joueur2, plateau):
    p1, p2= quiCommence(joueur1,joueur2)
    print("Let's go!")
    print("")
    if(p1==joueur1):
        for i in range(len(plateau)):
            if (i%2==0):
                plateau = unTour(plateau, joueur1)
            else: 
                plateau = queFaitHubert(plateau)
            print("")
            if(partieFinie(plateau)):
                gagnant, perdant = quiAgagne(i, joueur1, joueur2)
                break 
        if(gagnant=="Hubert"):
            print("Hubert t'as battu ! Bouh !")
        else: 
            print("Bravo, tu es intellectuellement supérieur à la machine")
    else: 
        for i in range(1, len(plateau)+1):
            time.sleep(0.5)
            if (i%2==0):
                plateau = unTour(plateau, joueur1)
            else: 
                plateau = queFaitHubert(plateau)
            print("")
            if(partieFinie(plateau)):
                gagnant, perdant = quiAgagne(i, joueur1, joueur2)
                break 
        if(gagnant=="Hubert"):
            print("Hubert t'as battu ! Bouh !")
        else: 
            print("Bravo, tu es intellectuellement supérieur à la machine")


        

def partie():
    preambule()
    mode,joueur1,joueur2 = choix_mode() 
    n = nombreDePieces()
    plateau = creerPlateau(n)
    if (int(mode) == 2):
        jeu_a_deux(joueur1, joueur2, plateau)
    if (int(mode)==1):
        jeu_a_un(joueur1, joueur2, plateau)
#rejouer ? garder le fil des parties ? demander si tu veux les explications ? 
    
partie()