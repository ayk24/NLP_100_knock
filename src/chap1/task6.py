
def gen_ngram(n, target_str):
    result = []

    for i in range(0, len(target_str) - n + 1):
        result.append(target_str[i:i+n])

    return result


# 集合にはset型を使う
set_x = set(gen_ngram(2, "paraparaparadise"))
set_y = set(gen_ngram(2, "paragraph"))

# set_or = set_x | set_y
set_or = set_x.union(set_y)

# set_and = set_x & set_y
set_and = set_x.intersection(set_y)

# set_sub = set_x - set_y
set_sub = set_x.difference(set_y)

print("X : " + str(set_x))
print("Y : " + str(set_y))
print("和: " + str(set_or))
print("積: " + str(set_and))
print("差: " + str(set_sub))
print("Xに'se'が含まれているか: " + str('se' in set_x))
print("Yに'se'が含まれているか: " + str('se' in set_y))
