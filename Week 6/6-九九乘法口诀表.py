# 打印生成九九乘法口诀表

for i in range(1,10): # 行
    for j in range(1,i+1): # 列
        print(i,"*",j,"=",i*j,end=" ") # 横着生成
    print() # 换行