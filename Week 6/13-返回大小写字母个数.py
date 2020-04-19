# 设计一个函数, 接收字符串参数，返回大写字母个数和小写字母个数

def letter_num(words):
    upper = 0
    lower = 0
    for word in words :
        if word.isupper():
            upper+=1
        if word.islower():
            lower+=1
    return(upper,lower)
words='\"ABCisDEFG\"'
(upper,lower)=letter_num(words)
print(("字符串%s中大写字母的个数是：")%words,upper,"，小写字母的个数是：",lower)