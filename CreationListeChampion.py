import json

with open('data.json') as data_file:
    data = json.load(data_file)
    with open('listeChampion.txt', 'w') as f:
        string ="("
        for key in data:
            value = data[key]
            print( key, value)
            nom = key.split()[0]
            if nom not in string:
                string += f' \"{nom}\"'
        string +=")"
        f.write(string)




