# 用函数递归求任意正整数的正整数次方

n=int(input("请输入一个正整数："))

def calc(n):
    if n == 1:
        return 1
    else:
        return n * calc(n-1)

print(calc(n))