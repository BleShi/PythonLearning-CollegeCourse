# 用户输入三个数值（可能是整数，也可能是小数），比较大小，然后分别输出最大值和最小值。

num1=input("请输入一个数： ")
num2=input("请输入第二个数： ")
num3=input("请输入第三个数： ")
numall=[num1,num2,num3]
print("最大的数是：",max(numall))
print("最小的数是：",min(numall))