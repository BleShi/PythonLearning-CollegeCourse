# 用户输入两个正整数，求他们的最大公约数。
m=int(input("请输入正整数："))
n=int(input("请再输入一个正整数："))
min=m
if m>n:
    min=n
for i in range(min,1,-1):
    if m%i==0 and n%i==0:
        print(m,"和",n,"的最大公约数是：",i)
        break