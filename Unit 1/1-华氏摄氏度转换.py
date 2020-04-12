# 华氏摄氏度转换
# -*- coding: utf-8 -*-
    
temp_str = input("请输入带符号的温度值，如'23c'，'34f'")
if temp_str[-1] in ['F','f']:
    temp_Cels = (eval(temp_str[0:-1]) -32) / 1.8
    print("转换后的温度是 %.2f摄氏度" % temp_Cels)
elif temp_str[-1] in ['C','c']:
    temp_Farhr = 1.8 * eval(temp_str[0:-1]) + 32
    print("转换后的温度是{:.2f}华氏度".format(temp_Farhr))
else:
    print("格式错误")