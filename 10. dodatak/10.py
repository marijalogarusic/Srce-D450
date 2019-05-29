import math

a = int(input("Unesite vrijednost a1: "))
b = int(input("Unesite vrijednost b1: "))
n = int(input("Unesite vrijednost n: "))

print("A(1)=", round(a, 2), sep="", end=", ")
print("B(1)=", round(b, 2))

i = 2

while i <= n:
   aTmp = a
   bTmp = b

   a = (aTmp + bTmp) / 2
   b = math.sqrt(aTmp + bTmp)

   print("A(", i, ")=", round(a, 2),sep="",end=", ")
   print("B(", i, ")=", round(b, 2),sep="")

   i += 1
