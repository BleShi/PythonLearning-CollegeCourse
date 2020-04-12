# 求一元二次方程的根
import math
a=float(input("请输入一元二次方程的二次系数："))
b=float(input("请输入方程的一次系数："))
c=float(input("请输入方程的常数项："))
if a==0:
    print("方程二次系数不能为0！")
else:
    delta=b*b-4*a*c
    x=-b/(2*a)
    if delta==0:
        print("方程有唯一解，即X=",x)
    elif delta>0:
        x1=x-math.sqrt(delta)/(2*a)
        x2=x-math.sqrt(delta)/(2*a)
        print("方程有个两个实根，分别是X1=",x1,",X2=",x2)
    else:
        x1=(-b+complex(0,1)*math.sqrt((-1)*delta))/(2*a)
        x2=(-b-complex(0,1)*math.sqrt((-1)*delta))/(2*a)
        print("方程有个两个虚根，分别是X1=",x1,",X2=",x2)