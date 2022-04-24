x = 70.000
y = 180.000
NUM_ANOS = 0
while (x < y):
    x = x + x*3.5/100
    y = y + y*1.5/100
    NUM_ANOS = NUM_ANOS + 1
print("número de anos:", NUM_ANOS)

input()
