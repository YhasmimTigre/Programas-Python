# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:57:37 2021

@author: Yhasmim
"""
print("digite números")
num = int
soma = 0
menor = None
maior = None 
while (num != -1):
    num = input()
    num = int(num)
    if maior is None:
        maior = num
    elif num > maior:
        maior = num
    if menor is None:
            menor = num
    elif num < menor:
            menor = num
    soma = soma + num  
print( 'menor:', menor)
print( 'maior:', maior)
print( 'soma:', soma)

input()