# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = "http://sinnersclub.com.br/agenda/"
r = requests.get(url)
f = open('links_sin.txt','w')

soup = BeautifulSoup(r.content,"lxml")

links = soup.find_all("a")

for link in links:
	print "<a href='%s'>%s</a>" %(link.get("href"),link.text)
	if isinstance(link.get("href"), str) == False:
		continue
	if 'agenda/' in link.get("href"):
		text = link.get("href")
		f.write(text + '\n')

f.close()



