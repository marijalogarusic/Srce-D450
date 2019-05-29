brojac = 0
a = 2
b = 10

for n in range(a, b+1):
    jePrim = True
    for x in range(2, n):
        if n % x == 0:
            jePrim = False
            break
    if jePrim == True:
        brojac += 1

print(brojac)
