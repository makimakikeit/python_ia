data_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
print(data_list)
print(data_list[:5])

data_list = [
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9] # 2
]
print(data_list[1][1]) # 5を取り出す

food = ['apple', 'gapes', 'orange']
# 上書きができる
food[1] = 'grape'
# 追加ができる
food.append('tomato')
# 指定した場所に追加する
food.insert(0, 'suika')
print(food)
# 指定した場所を削除
food.pop(1)
print(food)
# 指定した要素を削除
food.remove('suika')
print(food)
