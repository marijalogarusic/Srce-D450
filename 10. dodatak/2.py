niz1 = input("Unesite niz znakova: ")
niz2 = input("Unesite niz znakova: ")

duljina1 = len(niz1)
duljina2 = len(niz2)

if duljina1 < duljina2:
    duljina = duljina1
else:
    duljina = duljina2

i = 0
while i < duljina:
    if niz1[i].lower() == niz2[i].lower():
        print(i, niz1[i].lower())
    i += 1
