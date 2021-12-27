# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 12:37:20 2021

@author: nadee
"""

import numpy as np
import math
    
def inputSysteme(tab, nbcol, nbvar, nbcontr):
    tab[0][0]=1
    
    for i in range (1, nbvar+1):
        res= int(input("Veuillez saisir le coefficient de la variable de décision n°"+ str(i) +" de l'expression de Z: "))
        tab[0][i]= res *-1

    for j in range (1, nbcontr+1):        
        for k in range (1, nbvar+1):
            res= int(input("Veuillez saisir le coefficient de la variable de décision n°"+ str(k) +" de la contrainte n°" + str(j) + ": "))
            tab[j][k]= res  
        res2= int(input("Veuillez saisir la valeur après l'inégalité <= de la contrainte n°" + str(j) + ": "))
        tab[j][nbcol-2]= res2  

    return tab

def initialiseSysteme(tab, nbvar, nbrow, nbcol):
    col= nbvar+1
    for row in range (1, nbrow):
        tab[row][col]=1
        col+=1
    print("Itération n°0:\n")
    for j in range(nbrow):
        for i in range (nbcol-1):
            print(str(round(tab[j][i],2)),end="  ")
        print("\n")
    return tab
    
def findpivot(tab,nbcontr,nbcol):
        # On choisit la colonne du pivot en choisissant la plus petite valeur de z sans la valeur après l'égalité
    new_li=[]
    for i in range (1, nbcol):
        new_li.append(tab[0][i])        
    indcolpivot = new_li.index(min(new_li)) +1
    
    # On choisit la ligne du pivot: on fait le quotient de b et du coeff de la colonne pivot de chaque contrainte A, B et/ou C

     # Selon si elles ont déjà été pivots ou pas, on ajoute l'id de la ligne en tant que clé  du dico q et la valeur du quotient en tant que valeur
    q=dict()
    
    for i in range (1,nbcontr+1):
        if tab[i][indcolpivot]!=0 and tab[i][nbcol-1]==0:
            r = tab[i][nbcol-2] / tab[i][indcolpivot]
            q[str(i)]= r


        
    #On récupère le minimum de ces quotients   
    # print(q)
    minimum= min(q.values())
    
    #On récupère la clé de la valeur minimum dans le dico qui deviendra ainsi la ligne du pivot
    for k, val in q.items(): 
        if minimum == val: 
            indlipivot= int(k)
                
    #On actualise le statut de ligne pivot pour la ligne concernée        
    tab[indlipivot][nbcol-1]=1
            
         #On recupère le pivot    
    pivot = tab[indlipivot][indcolpivot]
    print("Indice de la ligne pivot= ", indlipivot)
    print("Indice de la colonne pivot= ", indcolpivot)
    print("pivot= ", pivot)
        
    return indcolpivot, indlipivot, pivot


def optimisable(tab, nbcol):
    #On vérifie qu'il n'y a pas de valeurs négatives dans la fonction z
    type(tab)
    for i in range (1, nbcol-2):
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
        for i in range(nbcol-1):
            newli.append(lipivot[i]/pivot)
        #print("New ligne=", newli)
        newli.append(lipivot[nbcol-1])
        return newli
    #Sinon newL--> L - coefflp/p * Lp
    else: 
        j=0
        for i in range(nbcol-1):
            newli.append(licontr[i] - q * lipivot[j])
            j= j+1
        #print("New ligne=", newli)
        newli.append(licontr[nbcol-1])
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
            for i in range (nbcol-1):
                print(str(round(tab[j][i],2)),end="  ")
            print("\n")
        if count==nbcontr:
            print("\n Nous avons la solution finale suivante: \n Z=", tab[0][nbcol-2])
            return tab
        
    
# def ope_elem(tab,nbcol,nbvar,nbcontr):
#     #On réitère le processus tant que Z est optimisable
#     count=0
#     while(optimisable(tab, nbcol)):
#         indcolpivot, indlipivot, pivot = findpivot(tab, nbcontr, nbcol)
#         newz = ope_elem_unit(tab, pivot, indlipivot, indcolpivot, 0, nbcol)
#         newa = ope_elem_unit(tab, pivot, indlipivot, indcolpivot, 1, nbcol)
#         newb = ope_elem_unit(tab, pivot, indlipivot, indcolpivot, 2, nbcol)
#         newc = ope_elem_unit(tab, pivot, indlipivot, indcolpivot, 3, nbcol)
#         tab=actualiseSys(newz, newa, newb, newc)
#         count= count + 1
#         print("\n------------------------------------------------------------------------------------")
#         print("\n Itération n°" + str(count)+ ": \n")
#         print(tab)
#         if count==nbcontr:
#             print("\n Nous avons la solution finale suivante: \n Z=", tab[0][nbcol-2])
#             return tab
        
    # def ope_unit_bigm(self, j):
        
    #     newz=[]
    #     z= self.ligne[0]
    #     licontr = self.ligne[j]
    #     k=0
    #     for i in z:
    #         newz.append(i - self.M * licontr[k])
    #         k=k+1
    #     print("New Z=", newz)
    #     print(licontr)
    #     return newz
    
    # def ope_bigm(self):
        
    #     j=1
    #     while j<=3:
    #         if self.ligne[j][7]!=0 or self.ligne[j][8]!=0 or self.ligne[j][9]!=0:
    #             newz= self.ope_unit_bigm(j)
    #             self.actualiseSys(newz, self.a.col, self.b.col, self.c.col)
    #             print("\n------------------------------------------------------------------------------------")
    #             print("\n Big M: Transformaion n°"+ str(j) + " de Z: ")
    #             affCan = sys.affichageCanonique()
    #             print(affCan)
    #         j= j+1
     

            
#Simplex et BigM pour plusieurs variables 

# Pour tester variable en input--> Décommenter les deux lignes en-dessous 
# nbvar=int(input("Veuillez saisir le nombre de variables de décision souhaités: "))
# nbcontr=int(input("Veuillez saisir le nombre de contraintes souhaités: "))

#Exemple: 3 variable/3 contraintes 
# Pour tester variable en input--> Commenter les 2 lignes en dessous
nbvar=3
nbcontr=3

#nombre de colonnes= nombre de variables de decision + nombre de contraintes ( + colonne z + après égalité) + booleen qui affiche si a été ligne pivot ou non
nbcol= nbvar + nbcontr + 1 + 1 + 1
#nombre de lignes = nombre de contraintes +1 
nbrow= nbcontr + 1

#On crée une matrice de 0 
tab= np.zeros((nbrow,nbcol))

#Pour récupérer les coefficients  par input --> decommenter la ligne en dessous
# tab=inputSysteme(tab, nbcol, nbvar, nbcontr)

#Exemple de valeurs pour 3 variables et 3 contraintes
#Pour tester avec input, commentez le paragraphe en-dessous
#Z
tab[0][0]=1
tab[0][1]=-4
tab[0][2]=1
tab[0][3]=-2
tab[0][nbcol-2]=0

#Contrainte n°1
tab[1][1]=2
tab[1][2]=1
tab[1][3]=2
tab[1][nbcol-2]=6

#Contrainte n°2
tab[2][1]=1
tab[2][2]=-4
tab[2][3]=2
tab[2][nbcol-2]=0

#Contrainte n°3
tab[3][1]=5
tab[3][2]=-2
tab[3][3]=-2
tab[3][nbcol-2]=4

#On initialise le système
tab=initialiseSysteme(tab, nbvar, nbrow, nbcol)

#On cherche le pivot:
tab=ope_elem(tab, nbrow, nbcol,nbvar,nbcontr)
    