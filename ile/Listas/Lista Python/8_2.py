# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 8.2")   

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
count = 0
for line in fhand:
    palavras = line.split()
    # print ‘Debug:’, palavras
    if len(palavras) <= 1 : continue
    if not line.startswith('From ') : continue    
    print(palavras[2])

