n = 7

for i in range(0,n): # Određuje redak
    for j in range(0,n): # Određuje stupac
        if i == j:
            print("1", end='')
        else:
            print("0", end='')
    print()
