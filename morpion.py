# -*- coding: utf-8 -*-
import random

def choix_mode():
    mode = input("Combien de joueurs ?")
    if(int(mode)==2):
        print (" ")
        joueur1 = input("Comment t'appelles-tu, Joueur 1 ?")
        print ("Tu joues les croix !")
        print (" ")
        joueur2 = input("Comment t'appelles-tu, Joueur 2 ?")
        print ("Tu joues les ronds !")
        return mode, joueur1, joueur2
    if (int(mode)==1):
        print (" ")
        joueur1 = input("Tu as donc choisi de jouer contre Morpionnage. Comment t'appelles-tu?")
        joueur2 = "Morpionnage"
        return mode, joueur1, joueur2
    else: 
        raise Exception ("Vous devez jouer soit à 1 soit à 2 !")


def creerCases():
    grille = [[False,False,False],[False,False,False],[False,False,False]]
    return grille 

def afficher(cases):
    print("   1   2   3")
    print (" -------------")
    for i in range (3):
        print (i+1, end=" ")
        for j in range (3):
            if(cases[i][j]!=False):
                print("|", cases[i][j],end=" ")
            else:
                print("|   ",end="")
        print("|")
        print (" -------------")

afficher(creerCases())

def jeu_un_tour(nom_utilisateur):
    ligne = int(input("Sur quelle ligne veux-tu jouer ?"))-1
    colonne = int(input("Sur quelle colonne ?"))-1
    return (ligne,colonne)

def verif_tour(ligne, colonne, cases):
    if (ligne<=2)and(ligne>=0):
        if (colonne<=2)and(colonne>=0):
            if(cases[ligne][colonne]!="X")or(cases[ligne][colonne]!="O"):
                return True
    return False 


def qlqn_a_gagne(cases):
    for i in range (3):
        if(cases[i][0]==cases[i][1])and(cases[i][1]==cases[i][2])and(cases[i][0]!=False):
            return True
    for j in range(3):
        if(cases[0][j]==cases[1][j])and(cases[0][j]==cases[2][j])and(cases[0][j]!=False):
            return True
    if(cases[0][0]==cases[1][1])and(cases[0][0]==cases[2][2])and(cases[0][0]!=False):
        return True
    if(cases[0][2]==cases[2][0])and(cases[1][1]==cases[0][2])and(cases[2][0]!=False):
        return True
    return False

def gagnant(cases,joueur1,joueur2):
    for i in range (3):
        if(cases[i][0]==cases[i][1])and(cases[i][1]==cases[i][2])and(cases[i][0]!=False):
            if(cases[i][0]=="X"):
                print(joueur1, ", bien joué champion !", joueur2, ", révise tes cours de morpion !")
        else:
            print(joueur2, ", bien joué champion !", joueur1, ", révise tes cours de morpion !")
    for j in range(3):
        if(cases[0][j]==cases[1][j])and(cases[0][j]==cases[2][j])and(cases[0][j]!=False):
            if(cases[0][j]=="X"):
                print(joueur1, ", bien joué champion !", joueur2, ", révise tes cours de morpion !")
            else:
                print(joueur2, ", bien joué champion !", joueur1, ", révise tes cours de morpion !")
    if(cases[0][0]==cases[1][1])and(cases[0][0]==cases[2][2])and(cases[0][0]!=False):
        if(cases[0][0]=="X"):
            print(joueur1, ", bien joué champion !", joueur2, ", révise tes cours de morpion !")
        else:
            print(joueur2, ", bien joué champion !", joueur1, ", révise tes cours de morpion !")
        if(cases[0][2]==cases[2][0])and(cases[1][1]==cases[0][2])and(cases[2][0]!=False):
            if(cases[0][0]=="X"):
                print(joueur1, ", bien joué champion !", joueur2, ", révise tes cours de morpion !")
            else:
                print(joueur2, ", bien joué champion !", joueur1, ", révise tes cours de morpion !")

