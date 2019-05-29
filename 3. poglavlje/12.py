n=5
x=1
y=1

for i in range(0,n): # Određuje redak
    for j in range(0,n): # Određuje stupac
        if i == y and j == x:
            print("X", end='')
        else:
            print("-", end='')
    print()
