from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json

def get_counter(url):
    print(f'on fait les counters de {url}')
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    soup = BeautifulSoup(page)
    liste = soup.find_all("div", {'class': "_yq1p7n _cu8r22"})
    liste = liste[1].find_all("div",{'class': "_ate82z"})
    liste_counter =[]
    for champions in liste:
         for x in champions:
             nom = x['href'][43:].split('/')[0]
             liste_counter.append(nom)
    return liste_counter



get_counter("https://www.metasrc.com/5v5/11.23/champion/camille/top")

url = "https://www.metasrc.com/5v5/11.23/tierlist"
#on utilise un user agent pour contourner bloquage
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup=BeautifulSoup(page)
liste = soup.find_all("div",{'class': "_ate82z"})

tiers =['S+','S','A','B','C','D']
cpt=0
resultat={}
for tier in liste:
     champion_tier =tiers[cpt]
     champions = tier.find_all({'a':"href"})
     for champion in champions:
          link =champion['href']
          nom=link[43:].split('/')[0]
          lane = link[43:].split('/')[1]
          data= {}
          data['tier']=champion_tier
          data['url']=link
          data['counters']=get_counter(link)
          resultat [f"{nom} {lane}"] = data
     cpt+=1
with open("data.json", "w") as outfile:
    json.dump(resultat, outfile)
