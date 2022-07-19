# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:38:12 2021

@author: Yhasmim
"""
#definimos uma string digitada pelo usuário
string = str(input("Digite uma frase"))

#primeira forma de resolver com uma nova string
nova_string = str()

#percorremos a string, tiramos os espaços e concatenamos para uma nova string
for i in range (0, len(string)):
    if string[i] == ' ':
        continue
    else:
        nova_string = nova_string + string[i]
                        
print(nova_string)

#segunda forma (mais rápida) de resolver, com uma função
"""
#utilizamos o .raplace para retirar os espaços em branco
print (string.replace(" ",""))
"""