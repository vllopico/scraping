import requests
from bs4 import BeautifulSoup
import time
import json

start = time.time()

cataleg_vins = list()
vins_x_pagina = 24
pagina = 0
num_pag = 229

while pagina <= num_pag:

	if pagina == 0:
		pg = "https://www.v....com/es/vinos/tinto/"
	else:
		pg = "https://www.v....com/es/vinos/tinto/?cursor="+str(pagina*vins_x_pagina)

	page = requests.get(pg)
	soup = BeautifulSoup(page.text,'html.parser')

	vins = soup.find_all("div", {"class": "product-list-item"})
	
	for v in vins:
		info_vi = v.find_all("div", {"class":"info"})
		info_preu = v.find_all("div", {"class":"quantity-widget small"})
		
		for iv in info_vi:
			nom_vi = iv.find_all("h2")
			regio = iv.find_all("div",{"class":"region"})
			
			info_celler = iv.find_all("div",{"class":"details"})
			for ic in info_celler:
				celler = ic.find_all("div")
		
		for ip in info_preu:
			preu = ip.find_all("p", {"class":"price"})
			
		botella = {"vi":nom_vi[0].text, "celler":celler[0].text, "regio":regio[0].text, "preu":preu[0].text}
		cataleg_vins.append(botella)
		
	pagina = pagina + 1
		
with open('vins_negres.json', 'w') as file:
    json.dump(cataleg_vins, file, indent=4, ensure_ascii=False)

end = time.time()
t = end - start
print ("Script time ->", str(t), "s")
