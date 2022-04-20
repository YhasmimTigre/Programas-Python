# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:26:57 2021

@author: Yhasmim
"""
num = int 
num = 1
soma = 0
while (num  <= 500):
    num = num + 1
    if (num % 2 == 0):
        continue
    elif(num % 3 == 0):
        soma = soma + num 
    else:
        continue
    
print(soma)        

input()