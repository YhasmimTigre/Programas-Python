# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 10:03:19 2021

@author: Yhasmim
"""
#usuário digita uma string
data = str(input("digite uma data dd/mm/aaaa: "))
#separamos os meses em um dicionario
mes_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março',
           4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho',
           8: 'agosto', 9: 'setembro', 10: 'outubro',
           11: 'novembro', 12: 'dezembro'}
#encontramos o numero do mês correspondente e exibimos ao usuário
dia, mes, ano = data.split("/")
print ("Data por extenso: %s de %s de %s" % (dia, mes_ext[int(mes)], ano))