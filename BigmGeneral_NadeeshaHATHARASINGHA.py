# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:37:20 2021

@author: nadee
"""

import numpy as np
import math
   
M= 10** 9
 
def inputSysteme(tab, nbcol, nbvar, nbcontr):
    tab[0][0]=1
#tab[0]-->z, tab[1]-->x1, tab[2]-->x2, tab[n]-->xn, tab[n+1]-->c1,tab[n+m] -->cm, tab[n+m+1]=a1, tab[n+m+l]=al, tab[col-3]=b, tab[col-2]=Lipivot ou pas, tab[col-1]-->opérateur 
    
    for i in range (1, nbvar+1):
        res= int(input("Veuillez saisir le coefficient de la variable de décision n°"+ str(i) +" de l'expression de Z: "))
        tab[0][i]= res *-1

    for j in range (1, nbcontr+1):        
        for k in range (1, nbvar+1):
            res= int(input("Veuillez saisir le coefficient de la variable de décision n°"+ str(k) +" de la contrainte n°" + str(j) + ": "))
            tab[j][k]= res
        op= int(input("Choississez le type d'opérateur: \n 1.<= \n 2.>= \n 3.= \n "))
        res2= int(input("Veuillez saisir la valeur après l'inégalité <= de la contrainte n°" + str(j) + ": "))
        tab[j][nbcol-3]= res2  
        tab[j][nbcol-1]= op  
        

    return tab

def initialiseSysteme(tab, nbcontr, nbvar, nbrow, nbcol):
    col= nbvar+1
    for row in range (1, nbrow):
        if tab[row][nbcol-1]==1: #op --> "<="
            tab[row][col]=1
        elif tab[row][nbcol-1]==2: #op --> ">="
            tab[row][col] = -1
            tab[row][col+nbcontr] = 1 #var artificielle de la contrainte row
            tab[0][col+nbcontr] = M #var artificielle de z    
        else:
            tab[row][col+nbcontr] = 1 #var artificielle de la contrainte row
            tab[0][col+nbcontr] = M #var artificielle de z  
        col+=1
        
        
    print("Forme canonique:\n")
    for j in range(nbrow):
        for i in range (nbcol-2):
            print(str(round(tab[j][i],2)),end="  ")
        print("\n")
        
    return tab
    
def findpivot(tab,nbcontr,nbcol):
        # On choisit la colonne du pivot en choisissant la plus petite valeur de z sans la valeur après l'égalité
    new_li=[]
    for i in range (1, nbcol-3):
        new_li.append(tab[0][i])        
    indcolpivot = new_li.index(min(new_li)) +1
    
    # On choisit la ligne du pivot: on fait le quotient de b et du coeff de la colonne pivot de chaque contrainte A, B et/ou C

     # Selon si elles ont déjà été pivots ou pas, on ajoute l'id de la ligne en tant que clé  du dico q et la valeur du quotient en tant que valeur
    q=dict()
    
    for i in range (1,nbcontr+1):
        if tab[i][indcolpivot]!=0 and tab[i][nbcol-2]==0:
            r = tab[i][nbcol-3] / tab[i][indcolpivot]
            q[str(i)]= r


        
    #On récupère le minimum de ces quotients   
    # print(q)
    minimum= min(q.values())
    
    #On récupère la clé de la valeur minimum dans le dico qui deviendra ainsi la ligne du pivot
    for k, val in q.items(): 
        if minimum == val: 
            indlipivot= int(k)
                
    #On actualise le statut de ligne pivot pour la ligne concernée        
    tab[indlipivot][nbcol-2]=1
            
         #On recupère le pivot    
    pivot = tab[indlipivot][indcolpivot]
    print("Indice de la ligne pivot= ", indlipivot)
    print("Indice de la colonne pivot= ", indcolpivot)
    print("pivot= ", pivot)
        
    return indcolpivot, indlipivot, pivot


def optimisable(tab, nbcol):
    #On vérifie qu'il n'y a pas de valeurs négatives dans la fonction z
    type(tab)
    for i in range (1, nbcol-3):
        if tab[0][i]<0:
            return True
    return False

def ope_elem_unit(tab, pivot, indlipivot, indcolpivot, indlicontr ,nbcol):

    newli = []
    lipivot = tab[indlipivot]
    licontr = tab[indlicontr]
    #print("Licontr: ", licontr)
    q= tab[indlicontr][indcolpivot]/pivot
    # print("q= ", q)
    
    #Si ligne de pivot: newL--> Lp/p
    if indlipivot == indlicontr:
        for i in range(nbcol-2):
            newli.append(lipivot[i]/pivot)
        newli.append(lipivot[nbcol-2])
        newli.append(lipivot[nbcol-1])
        # print("Ligne Pivot=", newli)

        return newli
    #Sinon newL--> L - coefflp/p * Lp
    else: 
        for i in range(nbcol-2):
            newli.append(licontr[i] - q * lipivot[i])
        newli.append(licontr[nbcol-2])
        newli.append(lipivot[nbcol-1])
        # print("Contrainte n°"+str(indlicontr+1)+"=", newli)

        return newli
    
    
   
def ope_elem(tab,nbrow,nbcol,nbvar,nbcontr):
    #On réitère le processus tant que Z est optimisable
    count=0
    while(optimisable(tab, nbcol)):
        newtab=[]
        indcolpivot, indlipivot, pivot = findpivot(tab, nbcontr, nbcol)       
        for i in range(0,nbrow):
            newli = ope_elem_unit(tab, pivot, indlipivot, indcolpivot, i, nbcol)
            newtab.append(newli)
        tab=newtab
        count= count + 1
        print("\n------------------------------------------------------------------------------------")
        print("\n Itération n°" + str(count)+ ": \n")
        for j in range(nbrow):
            for i in range (nbcol-2):
                print(str(round(tab[j][i],2)),end="  ")
            print("\n")
        if count>=nbcontr:
            print("\n Ce système n'a pas de solution ou des solutions infinie.")
            return tab
    print("\n Nous avons la solution finale suivante: \n Z=", tab[0][nbcol-3])
    return tab
        
    
        
def ope_unit_bigm(tab,j):
    
    newz=[]
    z= tab[0]
    licontr = tab[j]
    k=0
    for i in z:
        newz.append(i - M * licontr[k])
        k=k+1
    return newz

def ope_bigm(tab,nbvar,nbcontr):
    
    j=1
    count=1
    while j<=nbcontr:
        if tab[j][nbvar+nbcontr+j]!=0:
            print("\n------------------------------------------------------------------------------------")
            print("\n Big M: Transformation n°"+ str(count) + " de Z: ")
            newz= ope_unit_bigm(tab,j)
            tab[0]=newz
            count=count+1
        
        j= j+1   
    for k in range(nbrow):
        for l in range (nbcol-2):
            print(str(round(tab[k][l],2)),end="  ")
        print("\n")
    return tab
 

            
#Simplex et BigM pour plusieurs variables 

# Pour tester variable en input--> Décommenter les deux lignes en-dessous 
nbvar=int(input("Veuillez saisir le nombre de variables de décision souhaités: "))
nbcontr=int(input("Veuillez saisir le nombre de contraintes souhaités: "))

#Exemple: 3 variable/3 contraintes 
# Pour tester variable en input--> Commenter les 2 lignes en dessous
# nbvar=2
# nbcontr=3

#nombre de colonnes= colonne z + nombre de variables de decision + nombre de contraintes + variable artificielles + après égalité + opérateur + booleen ligne pivot ou non
nbcol= 1 + nbvar + (nbcontr*2) + 1 + 1 + 1
#tab[0]-->z, tab[1]-->x1, tab[2]-->x2, tab[n]-->xn, tab[n+1]-->c1,tab[n+m] -->cm, tab[n+m+1]=a1, tab[n+m+l]=al, tab[col-3]=b, tab[col-2]=opérateur, tab[col-1]-->Lipivot ou pas
#nombre de lignes = nombre de contraintes +1 
nbrow= nbcontr + 1

#On crée une matrice de 0 
tab= np.zeros((nbrow,nbcol))

#Pour récupérer les coefficients  par input --> decommenter la ligne en dessous
tab=inputSysteme(tab, nbcol, nbvar, nbcontr)

#Exemple de valeurs pour 2 variables et 3 contraintes
#Pour tester avec input, commentez le paragraphe en-dessous
# #Z
# tab[0][0]=1
# tab[0][1]=-3
# tab[0][2]=-5
# tab[0][nbcol-3]=0

# #Contrainte n°1
# tab[1][1]=1
# tab[1][2]=1
# tab[1][nbcol-3]=2
# tab[1][nbcol-1]=2

# #Contrainte n°2
# tab[2][1]=0
# tab[2][2]=1
# tab[2][nbcol-3]=6
# tab[2][nbcol-1]=1

# #Contrainte n°3
# tab[3][1]=3
# tab[3][2]=2
# tab[3][nbcol-3]=18
# tab[3][nbcol-1]=3

#On initialise le système
tab=initialiseSysteme(tab, nbcontr, nbvar, nbrow, nbcol)

#On fait les opérations de BigM avec le svariables artificielles
tab=ope_bigm(tab, nbvar, nbcontr)

#On effectue les opérations élémentaires de pivot
tab=ope_elem(tab, nbrow, nbcol,nbvar,nbcontr)
    