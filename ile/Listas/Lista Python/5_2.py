# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 5.2")
    
import numpy as np
buffer = []
while(True):
    number = input("Digite um número: ")
    try:
        if number == "done" or  number == "Done":
            break;
        else:
            number = float(number)
            buffer.append(number)
    except:
        print("Invalid Input")
if len(buffer)<2:
    print("Lista contém menos que dois números.")
else:       
    print(min(buffer),max(buffer))        

