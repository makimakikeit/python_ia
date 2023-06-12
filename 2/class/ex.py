# 演習１：関数を作成し１〜１００までのfizzbuzzをする
# def fizzbuzz(first, end):
#     for i in range(first, end):
#         if i % 15 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)
# fizzbuzz(1, 101)

# 演習２：改良版
def fizzbuzz(first=10, end=20):
    for i in range(first, end):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

# ここに数字を入れれば、その数字で実行される
fizzbuzz(1, 101)
fizzbuzz()
