# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:12:47 2021

@author: Yhasmim
"""

print ("quanto você ganha por hora?")
salario_hora = input()
print ("qual o numero de horas trabalhadas no mês?")
hora = input()
salario_hora = float (salario_hora)
hora = float (hora)
salario_bruto = salario_hora*hora 
ir = (11/100)*salario_bruto
inss = (8/100)*salario_bruto
sind = (5/100)*salario_bruto
salario_liquido = salario_bruto - (ir + inss + sind)
print("Salário Bruto: R$" , salario_bruto)
print("IR (11%): R$" , ir)
print("INSS (8%): R$" , inss)
print("Sindicato (5%): R$" , sind)
print("Salário Liquido: R$" , salario_liquido)

 
input()
