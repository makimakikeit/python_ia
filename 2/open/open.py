# with open() とすると、エラーが起きても、必ずファイルを閉じてくれる
# ファイルの上書き
# with open('sample.txt', 'w', encoding='utf-8') as file:
#     file.write('２行目\n')
#     file.write('２行目\n')

# r 読み込みモード
# encoding='utf-8'と必ずつける
# 読み込んだ時、文字化けしたら'cp932'
with open('sample.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    print(text)

    for line in file:
        print(line, end='')