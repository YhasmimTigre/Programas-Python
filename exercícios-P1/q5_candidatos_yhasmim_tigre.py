# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:52:42 2021

@author: Yhasmim
"""

num_eleitores = int(input("Qual o numero total de eleitores? "))

print( "para votar no candidato 1 digite numero 1")
print( "para votar no candidato 2 digite numero 2")
print( "para votar no candidato 3 digite numero 3")

voto_1 = 0
voto_2 = 0
voto_3 = 0
voto = 0
nulos = 0

for i in range (num_eleitores):
     voto = int(input("digite os votos obedecendo a regra: "))  

     if (voto == 1):
        voto_1 = voto_1 +1 
    
     elif (voto == 2):
         voto_2 = voto_2 +1         

     elif (voto == 3):
         voto_2 = voto_2 +1
    
     else:
         nulos = nulos + 1
         print ("voto nulo")    
    
print("votos do candidado 1 :", voto_1)
print("votos do candidado 2 :", voto_2)
print("votos do candidado 3 :", voto_3)
print("votos nulos : ", nulos)