# -*- coding: utf-8 -*-
"""
Created on Tue May  9 22:42:49 2017

@author: romul
"""
name_file = "trash.txt"
f = open(name_file,'w')
fhand = open("lista.py",encoding = "utf-8")
count = 0
for line in fhand:
    if line.startswith("print(\"Exe"):
        f.close()        
        numbers = line.split()[1].split("\"")[0].split(".")
        name_file = "{}_{}.py".format(numbers[0],numbers[1])
        f = open(name_file,'w',encoding='utf-8')
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("\"\"\"\n")
        f.write("Created on Tue May  9 22:42:49 2017\n")
        f.write("\n")
        f.write("@author: Rômulo Rodrigues\n")
        f.write("\"\"\"\n")
        f.write("\n")
        f.write(line)
    else:
        f.write(line)
f.close()