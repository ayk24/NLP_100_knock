
org_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
split_str = org_str.split(' ')
result = []

for word in split_str:
    count = 0
    for char in word:
        if word.isalpha():
            count += 1
    result.append(count)

print(result)
