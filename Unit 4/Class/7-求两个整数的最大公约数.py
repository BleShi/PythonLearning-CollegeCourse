# 求两个整数的最大公约数
# 基本方法是先求两者较小的那个，然后循环变量从较小的变量向1倒退，当循环变量同时被两者整数时，最大公约数就找到了，立即退出循环。
m=int(input("请输入正整数："))
n=int(input("请再输入一个正整数："))
min=m
if m>n:
    min=n
for i in range(min,1,-1):
    if m%i==0 and n%i==0:
        print(m,"和",n,"的最大公约数是：",i)
        break