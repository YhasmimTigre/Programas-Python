# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:19:14 2021

@author: Yhasmim
"""
total = 0
cod_prod = 1
preco = 0
while (cod_prod != 0):
    print("digite o codigo do produto")
    cod_prod = input()
    cod_prod = float(cod_prod)
    quant_comp = 0
    if (cod_prod == 0):
        break
    if (cod_prod == 1):
        print("quantidade comprada")
        quant_comp = input()
        quant_comp = float(quant_comp)
        preco = 5.50
    elif (cod_prod == 2):
        print("quantidade comprada")
        quant_comp = input()
        quant_comp = float(quant_comp)
        preco = 2.30
    elif (cod_prod == 3):
        print("quantidade comprada")
        quant_comp = input()
        quant_comp = float(quant_comp)
        preco = 4.75
    elif (cod_prod == 4):
        print("quantidade comprada")
        quant_comp = input()
        quant_comp = float(quant_comp)
        preco = 6.80
    elif (cod_prod == 5):
        print("quantidade comprada")
        quant_comp = input()
        quant_comp = float(quant_comp)
        preco = 9.30
    else:
        print("código Inválido")
    total = quant_comp*preco + total
print(f"total da compra: {total:.2f}")  

input()
     
