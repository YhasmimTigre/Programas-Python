#O usuário digita sua primeiro e segunda nota e recebe uma classficação de acordo com ela.

print("Digite sua primeira nota")
prim_nota = input()
prim_nota = float(prim_nota)
print("Digite sua segunda nota nota")
seg_nota = input()
seg_nota = float(seg_nota)
media=(prim_nota + seg_nota)/2
if (media >= 9.0 and media < 10.0):
    print("conceito A")
elif(media >= 7.5 and media < 9.0):
    print("Conceito B")
elif(media >= 6.0 and media < 7.5):
    print("Conceito C")
elif (media >= 4.0 and media < 6.0):
    print("Conceito D")
elif (media >= 0 and media < 4.0):
    print("Conceito E")

input()
