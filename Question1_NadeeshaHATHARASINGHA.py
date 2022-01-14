# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 01:08:49 2022

@author: nadee
"""

import Bigm as b



#Question 1: 3 variables décisionnelles et 3 contraintes "<=" --> Simplex
"""    Maximiser Z : 11x1 + 16x2 + 15x3
        s.c :
                A :  x1 + 2x2 + 3/2x3 <= 12 000 
    	        B : 2/3 x1 + 2/3 x2+ x3 <= 4600 
    	        C : 1/2 x1 + 1/3 x2 + 1/2 x3 <= 2400

            
"""
#Cliquez sur 'Run' pour voir les itérations et le résultat de la méthode Simplex 

#Tests
print("\n Simplex: 3 variables et 3 contraintes \n")
print("------------------------------------------------------------------------------------")

#Expr(name, id, maxi, cx1, cx2, cx3, cz, op, cb)

# Expression de Z
print("Expression de Z:")
Z = b.Expr("Z", 0, 1, 11, 16, 15, 1, 3,0 )
print("------------------------------------------------------------------------------------")

# Expression de c1
print("Expression de la première contrainte A:")
A = b.Expr("A", 1, 1, 1, 2 , 1.5, 0, 1, 12000 )
print(A.op)

print("------------------------------------------------------------------------------------")

# Expression de c2
print("Expression de la deuxième contrainte B:")
B = b.Expr("B", 2, 1, 0.666, 0.666, 1, 0, 1,4600)
print(B.op)

print("------------------------------------------------------------------------------------")

# Expression de c3
print("Expression de la deuxième contrainte C:")
C = b.Expr("C", 3, 1, 0.5, 0.333, 0.5, 0, 1, 2400)
print(C.op)

print("------------------------------------------------------------------------------------")

# Systeme
sys = b.Systeme(Z, A, B, C)
affGen = sys.affichageGeneral()
print(affGen)
affCan = sys.affichageCanonique()
print(affCan)
sys.ope_bigm()
sys.ope_elem()


 