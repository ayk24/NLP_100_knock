# coding: utf-8
import math

file_name = './data/hightemp.txt'
n = int(input('N: '))

with open(file_name, encoding="utf8", errors='ignore') as input_file:
    lines = input_file.readlines()

# ceilは切り上げ
lines_len = len(lines)
unit = math.ceil(lines_len / n)

for i, j in enumerate(range(0, lines_len, unit), 1):
    with open('./data/unit_{:02d}.txt'.format(i), mode='w', encoding="utf8", errors='ignore') as out_file:
        for line in lines[j:j + unit]:
            out_file.write(line)
