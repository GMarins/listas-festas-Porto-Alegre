from festas import *


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



for links in links_sin:
	sinners(links)

for links in links_marg:
	margot(links)
for links in links_beco:
	beco(links)

f_sin.close()
f_marg.close()
f_beco.close()
