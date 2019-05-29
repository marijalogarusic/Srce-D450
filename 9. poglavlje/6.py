def analiza(lista):
    for i in lista:
        if i%2 == 1:
            return False
    return True


lista = [2, 4, 6, 8, 9]

if analiza(lista) == True:
    print("Svi elementi su parni!")
else:
    print("Postoji barem jedan neparan broj!")
