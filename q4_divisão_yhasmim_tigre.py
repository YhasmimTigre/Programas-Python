# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 21:49:16 2021

@author: Yhasmim
"""
print("digite o numerador número:")
x = input()
x = float(x)
print("digite o denominador número:")
y = input()
y = float (y)
divisao = 0
while (x >= y):
    divisao = divisao + 1
    x = x - y
    if (x <= y):
        n = x 
        n = y - n
print("divisão:", divisao )
print("resto de divisão:", x)

input()
