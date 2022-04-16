# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:12:12 2021

@author: Yhasmim
"""

print ("qual a sua altura?")
h = input()
print ("você é homem ou mulher?")
sexo = input()
h = float (h)
if (sexo == 'mulher'):
    peso = (62.1*h) - 44.7
    print ("o seu peso ideal é:", peso)
elif (sexo == 'homem'):
    peso = (72.7*h) - 58
    print ("o seu peso ideal é:", peso)         
else: 
    print ("sexo não definido")   
input()