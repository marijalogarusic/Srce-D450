dani = ['ponedjeljak', 'utorak', 'srijeda', 'četvrtak', 'petak']

dani.append('subota')
dani.append('nedjelja')

print(dani)

#ispisuju se samo neradni dani, svaki u svom retku:
for element in dani[5:7]:
    print(element)
