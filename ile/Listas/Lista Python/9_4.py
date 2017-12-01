# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 9.4") 

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
emails = dict()
for line in fhand:
   line = line.rstrip()
   if not line.startswith("From "): continue
   if line.split()[1] in emails:
       emails[line.split()[1]] += 1
   else:
       emails[line.split()[1]] = 1
maxvalor = 0      
for key,value in emails.items():
    if emails[key] < maxvalor: continue
    maxvalor = value
    keymax = key
print(keymax)