def bloquer_l_adversaire(cases):
  if(cases[2][0]=="X" and cases[0][0]=="X" and cases[1][0] != "O"):
    cases[1][0] = "O"
    return True
  if(cases[0][0]=="X" and cases[1][0]=="X" and cases[2][0] != "O"):
    cases[2][0] = "O"
    return True
  if(cases[1][0]=="X" and cases[2][0]=="X" and cases[0][0] != "O"):
    cases[0][0] = "O"
    return True
  if(cases[0][0]=="X" and cases[0][2]=="X" and cases[0][1] != "O"):
    cases[0][1] = "O"
    return True
  if(cases[0][0]=="X" and cases[0][1]=="X" and cases[0][2] != "O"):
    cases[0][2] = "O"
    return True
  if(cases[0][1]=="X" and cases[0][2]=="X" and cases[0][0] != "O"):
    cases[0][0] = "O"
    return True
  if(cases[0][2]=="X" and cases[2][2]=="X" and cases[1][2] != "O"):
    cases[1][2] = "O"
    return True
  if(cases[0][2]=="X" and cases[1][2]=="X" and cases[2][2] != "O"):
    cases[2][2] = "O"
    return True
  if(cases[2][2]=="X" and cases[1][2]=="X" and cases[0][2] != "O"):
    cases[0][2] = "O"
    return True
  if(cases[2][2]=="X" and cases[2][0]=="X" and cases[2][1] != "O"):
    cases[2][1] = "O"
    return True
  if(cases[0][0]=="X" and cases[1][1]=="X" and cases[2][2] != "O"):
    cases[2][2] = "O"
    return True
  if(cases[1][1]=="X" and cases[2][2]=="X" and cases[0][0] != "O"):
    cases[0][0] = "O"
    return True
  if(cases[0][2]=="X" and cases[1][1]=="X" and cases[2][0] != "O"):
    cases[2][0] = "O"
    return True
  if(cases[2][0]=="X" and cases[1][1]=="X" and cases[0][2] != "O"):
    cases[0][2] = "O"
    return True
  if((cases[2][0]=="X" and cases[0][2]=="X" and cases[1][1] != "O")or(cases[0][0]=="X" and cases[2][2]=="X" and cases[1][1] != "O")):
    cases[1][1] = "O"
    return True
  if(cases[0][1]=="X" and cases[1][1]=="X" and cases[2][1] != "O"):
    cases[2][1] = "O"
    return True
  if(cases[0][1]=="X" and cases[2][1]=="X" and cases[1][1] != "O"):
    cases[1][1] = "O"
    return True
  if(cases[1][1]=="X" and cases[2][1]=="X" and cases[0][1] != "O"):
    cases[0][1] = "O"
    return True
  if(cases[1][0]=="X" and cases[1][1]=="X" and cases[1][2] != "O"):
    cases[1][2] = "O"
    return True
  if(cases[1][2]=="X" and cases[1][1]=="X" and cases[1][0] != "O"):
    cases[1][0] = "O"
    return True
  if(cases[1][0]=="X" and cases[1][2]=="X" and cases[1][1] != "O"):
    cases[1][1] = "O"
    return True
  if(cases[2][2]=="X" and cases[2][1]=="X" and cases[2][0] != "O"):
    cases[2][0] = "O"
    return True
  if(cases[2][0]=="X" and cases[2][2]=="X" and cases[2][1] != "O"):
    cases[2][1] = "O"
    return True
  

def gagner(cases):
  if(cases[2][0]=="O" and cases[0][0]=="O" and cases[1][0] != "X"):
    cases[1][0] = "O"
    return True 
  if(cases[0][0]=="O" and cases[0][2]=="O" and cases[0][1] != "X"):
    cases[0][1] = "O"
    return True
  if(cases[0][2]=="O" and cases[2][2]=="O" and cases[1][2] != "X"):
    cases[1][2] = "O"
    return True
  if(cases[2][2]=="O" and cases[2][0]=="O" and cases[2][1] != "X"):
    cases[2][1] = "O"
    return True
  if((cases[2][0]=="O" and cases[0][2]=="O" and cases[1][1] != "X")or(cases[0][0]=="O" and cases[2][2]=="O" and cases[1][1] != "X")):
    cases[1][1] = "O"
    return True
  if(cases[0][0]=="O" and cases[1][1]=="O" and cases[2][2] != "X"):
    cases[2][2] = "O"
    return True
  if(cases[1][1]=="O" and cases[2][2]=="O" and cases[0][0] != "X"):
    cases[0][0] = "O"
    return True
  if(cases[0][2]=="O" and cases[1][1]=="O" and cases[2][0] != "X"):
    cases[2][0] = "O"
    return True
  if(cases[2][0]=="O" and cases[1][1]=="O" and cases[0][2] != "X"):
    cases[0][2] = "O"
    return True

