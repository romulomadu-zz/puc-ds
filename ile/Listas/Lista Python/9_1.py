# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 9.1") 

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("words.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo words.txt...")
    
words = dict()
for line in fhand:
    line = line.rstrip()
    linewords = line.split()
    for word in linewords:
        if word in words: continue
        words[word] = 0
print(words) 

