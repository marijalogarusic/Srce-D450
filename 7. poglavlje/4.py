ulaz = open("datoteka.txt", "r")
izlazParni = open("parni.txt", "w")
izlazZbroj = open("zbroj.txt", "w")

sumaBrojeva = 0
for line in ulaz.readlines():
    line = int(line)
    if line%2 == 0:
        izlazParni.write(str(line) + "\n")
    else:
        sumaBrojeva += line
        
izlazZbroj.write("Suma neparnih brojeva je: " + str(sumaBrojeva))

ulaz.close()
izlazParni.close()
izlazZbroj.close()
