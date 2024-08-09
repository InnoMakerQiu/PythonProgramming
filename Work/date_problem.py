# import datetime

# start_date = datetime.date(1901, 1, 1)
# end_date = datetime.date(2000, 12, 31)

# count = 0
# current_date = start_date
# while current_date <= end_date:
#     if current_date.weekday() == 0:  # 0 表示星期一
#         count += 1
#     current_date += datetime.timedelta(days=1)

# print(count)

import datetime

start_date = datetime.date(1901, 1, 1)
end_date = datetime.date(2000, 12, 31)

total_days = (end_date - start_date).days

start_weekday = start_date.weekday()  # 0 表示星期一

count = (total_days+start_weekday) // 7  # 计算完整的星期数

if start_weekday == 0:
    count += 1

print(count)


# 小蓝计划在某天的日期中出现 1 时跑 5 千米，否则只跑 1 千米。注意日期中出现 1 不仅指年月日也指星期。
# 请问按照小蓝的计划，20232023 年小蓝总共会跑步锻炼多少千米?
# 例如，5 月 1 日、1 月 13 日、11 月 5 日、4 月 3 日 (星期一) 小蓝会跑 5 千米，
# 而 5 月 23 日小蓝会跑 1 千米 (示例日期均为 2023 年)

# 做题感想
# 需要注意index的索引的值，一般默认是从0开始的。
# 注意星期标号，星期一为0-星期天为7
# 一旦发现代码那里出现了错误


import os
import sys

# 月份天数，考虑到2023年不是闰年
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def has_one(num):
    num_str = str(num)
    for digit in num_str:
        if digit == '1':
            return True
    return False

# 由于4月3日为星期一，所以可以推测1月1号为星期天
week_day = 6
day_5km = 0
# 
for index, element in enumerate(month_days):
#   print(f"The day is {day_5km}")
#   print(f"The month day is {element}")
  if has_one(index+1): 
    day_5km+=element
    week_day+=element
    week_day = week_day % 7
    continue
  for i in range(1, element+1):
    if has_one(i):
      day_5km += 1
    elif week_day == 0:
        day_5km += 1
    week_day += 1
    week_day = week_day % 7

day_1km = 365-day_5km
day_total = day_5km*5+day_1km*1
print(day_total)
