# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 8.4") 

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("romeo.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo romeo.txt...")
    
words = []
for line in fhand:
    linewords = line.rstrip().split()
    for word in linewords:
        if word in words: continue
        words.append(word)
words.sort()
print(words)

