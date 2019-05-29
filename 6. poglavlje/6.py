import math

broj = input("Unesite broj: ")
broj = float(broj)

f = math.floor(broj)
c = math.ceil(broj)

print(f, c, sep=", ")
