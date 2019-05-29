lista = []

brojac = 0
while True:
    broj = input("Unesite broj: ")
    broj = int(broj)

    if broj == 5:
        break
    else:
        brojac += 1
        lista.append(broj)

if brojac < 6:
    while brojac < 6:
        lista.append(0)
        brojac += 1

i = 0
for element in lista:
    print("[", i, "] = ", element, sep='')
    i += 1
