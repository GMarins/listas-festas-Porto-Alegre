from festas import *
from beco_scrapper import *
from cuck_scrapper import *
from marg_scrapper import *
from sin_scrapper import *
import time

start = time.time()

with open("links_sin.txt","r") as f_sin:
	links_sin = []
	for line in f_sin:
		links_sin.append(line.rstrip())

with open("links_marg.txt","r") as f_marg:
	links_marg = []
	for line in f_marg:
		links_marg.append(line.rstrip())
		
with open("links_beco.txt","r") as f_beco:
	links_beco = []
	for line in f_beco:
		links_beco.append(line.rstrip())
		
with open("links_cuck.txt","r") as f_cuck:
	links_cuck = []
	for line in f_cuck:
		links_cuck.append(line.rstrip())



for links in links_sin:
	sinners(links)
for links in links_marg:
	margot(links)
for links in links_beco:
	beco(links)
for links in links_cuck:
	cucko(links)

f_sin.close()
f_marg.close()
f_beco.close()
f_cuck.close()

elapsed = (time.time() - start)
print("\n\nThis code took: " + str(elapsed) + " seconds")
