def message(s=None):
    if s is None: # s == None と描きたくなったら、isを使う
        print('文字列が未入力です')
    else:
        print('入力文字列は「' + s + '」です')

# 'Hello World'は実引数とも呼ぶ
# 関数呼び出しの際に、引数名=値のように渡すことができる
message('Hello World')
message()
