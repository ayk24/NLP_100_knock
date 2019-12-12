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
    (   
    .*  
    \[\[Category:
    .*
    \]\]
    .*
    ) 
    $ 
    ''', re.MULTILINE + re.VERBOSE)

result = pattern.findall(extract_UK(file_name))

for line in result:
    print(line)
