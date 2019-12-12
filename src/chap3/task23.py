# coding: utf-8
import gzip
import json
import re


def extract_UK(input_file):
    with gzip.open(input_file, 'rt', encoding="utf8", errors='ignore') as lines:
        for line in lines:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']


file_name = './data/jawiki-country.json.gz'
pattern = re.compile(r'''
    ^       
    (={2,}) 
    \s*     
    (.+?)   
    \s*     
    \1      
    .*      
    $       
    ''', re.MULTILINE + re.VERBOSE)

result = pattern.findall(extract_UK(file_name))

for line in result:
    level = len(line[0]) - 1
    print('{indent}{section}({level})'.format(
        indent='\t' * (level - 1), section=line[1], level=level))
