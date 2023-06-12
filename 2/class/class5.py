# python が元々持っているライブラリ
import math

# print(math.pi)

import calendar
cal = calendar.TextCalendar()
print(cal.pryear(theyear=2022))


# from モジュール名 import クラスや関数、変数
from calendar import TextCalendar

cal = TextCalendar()
cal.pryear(theyear=2023)


from datetime import date
today = date()