# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:55:11 2017

@author: Rômulo Madureira Rodrigues
"""
print("Exercício 2.1")
5
x = 5
x + 1

print("Exercício 2.2")
name = input("Digite seu nome: ")
print("Olá {}".format(name))

print("Exercício 2.3")
horas = float(input("Horas: "))
valorhora = float(input("Valor/Hora: "))
salariobruto = horas*valorhora
print("\nSalário Bruto: {}".format(salariobruto))

print("Exercício 2.4")  
largura = 17
altura = 12.0
print("1) largura/2: {}".format(type(largura/2)))
print("2) largura/2.0: {}".format(type(largura/2.0)))
print("3) altura/3: {}".format(type(altura/3)))
print("4) 1 + 2*5: {}".format(type(1 + 2*5)))

print("Exercício 2.5")  
temp = float(input("Entre com a temperatura em °C: "))
print("Temperatura convertida para Fahrenheit: {}°F".format(temp*9/5 + 32))

print("Exercício 3.1")
horas = float(input("Horas: "))
valorhora = float(input("Valor/Hora: "))
if horas>40:
    salariobruto = 40*valorhora + (horas%40)*1.5*valorhora
else:
    salariobruto = horas*valorhora       
print("\nSalário Bruto: {}".format(salariobruto))

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
        
print("Exercício 4.1")
import random
for i in range (10):
    x = random.random()
    print('Execução {}: {}'.format(i+1,x))

print("Exercício 4.2")
repeat_lyrics()
def print_lyrics():
    print("I’m a lumberjack, and I’m okay.")
    print ("I sleep all night and I work all day.")
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
print("Exercício 4.3")
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
def print_lyrics():
    print("I’m a lumberjack, and I’m okay.")
    print ("I sleep all night and I work all day.")
repeat_lyrics()    

print("Exercício 4.4")   
print("Resposta: d) b e c são ambas verdadeiras") 
    
print("Exercício 4.5")   
print("Resposta: d) ABC Zap ABC")
    
print("Exercício 4.6")       
def computepagamento(horas,valorhora):
    if horas>40:
        salariobruto = 40*valorhora + (horas%40)*1.5*valorhora
    else:
        salariobruto = horas*valorhora       
    print("\nSalário Bruto: {}".format(salariobruto))   

try:
    horas = float(input("Horas: "))
    valorhora = float(input("Valor/Hora: "))
except:
    print("\nErro! Por favor, digite uma entrada numérica.")

computepagamento(horas,valorhora)

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

print("Exercício 6.1")

s = input("Entre com a string: ")
l = len(s)
while l>0:
    l-=1
    print(s[l])
  
print("Exercício 6.2")

print("'fruta'[:] resulta em 'fruta'")

print("Exercício 6.4")

print("banana".count('a'))

print("Exercício 6.5")

s = 'X-DSPAM-Confidence: 0.8475'
index = s.find(':')+1
num = float(s[index:])              
print("Num: {} Tipo: {}".format(num,type(num)))
              
print("Exercício 7.1")

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")


for line in fhand:
    line = line.rstrip()
    print(line.upper())

print("Exercício 7.2")

from numpy import mean

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
buffer = []    
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        buffer.append(float(line[line.find(":")+1:]))
print(mean(buffer))
    
    
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

print("Exercício 8.1")    

def chop(lst):
    lst = lst[1:-1]
    return None

def middle(lst):
    lst = lst[1:-1]
    return lst

print("Exercício 8.2")   

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
count = 0
for line in fhand:
    palavras = line.split()
    # print ‘Debug:’, palavras
    if len(palavras) <= 1 : continue
    if not line.startswith('From ') : continue    
    print(palavras[2])

print("Exercício 8.3") 

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
count = 0
for line in fhand:
    palavras = line.split()
    # print ‘Debug:’, palavras
    if len(palavras) <=1 or  not line.startswith('From ') : continue   
    print(palavras[2])
    
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

print("Exercício 8.5") 

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")

for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue
    print(line.split()[1])
    
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

print("Exercício 9.2")

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...") 

days = {'Sun':0,"Mon":0,"Tue":0,"Wed":0,"Thu":0,"Fri":0,"Sat":0}

count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "): continue   
    days[line.split()[2]] += 1
print(days)

print("Exercício 9.3")  

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
emails = dict()
for line in fhand:
   line = line.rstrip()
   if not line.startswith("From "): continue
   if line.split()[1] in emails:
       emails[line.split()[1]] += 1
   else:
       emails[line.split()[1]] = 1
print(emails) 

print("Exercício 9.4") 

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
emails = dict()
for line in fhand:
   line = line.rstrip()
   if not line.startswith("From "): continue
   if line.split()[1] in emails:
       emails[line.split()[1]] += 1
   else:
       emails[line.split()[1]] = 1
maxvalor = 0      
for key,value in emails.items():
    if emails[key] < maxvalor: continue
    maxvalor = value
    keymax = key
print(keymax)

print("Exercício 9.5")
    
try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
domain = dict()
for line in fhand:
   line = line.rstrip()
   if not line.startswith("From "): continue
   index = line.split()[1].find("@")+1
   if line.split()[1][index:] in domain:       
       domain[line.split()[1][index:]] += 1
   else:
       domain[line.split()[1][index:]] = 1

print(domain)
            
print("Exercício 10.1")

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
emails = dict()
for line in fhand:
   line = line.rstrip()
   if not line.startswith("From "): continue
   if line.split()[1] in emails:
       emails[line.split()[1]] += 1
   else:
       emails[line.split()[1]] = 1

lst = list()
for key, val in emails.items():
    lst.append( (val, key) )
lst.sort(reverse=True)
print(lst[0][1])

print("Exercício 10.2")

try:
    filename = input("Digite o nome do arquivo: ")
    fhand = open(filename)
    print("lendo arquivo {}...".format(filename))
except:
    fhand = open("mbox-short.txt")
    print("arquivo não encontrado...")    
    print("lendo arquivo mbox-short.txt...")
    
hours = dict()
for line in fhand:
    line =  line.rstrip()
    if not line.startswith("From "): continue
    index = line.split()[5].find(":")
    if line.split()[5][0:index] in hours:       
        hours[line.split()[5][0:index]] += 1
    else:
        hours[line.split()[5][0:index]] = 1

lst = list()
for key, val in hours.items():
    lst.append( (key, val) )
lst.sort()
for hour,count in lst:
    print(hour,count)    
 
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

              