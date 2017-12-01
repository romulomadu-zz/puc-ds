# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 3.3")
print("Score\tGrade\n>=\t0.9 A\n>=\t0.8 B\n>=\t0.7 C\n>=\t0.6 D\n<\t0.6 F\n")
try:
    nota = float(input("Digite uma pontuação: "))
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
    if nota>1.0:
        grade = float('forçar erro')
    if nota<0.0:
        grade = float('forçar erro')
    print("{}".format(grade))        
except:
    print("\nPontuação Ruim.")
        
