# 打印生成九九乘法口诀表
for x in range(1,10):
    for y in range(1,x+1):
        print("%d*%d=%2d" % (x,y,x*y),end=" ")
    print("")