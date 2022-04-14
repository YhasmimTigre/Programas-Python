# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 17:30:30 2021

@author: Yhasmim
"""

print("qual o turno que você estuda?")
turno = input()
if (turno == 'm'):
    print("bom dia!")
elif (turno == 'v'):
    print("boa tarde!")
elif (turno == 'n'):
    print("boa noite!")
elif (turno != 'm' or turno != 'v' or turno != 'n'):
    print("Valor inválido!")

input()