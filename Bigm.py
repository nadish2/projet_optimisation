# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:04:46 2021

@author: nadee
"""

    
#BigM pour 3 variables et 3 contraintes
class Expr:


    def __init__(self, name, id, cz):
        self.name = name
        self.id = id
        self.cz = cz
        self.cx1 = int(input("Veuillez entrer le coefficient de x1: "))
        self.cx2 = int(input("Veuillez entrer le coefficient de x2: "))
        self.cx3 = int(input("Veuillez entrer le coefficient de x3: "))

        if self.cz == 1:
            self.cb = 0
            self.cx1 = self.cx1 * -1
            self.cx2 = self.cx2 * -1
            self.cx3 = self.cx3 * -1
        else:
            self.op= int(input("Choississez le type d'opérateur: \n 1.<= \n 2.>= \n 3.= \n "))
            self.cb=int(input("Veuillez entrer le coefficient de b: "))  
        self.pivot= False   
        # Indices tableaux: z --> 0, cx1-->1, cx2-->2, cx3-->3, ce1-->4, ce2-->5, ce3 -->6, ca1--> 7, ca2-->8, ca3-->9, cb->10
        self.col= [self.cz,self.cx1, self.cx2, self.cx3, 0, 0, 0, 0, 0, 0, self.cb]
        
    def affichageGeneral(self):           
        if self.cz == 1:
            res = self.name + "= " + str(self.col[1] * -1) + "x1 + " + str(
                self.col[2]  * -1) + "x2 + " + str(self.col[3]  * -1) + "x3  "
        else:
            if self.op == 1:
                ope = '<='
            elif self.op ==2:
                ope = ">="
            else:
                ope = "=" 
            res = self.name + ": " + str(self.col[1] ) + "x1 + " + str(
                self.col[2] ) + "x2 + " + str(self.col[3] ) + "x3" + ope + str(self.col[10] )

        return res

    def affichageCanonique(self):
                
        if self.cz == 1:
            res = self.name + ": " + str(self.cz) + "z + " + str(self.col[1] ) + "x1 + " + str(self.col[2] ) + "x2 + " + str(
                self.col[3] ) + "x3 + " + str(self.col[4] ) + "e1 + " + str(self.col[5] ) + "e2 + " + str(self.col[6] ) + "e3 + " + str(self.col[7] ) + "a1 + " + str(self.col[8]) + "a2 + " + str(self.col[9]) + "a3 = " + str(self.col[10]) 

        else:
            res = self.name + ": " + str(self.cz) + "z + " + str(self.col[1] ) + "x1 + " + str(self.col[2] ) + "x2 + " + str(
                self.col[3] ) + "x3 + " + str(self.col[4] ) + "e1 + " + str(self.col[5] ) + "e2 + " + str(self.col[6] ) + "e3 + " + str(self.col[7] ) + "a1 + " + str(self.col[8]) + "a2 + " + str(self.col[9]) + "a3 = " + str(self.col[10]) 

        return res


class Systeme:
    
    def __init__(self, expr1, expr2, expr3, expr4):
        self.M= 10** 12

        self.z = expr1
        self.a = expr2
        self.b = expr3
        self.c = expr4
        self.z.col[10] = 0
       
        # Indices tableau col: z --> 0, cx1-->1, cx2-->2, cx3-->3, ce1-->4, ce2-->5, ce3 -->6, ca1--> 7, ca2-->8, ca3-->9, cb->10
        
        if self.a.op==1: #<=
            self.a.col[4] = 1
            print(self.a.col[4])
        elif self.a.op==2:#>=
            self.a.col[4] = -1
            self.a.col[7]= 1
            self.z.col[7]= self.M
        else: #=
            self.a.col[7] = 1
            self.z.col[7]= self.M


        if self.b.op==1:
            self.b.col[5] = 1

        elif self.b.op==2:
            self.b.col[5] = -1
            self.b.col[8]= 1
            self.z.col[8]= self.M

        else:
            self.b.col[8] = 1
            self.z.col[8]= self.M


        if self.c.op==1:
            self.c.col[6] = 1

        elif self.c.op==2:
            self.c.col[6] = -1
            self.c.col[9]= 1
            self.z.col[9]= self.M

        else:
            self.c.col[9] = 1
            self.z.col[9]= self.M

        
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
        # On choisit la colonne du pivot en choisissant la plus petite valeur de z sans la valeur cb après l'égalité
        new_li=[]
        for i in range (0, len(self.z.col)-1):
            new_li.append(self.z.col[i])        
        indcolpivot = new_li.index(min(new_li))
        print(indcolpivot)
        # On choisit la ligne du pivot: on fait le quotient de b et du coeff de la colonne pivot de chaque contrainte A, B et/ou C

        # Selon si elles ont déjà été pivots ou pas, on ajoute l'id de la ligne en tant que clé  du dico q et la valeur du quotient en tant que valeur
        q=dict()
        
        if not(self.a.pivot) and self.a.col[indcolpivot]!=0:
            q1 = self.a.col[10] / self.a.col[indcolpivot]
            q[self.a.id]= q1
            
        if not(self.b.pivot) and self.b.col[indcolpivot]!=0 :
            q2 = self.b.col[10] / self.b.col[indcolpivot]
            q[self.b.id]= q2
            
        if not(self.c.pivot) and self.c.col[indcolpivot]!=0:            
            q3 = self.c.col[10] / self.c.col[indcolpivot]
            q[self.c.id]= q3
            
       #On récupère le minimum de ces quotients   
        print(q)
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
        print("Z= ",self.z.col[10])
        print("Variables basiques: e1, e2, e3")
        print("Variables non-basiques: x1, x2, x3")
        
    def ope_unit_bigm(self, j):
        
        newz=[]
        z= self.ligne[0]
        licontr = self.ligne[j]
        k=0
        for i in z:
            newz.append(i - self.M * licontr[k])
            k=k+1
        print("New Z=", newz)
        print(licontr)
        return newz
    
    def ope_bigm(self):
        
        j=1
        while j<=3:
            if self.ligne[j][7]!=0 or self.ligne[j][8]!=0 or self.ligne[j][9]!=0:
                newz= self.ope_unit_bigm(j)
                self.actualiseSys(newz, self.a.col, self.b.col, self.c.col)
                print("\n------------------------------------------------------------------------------------")
                print("\n Big M: Transformaion n°"+ str(j) + " de Z: ")
                affCan = sys.affichageCanonique()
                print(affCan)
            j= j+1
     

#Tests
print("\n BigM: 3 variables et 3 contraintes \n")
print("------------------------------------------------------------------------------------")

# Expression de Z
print("Expression de Z:")
Z = Expr("Z", 0, 1)
print("------------------------------------------------------------------------------------")

# Expression de c1
print("Expression de la première contrainte A:")
A = Expr("A", 1, 0)
print(A.op)

print("------------------------------------------------------------------------------------")

# Expression de c2
print("Expression de la deuxième contrainte B:")
B = Expr("B", 2, 0)
print(B.op)

print("------------------------------------------------------------------------------------")

# Expression de c3
print("Expression de la deuxième contrainte C:")
C = Expr("C", 3, 0)
print(C.op)

print("------------------------------------------------------------------------------------")

# Systeme
sys = Systeme(Z, A, B, C)
affGen = sys.affichageGeneral()
print(affGen)
affCan = sys.affichageCanonique()
print(affCan)
sys.ope_bigm()
sys.ope_elem()


 