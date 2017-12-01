# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 6.5")

s = 'X-DSPAM-Confidence: 0.8475'
index = s.find(':')+1
num = float(s[index:])              
print("Num: {} Tipo: {}".format(num,type(num)))
              
