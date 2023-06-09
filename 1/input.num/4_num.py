print(3+2)
print(3-2)
print(3*2)
print(3/2)
print(3%2)

a = 100
b = 15
print(a % b)


num1 = input('数字を入力してください')
num2 = input('数字を入力してください')
# input は文字列になるため、数字として使用できない。int型にして数字として使用できるようにする必要がある。
int_num1 = int(num1)
int_num2 = int(num2)

print(int_num1 * int_num2)