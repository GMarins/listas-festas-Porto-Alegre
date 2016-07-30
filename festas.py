#Script para colocar o nome do pessoal em listas de festas
# -*- coding: utf-8 -*-
### PARTY LIST  v0.1a


#Esse arquivo contém as funções utilizadas
#As listas com os nomes são separadas devido às restrições de limite no número de nomes inscritos de cada casa

import re
import mechanize
import bs4

def cucko(s): 
	br = mechanize.Browser()
	nomes = ['Name1','Name2'] #Insert the names, unlimited amount
	email = '' #Insert your email

	for nome in nomes:
		retorno = br.open(s)
		br.select_form(nr=0)
		br.form['email'] = email
		br.form['nome[]'] = nome
		br.submit()


def sinners(s): #Fully Functional, mult names, one event per time CHECK
	br = mechanize.Browser()

	retorno = br.open(s)

	nomes = ['Name1','Name2'] #Insert the names, max 5
	email = '' #Insert your email

	for f in br.forms():
		print f

	br.select_form(nr=0)
	br.form['email'] = email
	i = 0
	for control in br.form.controls:
		if control.name == 'name[]':
			control.value = nomes[i]
			i += 1
	print br.form
	br.submit()


def margot(s): #Seems working
	"""61"""
	br = mechanize.Browser()
	nomes = ['Name1','Name2'] #Insert the names, max 5
	email = '' #Insert your email

	retorno = br.open(s)

	br.select_form(nr=0)
	print br.form
	br.form['email'] = email
	br.form['nome1'] = nomes[0]
	br.form['nome2'] = nomes[1]
	br.form['nome3'] = nomes[2]
	br.form['nome4'] = nomes[3]
	br.form['nome5'] = nomes[4]
	print br.form
	br.submit()



def beco(s):

	br = mechanize.Browser()

	nomes = ['Name1','Name2'] #Insert the names, max 10
	email = '' #Insert your email


	br.open(s)
	br.select_form(nr=0)
	print br.form
	br.form['email'] = email
	br.form['nome'] = nomes[0]
	br.form['nomeAmigo1'] = nomes[1]
	br.form['nomeAmigo2'] = nomes[2]
	br.form['nomeAmigo3'] = nomes[3]
	br.form['nomeAmigo4'] = nomes[4]
	br.form['nomeAmigo5'] = nomes[5]
	br.form['nomeAmigo6'] = nomes[6]
	br.form['nomeAmigo7'] = nomes[7]
	br.form['nomeAmigo8'] = nomes[8]
	br.form['nomeAmigo9'] = nomes[9]
	print br.form
	br.submit()






def esko(): 
	br = mechanize.Browser()
	pass

def obra():
	br = mechanize.Browser()
	pass
