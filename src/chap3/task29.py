# coding: utf-8
import gzip
import json
import re
import urllib.parse
import urllib.request


def extract_UK(input_file):
    with gzip.open(input_file, 'rt', encoding="utf8", errors='ignore') as lines:
        for line in lines:
            data_json = json.loads(line)
            if data_json['title'] == 'イギリス':
                return data_json['text']


def delete_markup(target):
    pattern = re.compile(r'''
        (\'{2,5})   
        (.*?)       
        (\1)        
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\2', target)

    pattern = re.compile(r'''
        \[\[       
        (?:        
        [^|]*?  
        \|      
        )??         
        ([^|]*?)    
        \]\]        
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)


    pattern = re.compile(r'''
        \{\{lang   
        (?:        
        [^|]*?  
            \|      
        )*?         
        ([^|]*?)    
        \}\}        
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)

    pattern = re.compile(r'''
        \[http:\/\/
        (?:        
            [^\s]*? 
            \s      
        )?          
        ([^]]*?)    
        \]          
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub(r'\1', target)

    pattern = re.compile(r'''
        <          
        \/?        
        [br|ref]   
        [^>]*?     
        >          
        ''', re.MULTILINE + re.VERBOSE)
    target = pattern.sub('', target)

    return target


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
for field in fields:
    result[field[0]] = delete_markup(field[1])

file_name_flag = result['国旗画像']

url = 'https://www.mediawiki.org/w/api.php?' \
    + 'action=query' \
    + '&titles=File:' + urllib.parse.quote(file_name_flag) \
    + '&format=json' \
    + '&prop=imageinfo' \
    + '&iiprop=url'

request = urllib.request.Request(url,
    headers={'User-Agent': '@ayk24'})
connection = urllib.request.urlopen(request)

data = json.loads(connection.read().decode())

url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']
print(url)
