# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 22:19:56 2021

@author: Yhasmim
"""

num = int(input("vamos verificar se um numero é primo! Digite o numero: "))

divisão = 0

for i in range (2,num):
   resultado = num %  i
    
   if(resultado == 0):
       print("esse numero não é primo")
       break
   elif(i == num-1):
       print("esse numero é primo")        
   else:
       continue

if(num == 2):
    print("esse numero é primo")