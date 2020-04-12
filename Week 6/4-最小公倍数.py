#  用户输入两个正整数，求他们的最小公倍数。
num1 = eval(input("请输入第一个数字： "))
num2 = eval(input("请输入第二个数字： "))

if num1<= 0 or num2 <= 0:
    print("两个数必须是正整数")
    exit(0)

if num1>num2:
    max=num1
    min=num2
else:
    max=num2
    min=num1
    
for i in range(1,min+1):
    numtemp=max*i
    if numtemp % min == 0:
        numresult=numtemp
        break

print("最小公倍数是：",numresult)