# coding: utf-8
import gzip
import json

file_name = './data/jawiki-country.json.gz'

with gzip.open(file_name, 'rt', encoding="utf8", errors='ignore') as data_file:
    for line in data_file:
        data_json = json.loads(line)
        if data_json['title'] == 'イギリス':
            print(data_json['text'])
            break
