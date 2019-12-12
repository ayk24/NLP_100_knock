# coding: utf-8

file_name = './data/hightemp.txt'
n = int(input('N: '))

with open(file_name, encoding="utf8", errors='ignore') as input_file:
    for i, line in enumerate(input_file):
        if i >= n:
            break
        print(line.rstrip())
