# 根据以下常识，设计函数isleapyear()判断某个年份是否为闰年，闰年返回True，平年返回False。在主程序中调用该函数，判断1900、1980、1999、2000、2019年是否为闰年，用print()输出"公元某年是闰年"或“公元某年是平年”。
# 注意:   程序只运行一次，就得出全部结果,不得使用input()函数或以反复调用的方式得出结果。isleapyear()函数内部不得使用print()函数。否则不给分。
# 常识：闰年是公历中的名词。闰年分为普通闰年和世纪闰年。
# 普通闰年:公历年份是4的倍数的，且不是100的倍数，为普通闰年。（如2004年就是闰年）；
# 世纪闰年:公历年份是整百数的，必须是400的倍数才是世纪闰年（如1900年不是世纪闰年，2000年是世纪闰年）；

def isleapyear (yeartocheck):
    if yeartocheck%4 == 0:
        return (True)
    else:
        return (False)

yearchecking = [1900,1980,1999,2000,2019]

for i in yearchecking:
    if isleapyear(i) is True:
        print("公元",i,"年是闰年")
    if isleapyear(i) is False:
        print("公元",i,"年是平年")