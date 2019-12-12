# coding: utf-8

file_name = "./data/hightemp.txt"
count = 0

with open(file_name, encoding="utf8", errors='ignore') as input_file:
    for line in input_file:
        print(line.replace('\t', ' '), end='')
