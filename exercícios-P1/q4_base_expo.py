"""
Calculo de base e expoente
"""

base_num = int(input("digite a base: "))

expoente_num = int(input("digite o expoente: "))

resultado = base_num
for i in range (expoente_num-1):
    resultado = base_num*resultado
    
print('%d elevado a %d = %d' % (base_num, expoente_num, resultado))

