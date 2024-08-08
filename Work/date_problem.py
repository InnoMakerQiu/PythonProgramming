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