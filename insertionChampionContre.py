import json

with open('data.json') as data_file:
    data = json.load(data_file)
    with open('insertionChampionContre.txt', 'w') as f:
        for key in data:
            value = data[key]
            #print( key, value)
            nom = key.split()[0]
            cps =0
            for i in value["counters"]:
                cps+=1
                if cps>1:
                    break
                string = f"""(ajouteRegle '(("{nom}Adversaire" T) ("{i}DispoLane" T)) (list "{i}Contre"  1)) \n"""
                string += f"""(ajouteRegle '(("{i}Adversaire" T) ("{nom}DispoLane" T)) (list "{nom}Contre"  -1))"""

                f.write(string)
                f.write('\n')





#  (ajouteRegle '(("ZedAdversaire" T) ("CamilleDispoLane" T)) (list "CamilleContre"  (+ 1 (nombre_contre "Camille"))))
#  (ajouteRegle '(("perd" T) ("gagne" T)) (list "CamilleContre"  (+ 1 (nombre_contre "Camille"))))





