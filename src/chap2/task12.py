# coding: utf-8

file_name = './data/hightemp.txt'

with open(file_name, encoding="utf8", errors='ignore') as input_file, \
        open('./data/col1.txt', mode='w', encoding="utf8") as col1_file, \
        open('./data/col2.txt', mode='w', encoding="utf8") as col2_file:

    for line in input_file:
        cols = line.split('\t')
        col1_file.write(cols[0] + '\n')
        col2_file.write(cols[1] + '\n')
