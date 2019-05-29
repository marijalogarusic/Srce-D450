gradovi = ['Bjelovar', 'Koprivnica', 'Osijek', 'Split', 'Zagreb']
gradovi.insert(0, gradovi[4])
print(gradovi)

while 'Zagreb' in gradovi:
    gradovi.remove('Zagreb')

print(gradovi)
