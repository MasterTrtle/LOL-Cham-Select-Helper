from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json

url = "https://www.metasrc.com/5v5/tierlist"
#on utilise un user agent pour contourner bloquage
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup=BeautifulSoup(page)
liste = soup.find_all("div",{'class': "_ate82z"})

tiers =['S+','S','A','B','C','D']
cpt =0

for tier in liste:
     champion_tier =tiers[cpt]
     champions = tier.find_all({'a':"href"})
     for champion in champions:
          link =champion['href']
          data = {}
          data['tier']=champion_tier
          data['href']=link
          data['nom']=link[37:].split('/')[0]
          data['lane'] = link[37:].split('/')[1]
          print(json.dumps(data))
     cpt+=1


