rjecnik = {"stol" : "desk", "sat" : "clock", "penkala" : "pencil", "remen" : "belt", "svjetlo" : "light"}

while 1==1:
    rijec = input("Unesite rijec na hrvatskome: ")
    rijec = rijec.lower()
    if rijec == "x":
        break
    if rijec in rjecnik:
        print(rjecnik[rijec])
    else:
        print("Unesene rijeci nema u rjecniku!")
