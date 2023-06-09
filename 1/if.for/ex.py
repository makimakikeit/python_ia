# for i in range(1, 101):
#     if i > 1:
#         for num in range(2, int(i ** 0.5) + 1):
#             if (i % num) == 0:
#                 break
#         else:
#             print(i)

for i in range(2, 101):
    prime = True
    for j in range(2, i):
#        print(f'i={i} j={j}')
        if i % j == 0:
 #           print(f'i={i} j={j}')
            prime = False
    if prime:
        print(i)


def is_prime(number):
    # 引数のnumberが素数ならTrueを返す
    for j in range(2, number):
        # print(f'  j={j}')
        if i % j == 0:
            return False
    # 割り切れなかったら（素数じゃなかったら）ここに到達する
    return True

for i in range(2, 101):
    if is_prime(i):
        print(i)