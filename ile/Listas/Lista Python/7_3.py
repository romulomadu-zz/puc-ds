# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: Rômulo Rodrigues
"""

print("Exercício 7.3")

from numpy import mean

try:
    filename = input("Enter the name of file: ")
    fhand = open(filename)    
    print("reading file {}...".format(filename))
except:    
    if filename == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk’d!")
    else:
        fhand = open("mbox-short.txt")
        print("file not found...")    
        print("reading file mbox-short.txt...")    

if filename != "na na boo boo":
    buffer = []    
    for line in fhand:
        line = line.rstrip()
        if line.startswith("X-DSPAM-Confidence:"):
            buffer.append(float(line[line.find(":")+1:]))
    print(mean(buffer))

