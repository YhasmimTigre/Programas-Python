# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 18:46:57 2021

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
    total = ((90/100) * valor)
    print("Valor total com desconto:R$", total)
elif (forma == 'dinheiro' and valor <100 ):
    print("Pagamento abaixo de R$100,00 não recebem desconto. Valor da compra: R$", valor)
elif (forma == 'cartão'):
    print("Crédito ou Débito?")
    variante = input()
    if (variante == 'débito'):
        print("Valor total da sua compra é de R$:", valor)
    elif(variante == 'crédito'):
        print("Em quantas parcelas quer dividir a compra?")
        parcela = input()
        parcela = int(parcela)
        if (parcela <= 3):
            total_parcela = valor/parcela
            print("Valor total da sua compra" , valor)
            print(parcela , "parcelas de R$:", total_parcela)
        else: 
            print("Quantidade de parcelas inválido")
    else:
        print("Forma de Pagamento Inválida")
    
else:
    print("Forma de Pagamento Inválida")

input()