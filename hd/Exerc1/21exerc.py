import mincemeat
import glob
import csv

text_files = glob.glob("C:\\Temp\\Exerc\\Textos\\*")

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

start_time = time.time()
source = dict((file_name, file_contents(file_name)) for file_name in text_files)
end_time = time.time()

def mapfn(k,v):
    print 'map ' + k
    from stopwords import allStopWords
    for line in v.splitlines():
        for word in line.split():
            if (word not in allStopWords):
                yield word, 1

def reducefn(k,v):
    print 'reduce ' + k
    return sum(v)

s = mincemeat.Server()

s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password = "changeme")

print 'Aqui1'
w = csv.writer(open("C:\\Temp\\Exerc\\RESULT.csv","w"))
print 'Aqui2'
for k, v in results.items():
    w.writerow([k,v])
                    
print("Elapsed time was %g seconds" % (end_time - start_time))                    
