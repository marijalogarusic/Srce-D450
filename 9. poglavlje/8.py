povrce = {
     'krumpir' : ['bijeli', 'crveni', 'za salatu'],
     'luk' : ['bijeli', 'crveni']
}

for vrsta in povrce.keys():
    print(vrsta.title(), ":", len(povrce[vrsta]))
