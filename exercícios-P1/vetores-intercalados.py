#definimos as listas

vetor_x = []
vetor_y = []

#criamos o input para o usuário

for i in range(0,5):
    vetor_x.append(int(input("digite os valores para o vetor 1: ")))

for i in range(0,5):
    vetor_y.append(int(input("digite os valores para o vetor 2: ")))

#importamos chain de intertools para fazer as listas interagirem

from itertools import chain

resultado = chain.from_iterable(zip(vetor_x, vetor_y))

print("União intercalada dos vetores 1 e 2:", *resultado)
