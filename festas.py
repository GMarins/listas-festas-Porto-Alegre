#Script para colocar o nome do pessoal em listas de festas
# -*- coding: utf-8 -*-
### PARTY LIST  v0.1a

import re
import mechanize
import bs4

def cucko(): #functional one name at the time, mult events, CHECK
	br = mechanize.Browser()
	retorno = br.open("http://www.cucko.com.br/nome_lista/nomeLista/336")
	raiz = 'http://www.cucko.com.br/nome_lista/nomeLista/'
	nomes = ['Gabriel Marins da Costa','Joao Vitor Correa', 'Thomas Vaitses Fontanari',
			'Joao Cesar Onofrio','Julia Dal Bosco','Franciele Velasques',
			'Gabriela Leguissamo','Ana Carolina dos Santos',
			'Carolina Ceolato','Tainah Piazetta','Rafael Coimbra Gus',
			'Rodrigo Sampaio','Pedro Morgan','Gabriel Griep']
	email = 'gmc.marins@gmail.com'

	
	for f in br.forms():
		print f
		
	festas = raw_input('Insira Id das festas:')
	
	lista_festas = festas.split(',')
	
	for f in lista_festas:
		endereco = raiz + f
		br.open(endereco)
		for nome in nomes:
			br.select_form(nr=0)
			br.form['email'] = email
			br.form['nome[]'] = nome
			br.submit()
			br.back()	
	
def sinners(s): #Fully Functional, mult names, one event per time CHECK
	br = mechanize.Browser()
	
	retorno = br.open(s)
	
	email = 'gmc.marins@gmail.com'
	nomes = ['Gabriel Marins da Costa','Julia Dal Bosco', 'Thomas Vaitses Fontanari',
			'Joao Vitor Correa Nogueira','Joao Cesar Onofrio']
	
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
	email = 'gmc.marins@gmail.com'
	nomes = ['Gabriel Marins da Costa','Julia Dal Bosco','Joao Vitor Correa Nogueira',
			'Tainah Piazetta','Carolina Ceolato']
	
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

	email = 'gmc.marins@gmail.com'
	nomes = ['Gabriel Marins da Costa','Joao Vitor Correa', 'Thomas Vaitses Fontanari',
			'Joao Cesar Onofrio','Julia Dal Bosco','Pedro Morgan',
			'Rodrigo Sampaio','Rafael Coimbra Gus',
			'Tainah Piazetta','Gabriela Leguissamo']
	
	
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
	
		
	
		
	

def anexo(): #not working
	br = mechanize.Browser()
	pass
	
