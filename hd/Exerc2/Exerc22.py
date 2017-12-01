import mincemeat
import glob
import csv

text_files = glob.glob("C:\\Temp\\Exerc\\Join\\*")

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name)) for file_name in text_files)

def mapfn(k,v):
    print 'map ' + k
    for line in v.splitlines():
        if k == "C:\\Temp\\Exerc\\Join\\2.2-vendas.csv":
            yield line.split(';')[0], 'Vendas' + ':' + line.split(';')[5]
        if k == "C:\\Temp\\Exerc\\Join\\2.2-filiais.csv":
            yield line.split(';')[0], 'Filial' + ':' + line.split(';')[1]

def reducefn(k,v):
    print 'reduce' + k
    total = 0
    for index, item in enumerate(v):
        if item.split(":")[0] == 'Vendas':
            total = int(item.split(":")[1]) + total
            #print total
        if item.split(":")[0] == 'Filial':
            NomeFilial = item.split(":")[1]
            #print NomeFilial
    L = list()
    L.append(NomeFilial + " , " + str(total))
    #print L
    return L

#def reducefn(k,v):
#    print 'reduce' + k
#    return v
            
s = mincemeat.Server()

s.datasource = source

s.mapfn = mapfn

s.reducefn = reducefn

results = s.run_server(password = "changeme")
#print results
w = csv.writer(open("C:\\Temp\\Exerc\\RESULT.csv","w"))

for k, v in results.items():
    print k,v
    w.writerow([k,str(v).replace("[","").replace("]","").replace("'","").replace(' ','')])
