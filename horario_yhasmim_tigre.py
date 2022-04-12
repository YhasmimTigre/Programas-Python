"""
Esse programa recebe uma informação e retorna uma resposta.
"""

print("qual o turno que você estuda? m = manhã, t = tarde, n = noite")
turno = input()
if (turno == 'm'):
    print("bom dia!")
elif (turno == 't'):
    print("boa tarde!")
elif (turno == 'n'):
    print("boa noite!")
elif (turno != 'm' or turno != 't' or turno != 'n'):
    print("Valor inválido!")

input()
