def zbroj(a, b):
   return a+b

def razlika(a, b):
   return a-b

def umnozak(a, b):
   return a*b

def kolicnik(a, b):
   # Provjera nedozvoljenog dijeljenja
   if b == 0:
      return "Dijeljenje s nulom!"
   return a/b

info = ("Odaberite računsku operaciju:\n" +
         "1 – zbrajanje\n" +
         "2 – oduzimanje\n" +
         "3 – množenje\n" +
         "4 – dijeljenje\n" +
         "0 – izlaz iz programa")

while True:
   print(info)

   tip = input("Unesite broj željene operacije: ")
   tip = int(tip)

   if tip < 0 or tip > 4:
      print("Nepoznata operacija!\n")
      continue
   if tip == 0:
      print("Izlaz iz programa")
      break
      
   a = int(input("Unesite prvu vrijednost: "))
   b = int(input("Unesite drugu vrijednost: "))

   if tip == 1:
      rezultat = zbroj(a, b)
   elif tip == 2:
      rezultat = razlika(a, b)
   elif tip == 3:
      rezultat = umnozak(a, b)
   elif tip == 4:
      rezultat = kolicnik(a, b)

   print("Rezultat je:", rezultat, "\n")
