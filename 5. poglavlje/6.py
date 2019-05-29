while True:
    bodovi = input("Unesite broj bodova: ")
    bodovi = float(bodovi)

    if bodovi >= 0 and bodovi < 50:
        print("Nedovoljan!")
    elif bodovi >= 50 and bodovi < 62.5:
        print("Dovoljan!")
    elif bodovi >= 62.5 and bodovi < 75:
        print("Dobar!")
    elif bodovi >= 75 and bodovi < 87.5:
        print("Vrlo dobar!")
    elif bodovi >= 87.5 and bodovi <= 100:
        print("Odličan!")
    else:
        print("Uneseni broj bodova je neispravan!")
        break
