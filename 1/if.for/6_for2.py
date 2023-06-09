# dic = {'商品A': 3, '商品B': 10, '商品C': 7, '商品D': 5}
#
# print('商品一覧')
#
# for key in dic.keys():
#     print(key)
#
# print('\n商品と在庫数の一覧')
# for key, value in dic.items():
#     print('商品名：' + key + '\t在庫数：' + str(value))
#

tuple_list = [
    ('商品A', 3),
    ('商品B', 10),
    ('商品C', 7),
    ('商品D', 5),
]

for key, value in tuple_list:
    print(key)
    print(value)