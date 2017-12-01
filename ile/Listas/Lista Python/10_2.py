# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 10.2")

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
hours = dict()
for line in fhand:
    line =  line.rstrip()
    if not line.startswith("From "): continue
    index = line.split()[5].find(":")
    if line.split()[5][0:index] in hours:       
        hours[line.split()[5][0:index]] += 1
    else:
        hours[line.split()[5][0:index]] = 1

lst = list()
for key, val in hours.items():
    lst.append( (key, val) )
lst.sort()
for hour,count in lst:
    print(hour,count)    
 
