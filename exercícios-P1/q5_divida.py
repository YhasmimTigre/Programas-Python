"""
Esse programa calcula o valor de uma divida de acordo com o juros e prestações
"""

print("qual o valor inicial da divida?")
vi = input()
vi = float(vi)
print("qual o juros mensal?")
jm = input() 
jm = float(jm)
print("qual o valor mensal que será pago?")
vm = input() 
vm = float(vm)
valor_inicial = vi

meses = 0
total_juros = 0
while (vi >= vm) :
        juros = vi*(jm/100)
        vi = vi + (juros - vm)
        total_juros = total_juros + juros
        meses = meses + 1

total_pago = valor_inicial + total_juros 
print(f"total de meses:{meses}")
print(f"total de juros:{total_juros:.2f}")
print(f"total da divida:{total_pago:.2f}")

input() 
