"""
Esse programa descobre se o seu triangulo é equilátero, isósceles ou escaleno.
"""

print("entre com o primeiro lado do triangulo")
lado_a = input()
lado_a = float(lado_a)
print("entre com o segundo lado do triangulo")
lado_b = input()
lado_b = float(lado_b)
print("entre com o terceiro lado do triangulo")
lado_c = input()
lado_c = float(lado_c)
if (lado_a == lado_b == lado_c ):
    print("Seu triângulo é equilátero")
elif (lado_a == lado_b or lado_b == lado_c or lado_c == lado_a):
    print("Seu triângulo é isósceles")
elif (lado_a != lado_b or lado_b != lado_c or lado_c != lado_a):
    print("Seu triângulo é escaleno")
    
    
input()
