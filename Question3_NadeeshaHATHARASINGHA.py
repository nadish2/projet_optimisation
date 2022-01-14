# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 01:08:49 2022

@author: nadee
"""

import BigmGeneral_NadeeshaHATHARASINGHA as b
import numpy as np


#Question 3: 4 variables décisionnelles et 4 contraintes "=" et "w=" --> Méthode Big M
"""    Minimiser Z : 30x11 + 25x12 + 36x21 + 30x22  
        s.c :
            	A :  x11 + x21 = 200
            	B :  x12 + x22 = 300
            	C :  x11 + x12 <= 400
            	D : x21 + x22 <= 300
 
            
"""
#Cliquez sur 'Run' pour voir les itérations et le résultat de la méthode Big M 

#Tests
print("\n BigM: 4 variables et 4 contraintes \n")
print("------------------------------------------------------------------------------------")

#Exemple: 3 variable/3 contraintes 
# Pour tester variable en input--> Commenter les 2 lignes en dessous
nbvar=4
nbcontr=4

#nombre de colonnes= colonne z + nombre de variables de decision + nombre de contraintes + variable artificielles + après égalité + opérateur + booleen ligne pivot ou non
nbcol= 1 + nbvar + (nbcontr*2) + 1 + 1 + 1


#nombre de lignes = nombre de contraintes +1 
nbrow= nbcontr + 1

#On crée une matrice de 0 
tab= np.zeros((nbrow,nbcol))


#Exemple de valeurs pour 4 variables et 4 contraintes
#Z
tab[0][0]=1 #z
tab[0][1]=30 #x11
tab[0][2]=25 #x12
tab[0][3]=36 #x21
tab[0][4]=30 #x22
tab[0][nbcol-3]=0 #b

#Contrainte n°1
tab[1][1]=1 #x11
tab[1][2]=0 #x12
tab[1][3]=1 #x21
tab[1][4]=0 #x22
tab[1][nbcol-3]=200 #b
tab[1][nbcol-1]=3 #opérateur: 1: <= ; 2: >= ; 3: =

#Contrainte n°2
tab[2][1]=0
tab[2][2]=1
tab[2][3]=0
tab[2][4]=1
tab[2][nbcol-3]=300
tab[2][nbcol-1]=3

#Contrainte n°3
tab[3][1]=1
tab[3][2]=1
tab[3][3]=0
tab[3][4]=0
tab[3][nbcol-3]=400
tab[3][nbcol-1]=1

#Contrainte n°4
tab[4][1]=0
tab[4][2]=0
tab[4][3]=1
tab[4][4]=1
tab[4][nbcol-3]=300
tab[4][nbcol-1]=1

#On initialise le système
tab=b.initialiseSysteme(tab, nbcontr, nbvar, nbrow, nbcol)

#On fait les opérations de BigM avec le svariables artificielles
tab=b.ope_bigm(tab, nbvar, nbcontr, nbrow, nbcol)

#On effectue les opérations élémentaires de pivot
tab=b.ope_elem(tab, nbrow, nbcol,nbvar,nbcontr)
    