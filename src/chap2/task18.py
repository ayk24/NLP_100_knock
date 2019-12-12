# coding: utf-8

file_name = './data/hightemp.txt'
lines = open(file_name, encoding="utf8", errors='ignore').readlines()
lines.sort(
    key=lambda line: float(line.split('\t')[2]),
    reverse=True,
)

for line in lines:
    print(line, end='')
