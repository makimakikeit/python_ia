import datetime
now = datetime.datetime.now()
today = datetime.date.today()

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

text = f'{now.year}年{now.month}月{now.day}日{now.hour}時{now.minute}分{now.second}秒'
print(text)

# 2023年06月12日 16時26分40秒
text = now.strftime('%Y年%m月%d日 %H時%M分%S秒')
print(text)

print(today)

import datetime

day_string = input('Y/m/d H:M:S 形式で! > ')
# 2023/01/01 00:00:00といった感じで入力するsuru
day_dt = datetime.datetime.strptime(day_string, '%Y/%m/%d %H:%M:%S')

# 20日後
days_after_20 = day_dt + datetime.timedelta(days=20)  # hoursで追加する時間、secondsで追加する秒
print(days_after_20)