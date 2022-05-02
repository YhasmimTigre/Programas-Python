# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:32:07 2021

@author: Yhasmim
"""

print("qual a raiz quadrada a ser calculada?")
n = input()
n = float(n)
b = 2
p = (b + (n/b))/2
while ((abs (b - p)) > 0.0001):
     b = p
     p = (b + (n/b))/2
     
print("o valor aproximado da raiz quadrada é:", b)

input()
