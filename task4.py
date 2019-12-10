
first_only = (1, 5, 6, 7, 8, 9, 15, 16, 19)
org_str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.' \
          ' New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
result = {}

split_str = org_str.split(' ')
for (num, word) in enumerate(split_str, 1):
    if num in first_only:
        result[word[0:1]] = num
    else:
        result[word[0:2]] = num

print(result)
