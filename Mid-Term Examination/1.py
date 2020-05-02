# 编写程序，打印如下图形。1.把程序代码粘贴到下方, 2.然后把代码和运行结果屏幕截图贴到后面。

def print_triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

print_triangle(5)