# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://www.cucko.com.br/agenda/"
r = requests.get(url)
f = open("links_cuck.txt","w")

soup = BeautifulSoup(r.content,"lxml")
links = soup.find_all("a")

for link in links:
	#print "<a href='%s'>%s</a>" %(link.get("href"),link.text)
	if isinstance(link.get("href"), str) == False:
		continue
	if 'evento' in link.get("href"):
		text = link.get("href")[-3:]
		f.write("http://www.cucko.com.br/nome_lista/nomeLista/" + text + '\n')
	
	
f.close()
