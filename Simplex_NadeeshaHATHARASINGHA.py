# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:23:22 2021

@author: nadee
"""

#Simplex pour 3 variables et 3 contraintes
class Expr:
   #nombre de ligne = nombre contrainte +1 
  #nombre de colonnes= nb de var de decision + nb de contraintes
   
    def __init__(self, name, id, cz):
        self.name = name
        self.id = id
        self.cz = cz
        cx1 = int(input("Veuillez entrer le coefficient de x1: "))
        cx2 = int(input("Veuillez entrer le coefficient de x2: "))
        cx3 = int(input("Veuillez entrer le coefficient de x3: "))
        if self.cz == 1:
            cb = 0
            cx1 = cx1 * -1
            cx2 = cx2 * -1
            cx3 = cx3 * -1
        else:
            cb=int(input("Veuillez entrer le coefficient de b: "))
        self.pivot= False   
        # Indices tableaux: z --> 0, cx1-->1, cx2-->2, cx3-->3, ce1-->4, ce2-->5, ce3 -->6, cb--> 7
        self.col = [self.cz, cx1, cx2, cx3, 0, 0, 0, cb]


    def affichageGeneral(self):
        if self.cz == 1:
            res = self.name + "= " + str(self.col[1] * -1) + "x1 + " + str(
                self.col[2]  * -1) + "x2 + " + str(self.col[3]  * -1) + "x3  "
        else:
            res = self.name + ": " + str(self.col[1] ) + "x1 + " + str(
                self.col[2] ) + "x2 + " + str(self.col[3] ) + "x3 <= " + str(self.col[7] )

        return res

    def affichageCanonique(self):
        if self.cz == 1:
            res = self.name + ": " + str(self.cz) + "z + " + str(self.col[1] ) + "x1 + " + str(self.col[2] ) + "x2 + " + str(
                self.col[3] ) + "x3 + " + str(self.col[4] ) + "e1 + " + str(self.col[5] ) + "e2 + " + str(self.col[6] ) + "e3 = " + str(self.col[7] )
        else:
            res = self.name + ": " + str(self.cz) + "z + " + str(self.col[1] ) + "x1 + " + str(self.col[2] ) + "x2 + " + str(
                self.col[3] ) + "x3 + " + str(self.col[4] ) + "e1 + " + str(self.col[5] ) + "e2 + " + str(self.col[6] ) + "e3 = " + str(self.col[7] )

        return res


class Systeme:
    def __init__(self, expr1, expr2, expr3, expr4):
        self.z = expr1
        self.a = expr2
        self.b = expr3
        self.c = expr4
        self.z.col[7] = 0
        self.a.col[4] = 1
        self.b.col[5] = 1
        self.c.col[6] = 1
        # Indices lignes: Z--> 0, A-->1, B-->2, C-->3
        self.ligne = [self.z.col, self.a.col, self.b.col, self.c.col]

    def affichageGeneral(self):
        print(" \n Forme générale")
        Z = self.z.affichageGeneral()
        A = self.a.affichageGeneral()
        B = self.b.affichageGeneral()
        C = self.c.affichageGeneral()
        res = Z + "\n" + A + "\n" + B + "\n" + C
        return res

    def affichageCanonique(self):
        print("\n Forme Canonique")
        Z = self.z.affichageCanonique()
        A = self.a.affichageCanonique()
        B = self.b.affichageCanonique()
        C = self.c.affichageCanonique()
        res = Z + "\n" + A + "\n" + B + "\n" + C
        return res

    def actualiseSys(self, z, a, b, c):
        self.z.col= z
        self.a.col = a
        self.b.col= b
        self.c.col= c        
        self.ligne = [z, a, b, c]

    def pivot(self):
        # On choisit la colonne du pivot
        indcolpivot = self.z.col.index(min(self.z.col))

        # On choisit la ligne du pivot: on fait le quotient de b et du coeff de la colonne pivot de chaque contrainte A, B et/ou C

        # Selon si elles ont déjà été pivots ou pas, on ajoute l'id de la ligne en tant que clé  du dico q et la valeur du quotient en tant que valeur
        q=dict()
        
        if not(self.a.pivot):
            q1 = self.a.col[7] / self.a.col[indcolpivot]
            q[self.a.id]= q1
            
        if not(self.b.pivot):
            q2 = self.b.col[7] / self.b.col[indcolpivot]
            q[self.b.id]= q2
            
        if not(self.c.pivot):            
            q3 = self.c.col[7] / self.c.col[indcolpivot]
            q[self.c.id]= q3
            
       #On récupère le minimum de ces quotients     
        minimum= min(q.values())

        #On récupère la clé de la valeur minimum dans le dico qui deviendra ainsi la ligne du pivot
        for k, val in q.items(): 
            if minimum == val: 
                indlipivot= int(k)
        #On actualise le statut de ligne pivot pour la ligne concernée        
        if self.a.id == indlipivot:
            self.a.pivot = True
        if self.b.id == indlipivot:
            self.b.pivot = True        
        if self.c.id == indlipivot:
            self.c.pivot = True    
        #On recupère le pivot    
        pivot = self.ligne[indlipivot][indcolpivot]
        print("Indice de la ligne pivot= ", indlipivot)
        print("Indice de la colonne pivot= ", indcolpivot)
        print("pivot= ", pivot)
        
        return indcolpivot, indlipivot, pivot
    
    def optimisable(self):
        #On vérifie qu'il n'y a pas de valeurs négatives dans la fonction z
        for i in self.z.col:
            if i<0:
                return True
        return False
    
    def ope_elem_unit(self, pivot, indlipivot, indcolpivot, indlicontr):

        newli = []
        lipivot = self.ligne[indlipivot]
        licontr = self.ligne[indlicontr]
        #print("Licontr: ", licontr)
        q= self.ligne[indlicontr][indcolpivot]/pivot
        # print("q= ", q)
        
        #Si ligne de pivot: newL--> Lp/p
        if indlipivot == indlicontr:
            for i in lipivot:
                newli.append(i/pivot)
            #print("New ligne=", newli)
            return newli
        #Sinon newL--> L - coefflp/p * Lp
        else: 
            j=0
            for i in licontr:
                newli.append(i - q * lipivot[j])
                j= j+1
            #print("New ligne=", newli)
            return newli
       
    def ope_elem(self):
        #On réitère le processus tant que Z est optimisable
        count=0
        while(self.optimisable()):
            indcolpivot, indlipivot, pivot = self.pivot()
            newz = self.ope_elem_unit(pivot, indlipivot, indcolpivot, 0)
            newa = self.ope_elem_unit(pivot, indlipivot, indcolpivot, 1)
            newb = self.ope_elem_unit(pivot, indlipivot, indcolpivot, 2)
            newc = self.ope_elem_unit(pivot, indlipivot, indcolpivot, 3)
            self.actualiseSys(newz, newa, newb, newc)
            count= count + 1
            print("\n------------------------------------------------------------------------------------")
            print("\n Itération n°: ", count)
            affCan = self.affichageCanonique()
            print(affCan)


        print("\n Solution finale trouvée au bout de ", count,"itérations. \n")
        print("Z= ",self.z.col[7])
        print("Variables basiques: x1, x2, x3")
        print("Variables non-basiques: e1, e2, e3")
        

#Tests
print("\n Simplex: 3 variables et 3 contraintes \n")
print("------------------------------------------------------------------------------------")

# Expression de Z
print("Expression de Z:")
Z = Expr("Z", 0, 1)
print("------------------------------------------------------------------------------------")

# Expression de c1
print("Expression de la première contrainte A:")
A = Expr("A", 1, 0)
print("------------------------------------------------------------------------------------")

# Expression de c2
print("Expression de la deuxième contrainte B:")
B = Expr("B", 2, 0)
print("------------------------------------------------------------------------------------")

# Expression de c3
print("Expression de la deuxième contrainte C:")
C = Expr("C", 3, 0)
print("------------------------------------------------------------------------------------")

# Systeme
sys = Systeme(Z, A, B, C)
affGen = sys.affichageGeneral()
print(affGen)
affCan = sys.affichageCanonique()
print(affCan)
sys.ope_elem()
