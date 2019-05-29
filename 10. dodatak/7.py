niz = input("Unesite niz znakova: ")

izlazniNiz = ""

veliko = True

for e in niz:
   if e >= 'A' and e <= 'Z' and veliko == True:
      izlazniNiz += e
      veliko = False
   elif e >= 'a' and e <= 'z' and veliko == False:
      izlazniNiz += e
      veliko = True

print(izlazniNiz)
