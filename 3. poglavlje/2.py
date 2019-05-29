a = 500
b = 5

if a > 100 and b < 100 or a < 100 and b > 100:
    print("Jedna je veća, a druga je manja od 100.")
elif a > 100 and b > 100:
    print("Obje vrijednosti su veće od 100.")
elif a < 100 and b < 100:
    print("Obje vrijednosti su manje od 100.")
else:
    print("Obje vrijednosti su jednake.")
