# 関数の外側で定義した変数は　、関数の中からでも見れる
# 関数の中で定義した　変数は、関数の外に出ると消滅する
# 関数の中、外側の変数を書き換えることは(基本的に)できない
def plus_g(a):
    print('gの値は' + str(g) + 'です')
    f = a + g
    d = a - g
    return f, d

g = 1
print(plus_g(3))

def tax(price):
    tax = int(price * 0.1)
    print(tax)
    result = int(price * 1.1)
    return result
a = tax(100)
b = tax(1980)
print(a)
print(b)
