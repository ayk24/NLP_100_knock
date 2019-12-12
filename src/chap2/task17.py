# coding: utf-8

file_name = './data/hightemp.txt'
with open(file_name, encoding="utf8", errors='ignore') as input_file:
    set_ken = set()
    for line in input_file:
        cols = line.split('\t')
        set_ken.add(cols[0])

for n in set_ken:
    print(n)
