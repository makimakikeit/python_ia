# 組み込み関数
user_name = input('名前を入力してください： ')
# print('こんにちは、' + user_name)
result = f'こんにちは、{user_name}'
print(result)

# formatで、変数を埋め込める
# 'こんにちは{}'.format(user_name)