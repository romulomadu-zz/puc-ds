# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 9.2")

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...") 

days = {'Sun':0,"Mon":0,"Tue":0,"Wed":0,"Thu":0,"Fri":0,"Sat":0}

count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue   
    days[line.split()[2]] += 1
print(days)

