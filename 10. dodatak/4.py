def sumaZnamenki(x):
   suma = 0

   while x > 0:
      suma += x%10
      x /= 10
      x = int(x)

   return suma

najmanji = 0
najmanjaSuma = -1
while True:
   x = input("Unesite broj: ")
   x = int(x)

   if x <= 0:
      break

   s = sumaZnamenki(x)

   if najmanjaSuma == -1 or najmanjaSuma > s:
      najmanjaSuma = s
      najmanji = x

print("Broj: ", najmanji)
print("Najmanja suma znamenki: ", int(najmanjaSuma))
