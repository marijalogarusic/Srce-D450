suma = 0

vrijednost = input("Unesite broj: ")
vrijednost = int(vrijednost)

suma += vrijednost

while True:
   prethodni = vrijednost
   
   vrijednost = input("Unesite broj: ")
   vrijednost = int(vrijednost)

   if vrijednost <= prethodni:
      break

   suma += vrijednost
   prethodni = vrijednost

print("Suma unesenih brojeva: ", suma)