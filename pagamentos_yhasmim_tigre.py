# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:20:25 2021

@author: Yhasmim
"""

print("Qual o valor da sua compra?")
valor = input()
valor = float(valor)
print("Qual a forma de pagamento?")
forma = input()
if (forma == 'cheque'):
    print("Pagamentos em cheque não recebem desconto. Valor da compra: R$", valor)
elif (forma == 'dinheiro' and valor >=100 ):
    total = ((0/100) * valor)
    print("Valor total com desconto:R$", total)
elif (forma == 'dinheiro' and valor <100 ):
    print("Pagamento abaixo de R$100,00 não recebem desconto. Valor da compra: R$", valor)
else:
    print("Forma de Pagamento Inválida")

input()