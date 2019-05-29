while True:
   n = int(input("Unesite vrijednost: "))
   
   if n >= 3 and n <= 20:
      break
   else:
      print("Neispravna vrijednost!")

i = 0
lista = []
postavljeno = 0
najveci = 0

while i < n:
   print(i+1, ". par!", sep="")
   
   x = int(input("Unesite x: "))
   y = int(input("Unesite y: "))

   lista.append([x, y])

   if postavljeno == 0 or najveci < x+y:
      najveci = x+y
      postavljeno = 1
      
   i += 1
   
for e in lista:
   if e[0]+e[1] == najveci:
      print(e)