# coding: utf-8

file_name = './data/hightemp.txt'
n = int(input('N: '))

if n > 0:
    with open(file_name, encoding="utf8", errors='ignore') as input_file:
        lines = input_file.readlines()

    for line in lines[-n:]:
        print(line.rstrip())
