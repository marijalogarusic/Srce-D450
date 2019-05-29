while True:
    n = input("Unesite n: ")
    n = int(n)

    if n >= 3 and n <= 10:
        break

brojac = 1
for i in range(0, n): # Određuje redak
    for j in range(0, i): # Određuje prazan stupac
        print("   ", end="")
    for j in range(0, n-i): # Ispisuje broj
        if brojac >= 0 and brojac <= 9:
            print("  ", end="")
            print(brojac, end="")
        else:
            print(" ", end="")
            print(brojac, end="")
        brojac += 1
    print()
