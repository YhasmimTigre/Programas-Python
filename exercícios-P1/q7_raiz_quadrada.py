"""
Nesse programa, realizamos o calculo de uma raiz quadrada,
resultando no seu valor aproximado
"""

print("qual a raiz quadrada a ser calculada?")
n = input()
n = float(n)
b = 2
p = (b + (n/b))/2
while ((abs (b - p)) > 0.0001):
     b = p
     p = (b + (n/b))/2
     
print("o valor aproximado da raiz quadrada é:", b)

input()