def jeu_a_deux():
  cases = creerCases()
  mode,joueur1,joueur2 = choix_mode() 
  if(int(mode)==2):
      print (" ")
      print("Les lignes et colonnes sont numérotées de 1 à 3. Que le meilleur gagne, c'est parti !")
      for i in range(9):
          if(i%2==0):
              print("À ton tour", joueur1, "!")
              ligne,colonne = jeu_un_tour(joueur1)
              if(verif_tour(ligne,colonne,cases)==True):
                cases[ligne][colonne] = "X"
              else:
                raise Exception ("Enfin, tu ne peux pas jouer là !") 
          else:
              print("À ton tour", joueur2,"!")
              ligne,colonne = jeu_un_tour(joueur2)
              if(verif_tour(ligne,colonne,cases)==True):
                  cases[ligne][colonne] = "O"
              else:
                  raise Exception("Enfin, tu ne peux pas jouer là !")
          afficher(cases)
          if(qlqn_a_gagne(cases)==True):
            break
      if(qlqn_a_gagne(cases)):
            gagnant(cases,joueur1,joueur2)
      else:
          print("Personne n'a gagné ! Ex-aequo les losers !")
  if (int(mode)==1):
      print (" ")
      print("Les lignes et colonnes sont numérotées de 1 à 3. Que le meilleur gagne, c'est parti !")
      afficher(cases)
      for i in range(9):
          if(i%2 == 0):
            x = 1
#            x = random.randint(1,4)
            if(x == 1):
              if(i==0):
                cases[2][0] = "O"
              if(i==2):
                y = 0
                if((ligne==2 and colonne==1)or(ligne==2 and colonne==2)or(ligne==1 and colonne==2)):
                  cases[0][0] = "O"
                  y = 1
                if((ligne==1 and colonne==0)or(ligne==0 and colonne==0)or(ligne==0 and colonne==1)):
                  cases[2][2] = "O"
                  y = 2
                if(ligne==0 and colonne==2):
                  cases[0][0] = "O"
                  y = 3
                if(ligne==1 and colonne==1):
                  cases[2][2] = "O"
              if(i==4):
                z = 0
                if(bloquer_l_adversaire(cases)==True):
                  bloquer_l_adversaire(cases)
                  z = 1
                if(gagner(cases)==True):
                  gagner(cases)
                if(y == 1):
                  if(z == 0):
                    cases[0][2] = "O"
                if(y == 2):
                  if(z == 0):
                    cases[0][2] = "O"
                if(y == 3):
                  cases[2][2] = "O"
              if(i == 6 or i ==8):
                if(bloquer_l_adversaire(cases)==True):
                  bloquer_l_adversaire(cases)
                if(gagner(cases)==True):
                  gagner(cases)
#              if(x == 2):
#                if(i==0):
#                  cases[0][0] = "O"
#              if(x == 3):
#                if(i==0):
#                  cases[0][2] = "O"
#              if(x == 4):
#                if(i==0):
#                  cases[2][2] = "O"
                
          else :
              print("À ton tour", joueur1, "!")
              ligne,colonne = jeu_un_tour(joueur1)
              if(verif_tour(ligne,colonne,cases)==True):
                  cases[ligne][colonne] = "X"
              else:
                  raise Exception ("Enfin, tu ne peux pas jouer là !")
          afficher(cases)
          if(qlqn_a_gagne(cases)==True):
            break
      if(qlqn_a_gagne(cases)):
            gagnant(cases,joueur1,joueur2)
      else:
          print("Personne n'a gagné ! Ex-aequo les losers !")
              
  
 
jeu_a_deux()
