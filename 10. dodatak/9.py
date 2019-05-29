niz = input("Unesite niz znakova: ")

privremenNiz = ""

for e in niz:
   if e>='a' and e<='z' or e>='A' and e<='Z':
      privremenNiz += e.lower()

duljina = len(privremenNiz)

i=0
palindrom = True

while i < int(duljina/2):
   if privremenNiz[i] != privremenNiz[duljina-i-1]:
      palindrom = False
      break
   i += 1

if palindrom == True:
   print("Uneseni niz znakova je palindrom!")
else:
   print("Uneseni niz znakova nije palindrom!")
