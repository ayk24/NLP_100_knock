
def gen_ngram(n, target_str):
    result = []

    # range(iのはじめ, iのおわり)
    for i in range(0, len(target_str) - n + 1):
        result.append(target_str[i:i+n])

    return result


org_str = "I am an NLPer"
words_split = org_str.split(' ')

# 単語 bi-gram
word_bi_gram = gen_ngram(2, words_split)

# 文字 bi-gram
char_bi_gram = gen_ngram(2, org_str)

print(word_bi_gram)
print(char_bi_gram)
