# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 10.3")

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("words.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo words.txt...")
    
text = fhand.read()

lst = [x for x in text.lower() if x.isalpha()]
letters = dict()
for letter in lst:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1
               
lst = []
for key,value in letters.items():
    lst.append((value,key))
lst.sort(reverse=True)

letters = dict()
for value,key in lst:
    letters[key]=value

print(letters)

              