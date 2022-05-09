
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:21:34 2021

@author: Yhasmim
"""
print("Bem-Vindo")

print("Qual o deposito inicial?")
dep_inicial = float(input())

print("Qual a taxa de juros da poupança?")
taxa_juros = float(input())

taxa_mensal = dep_inicial

print("Valores mês a mês para os 24 primeiros meses:")

for i in range (24):
     taxa_mensal = taxa_mensal*(taxa_juros/100 +1)
     print("mês", i+1, ":", "%.2f" % taxa_mensal)
print ("total ganho com juros:", "%.2f" % taxa_mensal)    

input()