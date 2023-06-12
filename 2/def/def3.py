# 変数や関数名は、すべて小文字で、単語の間にアンスコをつける
# get_tax
# my_name
# def tax(price):
#     tax = int(price * 0.1)
#     return tax
#
# a = tax(75)
# b = tax(1980)
# print(a)
# print(b)


def tax(price):
    tax = int(price * 0.1)
    price_including_tax = int(price * 1.1)
    paypal_tax = int(price * 5)
    return price_including_tax,  paypal_tax, tax

# 複数の戻り値がある時、代入も複数の変数を適宜できる
# a, b, c, d = [110, 10, 1, 2]
a, b, c = tax(100)
print(a)
print(b)
print(c)
