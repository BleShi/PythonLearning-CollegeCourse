# 闰年平年判断
year=int(input("请输入一个公元年份："))
if(year % 4==0 and  year%100!=0) or (year%400==0):
    print("公元",year,"年是闰年")
else:
    print("公元",year,"年是平年")