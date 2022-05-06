# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:37:28 2021

@author: Yhasmim
"""


resposta = 0
while( resposta != 'n'):
    print("digite o numero que desejar saber a tabuada:")
    num_int = int(input())
    
    for numero in range (10):
        print ('%d * %d = %d' % (num_int, numero+1, num_int*(numero+1)) )
    print("desejar saber a tabuada de outro numero? s/n")
    resposta = input()
  
