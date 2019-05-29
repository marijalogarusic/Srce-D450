from math import pow

lista = []
for x in range(41):
    for y in range(41):
        for z in range(41):
            if (pow(x, 2) + pow(y, 2)) == z:
                tmp = [x, y, z]
                lista.append(tmp)

for i in lista:
    print(i)
