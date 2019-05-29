dani = ['ponedjeljak', 'utorak', 'srijeda', 'četvrtak', 'petak', 'subota', 'nedjelja']
radniDani = ['ponedjeljak', 'utorak', 'srijeda', 'četvrtak', 'petak']
vikend = []

for element in dani:
    if element not in radniDani:
        vikend.append(element)
print(vikend)
