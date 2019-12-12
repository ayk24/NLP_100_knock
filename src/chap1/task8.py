
def cipher(target):
    result = ""

    for char in target:
        if char.islower():
            result += chr(219-ord(char))
        else:
            result += char

    return result


target_str = "I couldn't believe that I could actually understand " \
             "what I was reading : the phenomenal power of the human mind ."
conversion_str = cipher(target_str)

print("入力文: " + target_str)
print("暗号文: " + conversion_str)
print("復号文: " + cipher(conversion_str))
