# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 21:43:28 2021

@author: Yhasmim
"""


num = int(input("digite um numero inteiro: "))

primeiro = 1
segundo = 1
terceiro = 0

print("Sequencia de Fibonacci")
print(primeiro)
print(segundo)

for i in range (num -2):
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
    print(terceiro)