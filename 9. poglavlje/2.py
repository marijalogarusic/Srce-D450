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

print(lista)
