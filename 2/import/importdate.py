import datetime

# 年 月 日 時 分 秒
# 2023/6/12 9:00:00
one_day = datetime.datetime(2023, 6, 12, 9, 0, 0)
print(one_day)

# 20日後
days_after_20 = one_day + datetime.timedelta(days=20)
print(days_after_20)