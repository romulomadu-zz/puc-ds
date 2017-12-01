# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 4.7")     

def computagrau(nota):
    if nota>=0.6:
        grade = 'D'   
    if nota>=0.7:
        grade = 'C' 
    if nota>=0.8:
        grade = 'B'
    if nota>=0.9:
        grade = 'A'      
    if nota<0.6:
        grade = 'E'
    return grade
try:
    nota = float(input("Digite uma pontuação: ")) 
    if nota>1.0:
        grade = float('forçar erro')
    if nota<0.0:
        grade = float('forçar erro')
    grade = computagrau(nota)  
    print("{}".format(grade))
except:
    print("\nPontuação Ruim.")

