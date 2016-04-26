# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

f = open("links_beco.txt","w")

url = 'http://www.beco203.com.br/agenda/'
r = requests.get(url)


soup = BeautifulSoup(r.content,"lxml")
links = soup.find_all("a") #
agendas = []
links_form = []

for link in links: #add the events url to agendas
	if 'agenda/' in link.get("href") and 'ingresso' not in link.get("href") and 'aniver' not in link.get("href"):
		agendas.append('http://www.beco203.com.br/' + link.get("href").lstrip('../'))

for i in agendas: #loop through every event to get to the pre-form page
	url = i
	r = requests.get(url)
	soup = BeautifulSoup(r.content,"lxml")
	links = soup.find_all("a") ####

	for link in links: #loop to get the pages that redirect to the form selection page
		if 'selecaoLista' in link.get("href"): #append the pre-form pages to links_form
			links_form.append('http://www.beco203.com.br/' + link.get("href").lstrip("../"))
		
		if isinstance(link.get("href"), str) == False:
			continue
		
for i in links_form: #loop through the pre-forms to get the form page that will be written
	url = i
	r = requests.get(url)
	soup = BeautifulSoup(r.content,'lxml')
	links = soup.find_all("a")
	for link in links:
		if 'nomeLista' in link.get("href"):
			f.write("http://www.beco203.com.br/resources/files/" + link.get("href") + '\n')
		
f.close()
