niz = "Ovo Je Neki Niz Anakova"

brojac = 0
pronadenoA = 0

for x in niz:
    if x >= "A" and x <= 'Z':
        brojac += 1

    if x == "A":
        pronadenoA = 1
        print("Veliko slovo A je pronađeno.")

if pronadenoA == 0:
    print(brojac)
