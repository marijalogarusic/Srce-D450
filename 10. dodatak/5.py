def izracun():
    suma = 0
    tmp = x

    if tmp < 0:
        tmp *= -1

    while tmp > 0:
        suma += tmp
        tmp -= 1

    if x < 0:
        suma *= -1

    return suma


x = input("Unesite cijeli broj: ")
x = int(x)

suma = izracun()
print(suma)
