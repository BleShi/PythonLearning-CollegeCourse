# 用户输入一个正整数N，计算从1到N（包含1和N）相加之后的结果。
num=input("请输入一个数： ")
num=int(num)
num=num+1
sum=0
for i in range(num):
    sum=sum+i
print("从1到N（包含1和N）相加之后的结果是：",sum)