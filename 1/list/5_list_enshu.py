# 演習１ 5を取り出す
data_list = [1, 2, [3, 4, 5], [6, 7], 8, 9, [10, 11]]
print(data_list[3][1])

# 演習２
list = []
number1 = input("数値を入力してください：")
list.append(int(number1))
number2 = input("数値を入力してください：")
list.append(int(number2))
number3 = input("数値を入力してください：")
list.append(int(number3))
list.sort()
print(list)

# 演習３
list1 = []
number1 = input("数値を入力してください：")
list1.insert(0, int(number1))
number2 = input("数値を入力してください：")
list1.insert(0, int(number2))
number3 = input("数値を入力してください：")
list1.insert(0, int(number3))
sorted_list1 = sorted(list1, reverse=True)
print(sorted_list1)
