import json

with open('data.json') as data_file:
    data = json.load(data_file)
    with open('insertionChampionDispo.txt', 'w') as f:
        for key in data:
            value = data[key]
            print( key, value)
            nom = key.split()[0]
            lane = key.split()[1]
            string = f"""(ajouteRegle '(("{nom}Dispo" T) ("{lane}" T)) '("{nom}DispoLane"  T))"""
            f.write(string)
            f.write('\n')

#(ajouteRegle '(("CamilleDispo" T) ("Top" T)) '("CamilleDispoLane"  T))



