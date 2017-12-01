# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 9.5")
    
try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
domain = dict()
for line in fhand:
   line = line.rstrip()
   if not line.startswith("From "): continue
   index = line.split()[1].find("@")+1
   if line.split()[1][index:] in domain:       
       domain[line.split()[1][index:]] += 1
   else:
       domain[line.split()[1][index:]] = 1

print(domain)
            
