with open("datoteka.txt", "w") as f:
    for i in range(0, 20):
        if i%2 == 0:
            f.write(str(i) + " ")
