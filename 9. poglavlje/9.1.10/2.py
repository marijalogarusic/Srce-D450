dani = ['ponedjeljak', 'utorak', 'srijeda', 'četvrtak', 'petak', 'subota', 'nedjelja']

radniDani = dani.copy()
radniDani.pop()
radniDani.remove('subota')

print(radniDani)
