# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 7.2")

from numpy import mean

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
buffer = []    
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        buffer.append(float(line[line.find(":")+1:]))
print(mean(buffer))
    
    
