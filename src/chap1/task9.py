import random


def Typoglycemia(target):
    result_list = []

    for word in target.split(' '):
        if len(word) <= 4:
            result_list.append(word)
            # print(result_list)
        else:
            random_list = list(word[1:-1])
            random.shuffle(random_list)
            result_list.append(word[0] + ''.join(random_list) + word[-1])

    return ' '.join(result_list)


target_str = "I couldn't believe that I could actually understand " \
             "what I was reading : the phenomenal power of the human mind ."

result = Typoglycemia(target_str)
print(result)
