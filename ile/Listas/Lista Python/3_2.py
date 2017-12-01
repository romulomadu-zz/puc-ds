# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 3.2")
try:
    horas = float(input("Horas: "))
    valorhora = float(input("Valor/Hora: "))
    if horas>40:
        salariobruto = 40*valorhora + (horas%40)*1.5*valorhora
    else:
        salariobruto = horas*valorhora       
    print("\nSalário Bruto: {}".format(salariobruto))    
except:
    print("\nErro! Por favor, digite uma entrada numérica.")

