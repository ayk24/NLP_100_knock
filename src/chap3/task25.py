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
    ^\{\{基礎情報.*?$
    (.*?)       
    ^\}\}$      
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

contents = pattern.findall(extract_UK(file_name))

pattern = re.compile(r'''
    ^\|         
    (.+?)       
    \s*         
    =
    \s*         
    (.+?)       
    (?:         
    (?=\n\|) | (?=\n$)   
    )           
    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

fields = pattern.findall(contents[0])

result = {}
keys = []
for field in fields:
    result[field[0]] = field[1]
    keys.append(field[0])

for item in sorted(result.items(),
                   key=lambda field: keys.index(field[0])):
    print(item)
