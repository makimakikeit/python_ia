# 文字列の分割
food_list = 'apple, banana, orange'
food = food_list.split(',')
print(food)

food_text = ','.join(food)
print(food_text)

print("--------------")

user_file_text = """
hoge
fuga
taro
ziro
saburo
"""
file_text = sorted(user_file_text.split())
result = ' '.join(file_text)
print(result)
result2 = '\n'.join(file_text)
print(result2)
