# r = range(10)
# # r = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9]
# print(r)

# 指定回数の繰り返しは、iという関数を使用するのが一般的
for i in range(2,10):
    # print(i, end=' ')
    # print()
    for j in range(2, i):
        print(j, end=' ')

print()