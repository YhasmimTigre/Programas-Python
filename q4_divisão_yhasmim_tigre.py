#Esse programa efetua divisões

print("digite o numerador número:")
x = input()
x = float(x)
print("digite o denominador número:")
y = input()
y = float (y)
divisao = 0
while (x >= y):
    divisao = divisao + 1
    x = x - y
    if (x <= y):
        n = x 
        n = y - n
print("divisão:", divisao )
print("resto de divisão:", x)

input()
