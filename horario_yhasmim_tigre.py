#Esse programa recebe uma informação do usuário e retorna uma saudação 
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
