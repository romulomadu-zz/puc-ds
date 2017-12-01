# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 5.1")

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
        
print(sum(buffer),len(buffer),np.mean(buffer))               
            
