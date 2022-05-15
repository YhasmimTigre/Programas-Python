"""
Emulando um teste da Capricho, o programa descobre a faixa etária de uma turma
a partir das idades recebidas
"""

print("Teste da Capricho! sua turma é jovem, adulta ou idosa?")
print("vamos calcular a média de idade da sua turma!")

print("Quantas pessoas existem na sua turma?")
n = int(input())

print("Quais as idades das pessoas da sua turma?")

total = 0
for i in range (n):
      idades = int(input())
      total = idades + total

media = total / n

if (media <= 25):
    print("resultado: 0 a 25 anos: sua turma é jovem!")
    
elif (media >=26 and media < 60):
    print("resultado: 26 a 60 anos: sua turma é adulta!")
    
elif (media > 60):
    print("resultado: maior que 60 anos: sua turma é idosa!")
