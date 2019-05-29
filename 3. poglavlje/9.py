niz = "ABCDEFGHIJK"
duljina = len(niz)
n = 2

if duljina > n:
    indeks = 0
    for x in niz:
        if indeks%n == 0:
            print(x, end="")
        indeks += 1      
else:
    print("Greska!")
