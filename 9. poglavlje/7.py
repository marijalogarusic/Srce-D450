lista = []

while True:
    broj = input("Unesite broj: ")
    broj = int(broj)

    if broj == 5:
        break
    else:
        lista.append(broj)

print(lista)
lista.reverse()
print(lista)
