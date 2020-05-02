# 编写函数print_diamond(n)，要求n为任意大于5的奇数时，打印出菱形。如当输入为9的奇数的时候，打印如下图形。
# 1.把程序代码粘贴到下方。
# 2.然后把代码和运行结果屏幕截图贴到后面。


def print_diamond(n):
    diamond = int(n/2) + 1
    for i in range(1, n+1):  
        if i % (n-1) == 1:
            print(' '*diamond, '*')
        else:
            print(" " * abs(i-diamond), "*", ' '*((diamond-abs(i-diamond))*2-3), '*')

n_user = int(input("请输入一个数： "))

if n_user > 5 and n_user % 2 != 0:
    print_diamond(n_user)
else:
    print("请输入一个大于5的奇数哦!")