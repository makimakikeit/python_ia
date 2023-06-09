number_list = [12, 34, 64, 2, 67, -2, 90]

for number in number_list:
    if number < 10:
        print('処理を停止しました')
        continue
        # break
    else:
        print(number)