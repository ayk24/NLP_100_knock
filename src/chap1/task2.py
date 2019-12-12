
org_str1 = "パトカー"
org_str2 = "タクシー"
# str.join(): タプルを文字列に
result = ''.join(x + y for (x, y) in zip(org_str1, org_str2))
print(result)
