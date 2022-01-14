# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 01:13:26 2022

@author: nadee
"""


import Bigm as b


#Question 2: 2 variables décisionnelles et 3 contraintes ">="--> Méthode Big M

"""    Minimiser Z : 20000x1 + 25000x2 
        s.c :
               	A :  400x1 + 300x2 >= 25 000 
	            B :  300x1 + 400x2 >= 27 000 
	            C :  200 x1 + 500x2 >= 30 000 
            
"""
#Cliquez sur 'Run' pour voir les itérations et le résultat de la méthode Big M 

print("\n Simplex: 2 variables et 3 contraintes \n")
print("------------------------------------------------------------------------------------")


#Expr(name, id, maxi, cx1, cx2, cx3, cz, op, cb)

# Expression de Z
print("Expression de Z:")
Z = b.Expr("Z", 0, 0, 20000, 25000, 0, 1, 3,0 )
print("------------------------------------------------------------------------------------")

# Expression de c1
print("Expression de la première contrainte A:")
A = b.Expr("A", 1, 0, 400, 300 , 0, 0, 2, 25000 )
print(A.op)

print("------------------------------------------------------------------------------------")

# Expression de c2
print("Expression de la deuxième contrainte B:")
B = b.Expr("B", 2, 0, 300, 400, 0, 0, 2, 27000)
print(B.op)

print("------------------------------------------------------------------------------------")

# Expression de c3
print("Expression de la deuxième contrainte C:")
C = b.Expr("C", 3, 0, 200, 500, 0, 0, 2, 30000)
print(C.op)

print("------------------------------------------------------------------------------------")

# Systeme
# Systeme (FonctionZ, ContrainteA, ContrainteB, ContrainteC)

sys = b.Systeme(Z, A, B, C)
affGen = sys.affichageGeneral()
print(affGen)
affCan = sys.affichageCanonique()
print(affCan)
sys.ope_bigm()
sys.ope_elem()


 