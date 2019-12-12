# coding: utf-8

with open('./data/col1.txt', encoding="utf8") as col1_file, \
        open('./data/col2.txt', encoding="utf8") as col2_file,\
        open('./data/merge_col1_col2.txt', mode='w', encoding="utf8") as out_file:

    # zip(): 複数のシーケンスをまとめてループ
    # text.rstrip(): textの先頭や末尾の空白を削除する
    for col1_line, col2_line in zip(col1_file, col2_file):
        out_file.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')

