# 用户输入公元年份和月份，程序输出这个月的日历（注意区分闰年和平年，2月份天数不同）。

import calendar # 调用日历库

year = int(input("请输入年："))

month = int(input("请输入月："))

calendar.setfirstweekday(calendar.SUNDAY)

print(calendar.month(year,month))